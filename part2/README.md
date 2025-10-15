# Hbnb - Part2 : BL and API

## Overview
1. [Intro](#intro)
2. [Setting up the project](#setting-up-the-project)
3. [Structure](#structure)
4. [BL explanation](#bl-explanation)
5. [Outro](#outro)


## Intro
This section is dedicated to the second part[^1] of the Hbnb Project of [Holberton School](https://www.holbertonschool.fr/?utm_source=google&utm_medium=cpc&utm_campaign=MV%20-%20Notori%C3%A9t%C3%A9&gad_source=1&gad_campaignid=22385717730&gbraid=0AAAAABYPkmm8wuIv2e2IzPkrS8yXrdgCP&gclid=CjwKCAjwxrLHBhA2EiwAu9EdM7bq0u_FwEIb7Ui4iyM4Obn-jqZfVNPtfYb6Y6FDopVu2O5zaI0Q5BoCSk4QAvD_BwE)


==The objectives of this part of the project are the following== :
1. Set Up the Project Structure:
    - Organize the project into a modular architecture, following best practices for Python and Flask applications.
    - Create the necessary packages for the Presentation and Business Logic layers.

2. Implement the Business Logic Layer:
    - Develop the core classes for the business logic, including User, Place, Review, and Amenity entities.
    - Implement relationships between entities and define how they interact within the application.
    - Implement the facade pattern to simplify communication between the Presentation and Business Logic layers.

3. Build RESTful API Endpoints:
    - Implement the necessary API endpoints to handle CRUD operations for Users, Places, Reviews, and Amenities.
    - Use flask-restx to define and document the API, ensuring a clear and consistent structure.
    - Implement data serialization to return extended attributes for related objects.

4. Test and Validate the API:
    - Ensure that each endpoint works correctly and handles edge cases appropriately.
    - Use tools like Postman or cURL to test the API endpoints.


[^1]: You can find more information on the first part of the project by reading this [README](https://github.com/sarahwcqz/holbertonschool-hbnb/tree/develop/part1), explaining the global architecture of the project with package, class and sequence diagrams.



## Setting up the project
Here is an explanation, step by step, of how to install the project on your environnement:
1. Start by cloning the repository => `https://github.com/sarahwcqz/holbertonschool-hbnb` and go to the directory => `holbertonschool-hbnb/part2/hbnb`
<br>
2. Set up your virtual environnement with the following command: `python3 -m venv cutiepie` (you can actually call it as you like, but why not naming it with love?).
Activate your venv with `source cutiepie/bin/activate`.
Make sure to see a `(cutiepie)` before your command prompt, this tell you that your venv is running. Once you are done with the project you can deactivate it by taping `deactivate` in the command line.
<br>
3. Run `pip install -r requirements.txt` in the command line. This will automatically install every package needed.
<br>
4. Run the application with `python3 run.py`
In your terminal you should see this
```bash
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 184-853-731
 ```



## Structure
```bash
part2/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │       ├── __init__.py
│   │       ├── users.py
│   │       ├── places.py
│   │       ├── reviews.py
│   │       ├── amenities.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── place.py
│   │   ├── review.py
│   │   ├── amenity.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── facade.py
│   ├── persistence/
│       ├── __init__.py
│       ├── repository.py
├── run.py
├── config.py
├── requirements.txt
├── README.md
```
- At the root of the folder you can find the following files :
    - **run.py** 
    : the files that allows you to run the Flask appplication ([see part 4 of this section](#setting-up-the-project))
    - **config.py**
    : def 
    - **requirements.txt** 
    : The file containing all packages needed for the project ([see part 3 of this section](#setting-up-the-project))
    - This marvellous **README.md**
- You can also find the subdirectory **app/**, containing the core application code. For better readibility it is divided into the following subdirectories:
    - **api/**
    : API endpoints (atm it only contains the v1, refeering to the first version of the project)
    - **models/**
    : business logic classes
    - **services/**
    : home of the Facade, redirection the interactions to the concerned parties
    - **persistence/**
    : in-memory repository. In the following part of the project it will be replaced by a DB version with SQL Alchemy, but for the moment it allows us to focus on the other parts of the application.

## BL explanation
### BaseModel
This is the class from which every following subclasses will inherit.
It contains the attributes that are common to every other subclasses:
- **id**
: generates a unique UUID for every object created.
- **created_at**
: sets up the creation date, for audit purpose.
- **updated_at**
: updates the updated time each time the object is updated :dizzy_face:
<br>
<br>
The BaseModel class contains two methods :
- **save**
: it updates the updated_at timestamp whenever the object is modified
- **update**
: this one updates the attributes of the object based on the provided dictionary

### User

### Place

### Amenity

### Review


## Outro

