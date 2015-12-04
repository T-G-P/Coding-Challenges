# python-challenge

Your goal is to build a simple “Address Book” web app.  The backend is  Python/Flask/SQLAlchemy. Frontend is plain HTML.  

An Address Book contains all your contacts and all the addresses for each contact. Your goal is to implement everything in the wireframes in the attached PDF file.

### Required Functionality
- Search for contacts by name
- View an individual contact and addresses
- Add a new address to a contact
- Edit an existing address belonging to a contact

### Functionality you DO NOT need to build
- Deleting addresses
- Creating new contacts
- Editing contact information

To get started, unzip the template project and run “make init”.  You can run the unit test suite by running “make test” and you can launch the server by running “make runserver”.  When the server is running, you should be able to view your project at http://localhost:5000.

### Project Structure
- app
-- templates (you will edit and create templates in this folder)
--- index.html
-- static (put static assets here)
-- __init__.py (most of your code will go here!)
- Makefile (defines commands to initialize project, run your tests, and run the server)
- run.py (helper to run server -- no need to edit)
- config.py (project configuration -- no need to edit)
- tests.py (unit tests live here!)
- Junior Python Challenge Wireframes.pdf (wireframes for the completed project)

### Task 1: Define an Address model
We provide a (very simple) Contact model that represents one contact in your address book. It is up to you to define an Address model that represents one address for a contact.  

### Task 2: Implement Search
Complete the “search” method in app/__init__.py and build the “search.html” template.  Write a test to verify that the search method works as expected.  When this is complete you should be able to search for contacts by going to http://localhost:5000 and searching for a name.  Partial matches for the name should be included and search should not be case sensitive.  For example, searching for “hillary” would be expected to return the record for “Hillary Clinton.”

### Task 3: Implement Show Contact
Complete the “show_contact” method in app/__init__.py and build the “show_contact.html” template.  Link the search results to the matching show_contact routes. Write a test to verify that the show_contact method works as expected.  When this is complete you should be able to go to http://localhost:5000, search for a contact, and view the contact and addresses associated with that contact. 

### Task 4: Implement adding and editing Addresses
Write any needed routes and view templates to implement functionality to add and edit addresses for a selected contact.  Write tests to test the views. When this is complete you should have all the required functionality!

### Completion
- Ensure all functionality works and matches wireframes
- Ensure you have test coverage for all your code
- If time permits, make sure code is well factored and adheres to PEP8 (http://legacy.python.org/dev/peps/pep-0008/)
- Zip your challenge up (you may want to delete the “env” folder to make the file smaller) and email back to me.
