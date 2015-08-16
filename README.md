*MiniVenmo challenge implemented and designed by Tobias Perelstein*


## Requirements:

To execute the code, python 2.7 - 2.7.10 is needed


The application can be run via:

$ python app.py

The script  supports both interactive and new line delimited files for input

To pass a file simply run via:
$ python app.py filename.txt

State will not persist between runs.

### Tests :

Tests are located in the main project folder. Tests are run for the
all the modules of the application

Unit Tests can be run via:
$ python tests.py

# NOTES :
I chose to build the application in python as I enjoy it for its performance, flexibilty,
readability, data structures and community. I also am most experienced with python.

I designed and built the application with MVC in mind. I separated the project
into two main modules:
    
    *Users
    *Transactions
    
both depend on these modules:
    
    *Database
    *MiniVenmo

I broke it down this way because I felt that the payment and feed commands would
be stored as part of a User/Transaction relationship. With a real production application
in mind, I felt that transactions would have their own model and table and Users would
have a one to many relationship for transactions. Once I started buildling the application,
I realized that feeds and transactions were directly related so I separated the 'pay' and
'feed' functionality and put them inside the Transactions model. The Users module
provides a way to retrieve and modify specific properties on a User whereas Transactions
are between multiple Users and this is why I felt it would be better to keep a transactions
model and controller.

The Users and Transactions modules are accesed via a route that process command line
input or file input depending on how the program is executed. I separated the routing logic
to keep things more modular and maintanable. Since the command line is used to access
both resources, I thought it was best to keep all the main application logic separate.

The main routing functionality occurs in: *MiniVenmo.py* where arguments are validated
prior to being sent off to the User and Transaction controllers

Additionally, I abstracted all the app storage functionality into its own script called
*Database.py* located in the same directory as *MiniVenmo.py*. All of the information that
is stored throughout app context is processed by *Database.py* I abstracted all the
storage functionality as it's consistent across all modules and acts as the database layer
for this project. Despite not using a database, I felt that it would be best to keep things
consistent with MVC design where database logic is separate from the main controller logic.

Both the User module and Transaction module have controllers and models associated to them.
The models represent the resources and the controllers deal with all the logic of processing
the models and storing them within the context of the app.

### Main
The main script *app.py* instantiates the MiniVenmo class which is the routing layer of the
whole application. It calls the only public method of the MiniVenmo class which then runs
the application. There's not much to it and I built it this way so that the routeing class
is part of the *minivenmo* module

## Modules
### minivenmo.user

##### Scripts

*user/UsersController.py

*user/models.py

The Users module includes a Users Controller which handles all of the logic for the
'user', 'add', 'balance' commands. The Users Controller processes the input from
the command line and depending on the arguments, will instantiate a User object using
the User object in the *models.py* script. The UsersController makes extensive use of the
app Database for looking up and processing arguments.

The models script contains all the models directly associated with a User. In this case,
I split it up into a *User* model and a *CreditCard* model. However, I chose not to make
the Credit Card class instantiable and made all of its methods static. I broke it up this way
because I felt that credit card processing was specific to credit cards and not a user directly,
but a User should have a credit card property for the purpose of this app. To keep things localized,
I designed the CreditCard model to be used for validation alone. After sucessful credit card
validation, the credit card property of the user gets assigned.

Additional to the basic properties a User object has, I also gave it a static method
to be used for validating names prior to instantiation. I did it this way in order to
prevent user objects from being created and stored with bad input. Since name validation
is an action on a User, I left it as part of the class.

Exceptions are rasied in the database, model, and controller with appropriate
error messages. I designed the app to raise exceptions to make input processing
straight forward and to have the flexibilty of the try/catch. I thought about
building a custom exception class that inherited from Exception,
but for the purpose of this project, I used the default python Exception class.

### minivenmo.transaction

##### Scripts

*transaction/TransactionsController

*transaction/models.py

The Transactions module contains respective controllers and models similar to the User model.
The commands 'pay' and 'feed' are those having to do with retrieving or adding transactions
which is why they are the main methods in the TransActionsController. The TransactionsController
process arguments sent by the commands and heavily makes use of the app Database script.

The Transaction model is very simple and has the actor, target, amount, and note as properties.
These properties are needed to retrieve feeds and are the bare essentials for a transaction
which is why I designed it this way.

The controller processes arguments and raises exceptions for all cases in which input
is invalid. Feeds are retrieved by doing a lookup on the database and printing out
all transactions associated to the user passed in. Part of the reason why I abstracted
transactions is to make transactions more flexible and extensible. For the purpose
of this project, transactions are simple objects but, feeds are generated based on transactions
rather than simply storing feeds as strings on the User object.



### minivenmo.Database
##### Scripts:
*Database.py

The database for the project is a hash table/dictionary configured to store all of the objects/models
used by the app. I used a dictionary to emulate the key/value storage that a database provides.
I emulated the one to many relationship for users and transactions by having the value as an array of
transactions associated to a username key. I noticed that the app didn't require a two way relationship
between credit cards and users, so I designed the dictionary to only hold a set of credit card numbers.
I chose a set due to its awesome property of only storing unique values. User objects are stored as a key
value relationship as well with the key being the username, and the value being the user object.

The dictionary storage acts as a lookup layer as well as a write layer. All add/lookup methods
of the database are called within the User and Transaction controllers as they would
be in the event an actual database was used.

The database class uses the add/lookup methods to insert into the database and retrieve information

I designed the module to also set set a global property *db* that acts as a Database class instance
across all modules. This was necessary to keep the database in a global namespace during app context.

### minivenmo.MiniVenmo

##### Scripts:
*MiniVenmo.py

This script acts essentially as the routing part of the application and deals
with input/fileprocessing. Based on the input, the script directs/routes to the
UsersController/TransactionsController and errors out if the input is bad. I built it
this way in order to keep the logic separate from the controllers and to keep things
as small as possible.
