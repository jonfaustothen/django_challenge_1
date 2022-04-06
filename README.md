# Hello World App Using Django Framework
In this project, I create a website (on a local server) in which the user can enter their name after "hello/" to appear as text on the page.  I create an app with the django framework that receives any name from the user.  Django is a Python web framework which makes creating websites simple as it solves a lof of the web development. 

## Requirements
This projects requires that you have [Python3](https://www.python.org/downloads/) as well as [Django](https://www.djangoproject.com/download/).

## Usage
*To clone a copy of this project using https, run the following command in the command line:*
`$ git clone https://github.com/jonfaustothen/django_challenge_1.git`

*Create a Python virtual environment and activate it in your local project:*
`$ cd <your_local_project_directory_name>`
`$ python3 -m venv venv`
On Mac OS: `$ venv/bin/activate`
On PC: `$ venv\Scripts\activate.ps1`

*Install the packages from requirements.txt:*
`$ pip install -r requirements.txt`

*In the hellosite/ directory run the following command to start the server: *
`$ cd hellosite`
`$ python3 manage.py runserver`

### Try some more examples and see what happens
-   `localhost:8000/hello/jon`
-   `localhost:8000/hello/adam`
-   `localhost:8000/hello/cindy`
-   `localhost:8000/hello/goodbye/django`

## History / Credits
There are a multitude of resources online to write this script, but I mostly referred to lessons taught by Columbia University's JTC Program's staff.  Feel free to use this code to develop your own program!
