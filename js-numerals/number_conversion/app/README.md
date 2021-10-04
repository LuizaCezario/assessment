# Calculate Route App

The Calculate Route App is an app designed to calculate the distance from Moscow Ring Roud to a given adress.



# Installing
Install and update using pip:

pip install -U Flask
pip install geopy 
pip install nose

# Run the app
Go to the folder of the project "app", open a terminal and type:

python3 -m flask run

Go to http://127.0.0.1:5000/ in your navigator and use the app.

# Run the tests
Go to the folder of the project "app", open a terminal and type:

python3 -m unittest tests.py

It's necessary to run the app before of running the tests. Te html page has some validations,
the test for those cases were not made.