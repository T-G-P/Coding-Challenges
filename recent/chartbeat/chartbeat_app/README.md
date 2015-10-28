
README
===================
@Author Tobias Perelstein

The following readme will provide a brief overview of the design, shortcomings,
and functionality of the api

Production
-------------
The api is currently live at

http://tobias.perelste.in:8080/api/v1.0/increasingconcurrents

You can send a sample request by appending this query string here:

?apikey=317a25eccba186e0f6b558f45214c0e7&host=gizmodo.com

Specs/Tech
-------------

The api is built with python on top of flask. It is served with uwsgi under nginx. 
I used PostgreSQL and Redis for persistant data storage. I used Postgres to set up relations with Hosts, top pages, increasing visitors, and api keys. 

I used an open source tool called requests-cache which adds caching functionality to the python requests package. This is built on top of Redis. I used both Flask Sql Alchemy and Flask Migrate flask extensions to build and manage the database as well as to populate the database with the latest chartbeat results automatically via an hourly cron. 

I configured the flask app to be run with Uwsgi and Nginx.  

I took a look at the chartbeat headers and saw a rate limit header of 200 reqs/minute so I set each chartbeat request to have a timeout of 3 seconds per request. 

Benchmarked with siege at 100 concurrent requests per second. Varies with increasing duration. 

Requirements
-----------------
Before being able to run the application locally, you will need to install python2.7+, pip, virtualenv, and postgresql9.3+. You will also need to set up a table named 'chartbeat' as well as a postgres user. 

> **Installation all dependencies**
> pip install -r requirements.txt 
>  **Run locally with**
> python manage.py runserver
>
>Additionally, can also be set up with nginx/uwsgi using the api_* .conf/.ini files

----------
Design/Decisions
-------------------
I chose the factory pattern for creating the flask app instantiation due to
its ease of flexibilty, extensibility and modularity. I know that this application only
has one endpoint, but I designed it with big things in mind. Currently, the application is divided into one module (api) which contains the database models and api controller. The main chartbeat_app module exposes utility functions and extensions that are used throughout the application.  Overall, I built the application with MVC in mind. There are no views, just models and controllers for the api module. 

I chose flask due to having the most experience with it. I'm also an enthusiast and have written a bunch of flask applications in my free time. I enjoy it for it's compactness, performance, and great community. I chose uwsgi and nginx due to having had experience with them before and being able to get pretty decent performance. 

I picked Postgres for the initial data store as it was what I was experienced with most. I knew that I needed to cache the chartbeat request somehow so that it wouldn't bog down each request. Without it, I was unable to meet the minimum specifications of 100 requests/sec. I found an open source tool called requests-cache which adds caching functionality to the python requests open source package. I picked it due to its flexibility with multiple types of storage. I chose Redis as I've had experience with it before and wanted to get more familiar with it. 

Models
----------------
**Host**
**ApiKey**

The host model represents the host requested and contains all the properties relevant to it such as hostname, top pages, and increasing visitors. Hosts have a one to many relationship between Api Keys. 

The ApiKey model is related to hosts and api keys are valid across multiple hosts.  The database relationship proved to be very useful for having a cron job populate the database with chartbeat data when my api is not being actively requested. 



Controllers
--------------
The main api controller is where the bulk of the application logic occurs. 

A request comes into my api. The parameters get processed by the
increasingconcurrents endpoint. If invalid, I return an unauthorized response.

If the request doesn't pass chartbeat validation, I return a bad request. 

Next, I verify to see if the api key and host exist in the database. If not, I populate the database and set up a relationship with an Api Key. On the first request, there are no increasing visitors so an empty object is returned. 

On Subsequent requests, the chartbeat request is cached for 3 seconds, allowing for better performance. The data returned from subsequent requests is then compared against local data. This comparison is done by converting the chartbeat response objects into dictionaries using the path as the key, and visitors for the values. This way, the calculation of change in visitors is run in O(n) time since a only a single iteration over the most current api call needs to happen and the keys from the latest api call are used on the local data. On iteration occurs using the key from the current data against the same key in the local data. If for some reason a page disappears from the most current result, then this page is ignored. 

Once the result is built, it needs to be sorted by decreasing values. The host object is updated, and the database gets updated with the latest information returned at this point. 

BottleNecks/Improvements
---------------------------------
I built the api using tools/patterns that I was most experienced with. I'm still learning about asynchronous programming. After implementing the API initially,
I did some research and saw that I could use some asynchronous design patterns and gain a huge performance boost without requiring both redis and postgres as data stores. I don't think it's more efficient to do everything in memory, but, I think it would be awesome to apply one 3rd party request across hundreds of concurrent requests instead of needing to have a caching layer for the request. If I had more time, I would try to do something with the Futures python module. 

Another thing I would change is the usage of both postgres and Redis for data storage. I initially chose postgres due to being comfortable with it. But looking back now, I think its unecessary for the scope of the application. I think Redis woud have accomplished what I needed. I do really enjoy the json type feature in postgres though. This made it very easy to deal with returning/setting results and the fact that each object wasn't large, was good enough reason for me to use this feature of postres. 

Lastly, the writeup mentions that returning the difference of visitors between a 5 second period is a bad measurement of increasing. I agree with this, but I couldn't really come up with an implementation of my own. I think generally, it's a better measure to determing something based on a relative rate. A better api would be one that somehow analyzes requests over a certain time period and then provides  measurements across multiple times of day and how the visitors increased/decreased per page. 
