# Project Title

Contact Manager Application

## Description

Web based contact manager application using python flask web framework.

## Getting Started

### Dependencies


* The latest version of Python. Flask supports Python 3.6 and newer.
* These distributions will be installed automatically when installing Flask.

    * Werkzeug implements WSGI, the standard Python interface between applications and servers.

    * Jinja is a template language that renders the pages your application serves.

    * MarkupSafe comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.

    * ItsDangerous securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.

    * Click is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.

### Installing

* Download the source code
* Download the Xampp Application [click here](https://www.apachefriends.org/download.html)
* Download the Python [click here](https://www.python.org/downloads/)
* No modifications needed to be made to files/folders

### Executing program

* Before going to run the application make sure current working directory in cmd is pointing to the application folder i.e, /contact app.

* __STEP 1 :__ Installing required packages.
```
pip install -r requirements.txt
```

* __STEP 2 :__ Start the application
```
main.py
```

* __STEP 3 :__ Start your Xampp application. Start Apache and MySQl Server.

* __STEP 4 :__ import the contactdb.sql into the xampp.

* __STEP 5 :__ Open this url in web browser.
```
http://127.0.0.1:5000/
```


## Screen Shots

- Register Page
![picture alt](./static/screenshots/register.PNG)
   

- Login Page
![picture alt](./static/screenshots/login.PNG)

- Dashboard Page
![picture alt](./static/screenshots/Capture.PNG)

## Authors

[@Thammineni Pushyamitra](https://www.linkedin.com/in/thammineni-pushyamitra-5550821b9/)



## Acknowledgments

* [flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Julian Nash](https://pythonise.com/tags/flask)
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
