README
===================
@Author Tobias Perelstein

The following readme will provide an overview of the design and functionality of the api

Production
-------------
The api is currently live with BASE URL:

[http://tobias.perelste.in:8002/vimeo/api/v1.0/](http://tobias.perelste.in:8002/vimeo/api/v1.0/)

Overall API usage is documented at the bottom of this README.


Specs/Tech
-------------

The api is built with python on top of flask. It is served with uwsgi under nginx. 
I used PostgreSQL for persistent  data storage and Redis caching all 4XX status code responses. I used Postgres to set up simple single table database which stores all information relevant to a file upload such as filename, filehash, password if supplied, created date.

Additionally, I am using a Celery as a task queue for handling file deletion asynchronously so that the download requests are faster. In addition to the Redis instance I'm using for caching, I also set up a Redis instance as a backend for the Celery task queue which is used for permanently removing files off of the file system after they are downloaded. 

I used both Flask Sql Alchemy and Flask Migrate (built on top of Alembic) flask extensions to build and manage the database migrations as well. 

I configured the flask app to be run with Uwsgi and Nginx.  

Benchmarked with siege at 100 concurrent requests per second. Varies with increasing duration. 

Requirements
-----------------
Before being able to run the application locally, you will need to install python2.7+, pip, virtualenv, and postgresql9.3+, redis. You will also need to set up a table named 'vimeo' as well as a postgres user. 

> **Installation all dependencies**
> pip install -r requirements.txt 
>  **Run locally with**
> python manage.py runserver
>
>Additionally, can also be set up with nginx/uwsgi using the api_* .conf/.ini files.
Configurations scripts for both instances of redis, and celery will also need to be configured and I provided my celery and redis configs and daemonization scripts here.

Design/Decisions/Data Structures
-------------------
I chose the factory pattern for creating the flask app instantiation due to
its ease of flexibilty, extensibility and modularity. I know that this application only
has two endpoints, but I designed it with big things in mind. Currently, the application is divided into one module (api) which contains the database models and api controller. 

The main vimeo_api module exposes all the extensions that are used throughout the application.  Overall, I built the application with MVC in mind. There are no views, just models and controllers for the api module. 

I chose flask due to having the most experience with it. I'm also an enthusiast and have written a few flask applications in my free time. I enjoy it for it's compactness, performance, and great community. I chose uwsgi and nginx due to having had experience with them before and being able to get pretty decent performance and scalability. 

I picked Postgres for the initial data store as I wanted a reliable persistant data storage and it was what I was experienced with most. I contemplated using Redis for everything, but decided not to as the database is very simple for the app and I woudln't ever have to worry about the redis instance dying. 

I knew that I could cache the 4XX responses so I could handle more concurrent requests so I chose Redis as a backend for storing those responses and I made use of the Flask-Cache extensions which made it very easy to wrap the responses with a decorator. 

Lastly all files are not served by Flask but by nginx. This was one of my bigger decisions. Despite the api not getting much use at the moment, nginx is tremendously faster than flask and is much better for serving static content and this would scale much better. In order to do this, I needed to flask to send a specific header which provides a redirect to nginx, which in turn is aliases to a directory on the filesystem. This way, flask does not have anything to do with the file serving and is only used for application logic. 

Models
----------------
**File**

The File model represents the file that is being uploaded/downloaded. The file model provides information such as the filename, unique filehash, creation time, and status (whether it's available for download or gone). In order to be able to store a file uniquely for each request, I hashed each file name with its creation time using the MD5 hash algorithm and I then created a folder on the filesystem with this hash. Inside this folder, I store the original file with its original name
intact for download. This hash is also used for retrieving the file from the file system when visiting the download endpoint. 

The file model contains several methods as well, mainly for password hashing/verification, and file hashing. IF a user supplies a password, this password is hashed using sha256. If a user needs to download a password protected file, the password they supply with the GET request is validated by the validate_password method in the file class 



Controllers
--------------
The main api controller is where the bulk of the application logic occurs. 

A request comes into my api. The parameters get processed by the
/file endpoints. The allowed methods for the api are PUT and GET 

Upon sending a PUT request, I verify to see if there is a file sent with the request at all. If not, I return a 400 Bad Request error.

Regardless of whether or not a password is sent, I take the form value for the password key and send it off to the add_file method of the File class which is a static method. This method creates a new file record in the database and performs all the necessary options such as hashing the password if it exists, creating the filehash, etc. The file is then written to the filesystem and a 201 success response is returned containing a success message as well as a download url for the GET
request

Upon sending a GET request to the url returns from the PUT, the filehash in the url is verified and the password is validated if the file is password protected. If the file is not found a 404 response is returned. If, the file is no longer available, a 410 response is returned. if the file is password protected but no password was sent, a 401 response is returned, and if the password is incorrect, a 401 response is returned. If all goes well, the file hash is verified
against the database and the file is found on the filesystem. The mimetype is found from the file using the built in python mimetype library and the response is returned. 

API OVERVIEW
------------
# API BASE URL
http://tobias.perelste.in:8002/vimeo/api/v1.0/

# PUT
## Upload File [/file] 
This endpoint allows you to upload a file with an optional password. Only allowed method is PUT so a 405 will be returned for other request methods.
* NOTE: The endpoint allows for a maximum file size of 16 megs. The web server will return a 413: Request Entity too Large for anything larger. 
### params
        file - the file being sent *REQUIRED
        password - the password for the file *OPTIONAL


#### Python example request to upload a photo
```python
import requests

url = 'http://tobias.perelste.in:8002/vimeo/api/v1.0/file'

files = {'file': open('report.xls', 'rb')}
data = {'password': 'hello world'}
res = requests.put(url, files=files, data=data)
```
### Upload photo [PUT]

### Possible Responses

+ Response 201 (application/json)

        {
            "status": "File Uploaded Successfully",
            "url": "http://tobias.perelste.in:8002/vimeo/api/v1.0/file/d1c5b168e5782c80fe36f601a9df3b47"
        }
+ Response 400 (application/json)

        {
            "error" : "Bad Request"
        }

+ Response 404 (application/json)

        {
            "error" : "Not Found"
        }
+ Response 405 (application/json)

        {
            "error" : "Method not Allowed"
        }

# GET
## Download Photo [/file/<filehash>]
This endpoint allows you to retrieve a file based on its hash. 

### query string params
        password - the password for the file *OPTIONAL

#### Python example request to download a file
```python
import requests

url = 'http://tobias.perelste.in:8002/vimeo/api/v1.0/file'

params = {'password': 'd1c5b168e5782c80fe36f601a9df3b47'}

res = requests.get(url, params=params)
```
### Download photo [GET]

### Possible Responses

+ Response 200 (original content type)

+ Response 400 (application/json)

        {
            "error" : "Bad Request"
        }

+ Response 404 (application/json)

        {
            "error" : "Not Found"
        }
+ Response 405 (application/json)

        {
            "error" : "Method not Allowed"
        }
        
+ Response 410 (application/json)

        {
            "error" : "Gone"
        }
        
