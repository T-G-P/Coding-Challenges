payperks coding challenge
=========================

Here we have the pay perks coding challenge. This is the second time I've touched django in
over a year and I really had a great time this time around. The first time I used django I was 
still a student and everything about it was overwhelming. This time around after using
flask for a while, I really was able to appreciate the features that django has to offer. 
Postgres was chosen as the persistent data store.

Currently live at http://tobias.perelste.in:8005/

Modules
=======
# payperks.login
This module contains the models, views, and controllers for the login system. 
It's heavily inspired from resources I've found online. Credit is given where it's due. 
This is still a work in progress.

## models
For the purpose of the application
the default Django User does not contain enough fields so I extended the User and made a
UserProfile model that contains all the other relevant fields. I import the signals module
so that the UserProfile table is populated automatically on User object creation.


## views
The login module views are farely straight forward. The register view creates a new user and processes
the input. The other views either render the templates associated to them or redirect the user
to a different page

## forms

The registration form class handles all the registration form input validation.


# payperks.sweepstakes
Here lies the core of the application. It is still a work in progress, but the core functionality
behind the application is implemented. 

## models
I designed the sweepstakes to support two models (Sweep and Drawing). These relatoinships allow for
straight forward querying and basic logic. Sweeps have a one to many relatoinship with 
drawings. Users also have a one to many relationship with drawings. 
The sweep also stores the prize amount and number of prizes at launch which are  arbitrarily determined 
using a small utility function in sweepstakes/utils.py. I tried to design a system where the data was as normalized
as possible. 

## views

The sweepstakes supports the main views outlined in the writeup. An admin user can run the sweep process
in which drawings are queried for and the highest open drawings are selected as winners based on
the number of prizes configured at the launch of the sweep.  Here are the following views

### earn points (POST)
When a user visits this view, a drawing object is created and is set with a random amount of points. 
These points will later be used by another view to determine the winner. The drawing is then appended to the users queryset.

### run sweeps (POST)
When the admin runs the sweep process, a sweep object is created. Aftewrad, all of the current open drawings are found. With the open drawings, the winners are then determined based on the number of prizes initialized with the sweep. At this point, every drawing is marked closed and it is marked as a winner depending on the points scored.


###  check_or_claim_prize(GET, POST)
With this view, the user either sends a GET OR POST request. Regardless of the request, if no
winning drawings are found, the status is reflected in the view. Otherwise, the user can either claim
or check the status of their prize. 
