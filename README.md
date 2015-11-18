README
======

## 3rd party 
All 3rd party api requests are done with Guzzle v6
3rd party api calls are abstracted and located in 'app/services'
The AbstractApi class is designed to be inherited from for any 3rd party api request.
The CredlyApi class extends that class and handles the actual api calls. I plan
to implement other endpoints in this class for more functionality.

## Routes
At the moment there is only one route and that is to retrieve information for 
any specified badge id.

## Controllers
In 'Http'/Controllers' I implemented a BaseController class which is
used to instantiate the CredlyApi class and make the credly api call with the guzzle
instance parameter
