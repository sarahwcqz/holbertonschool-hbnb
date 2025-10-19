# Hbnb - Part2 : BL and API

## Overview
1. [Intro](#intro)
2. [Setting up the project](#setting-up-the-project)
3. [Structure](#structure)
4. [BL explanation](#bl-explanation)
    - [Classes](#classes)
    - [Repository](#repository)
    - [Facade](#facade)
    - [Endpoints](#api---endpoints)
5. [Tests examples](#tests-examples)


## Intro
This section is dedicated to the second part[^1] of the Hbnb Project of [Holberton School](https://www.holbertonschool.fr/?utm_source=google&utm_medium=cpc&utm_campaign=MV%20-%20Notori%C3%A9t%C3%A9&gad_source=1&gad_campaignid=22385717730&gbraid=0AAAAABYPkmm8wuIv2e2IzPkrS8yXrdgCP&gclid=CjwKCAjwxrLHBhA2EiwAu9EdM7bq0u_FwEIb7Ui4iyM4Obn-jqZfVNPtfYb6Y6FDopVu2O5zaI0Q5BoCSk4QAvD_BwE)


**The objectives of this part of the project are the following** :
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
├── tests/
├── images/
```
- At the root of the folder you can find the following files :
    - **run.py** 
    : the files that allows you to run the Flask appplication ([see part 4 of this section](#setting-up-the-project))
    - **config.py**
    : def 
    - **requirements.txt** 
    : The file containing all packages needed for the project ([see part 3 of this section](#setting-up-the-project))
    - This marvellous **README.md**
- The tests directory contains all our unittests to make sure our endpoints comply with the instructions
- The images directory contains screenshots of our tests on POSTMAN, you'll find them in the Test examples section
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
### Classes
#### BaseModel
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

#### User
| Attribute   | Type      | Description                                                   |
|--------------|-----------|---------------------------------------------------------------|
| id           | String    | Unique identifier for each user                               |
| first_name   | String    | The first name of the user (**Required**, max 50 chars)       |
| last_name    | String    | The last name of the user (**Required**, max 50 chars)        |
| email        | String    | Unique email address (**Required**, must follow email format) |
| is_admin     | Boolean   | Indicates if user has admin privileges (Defaults to `False`)  |
| created_at   | DateTime  | Timestamp when the user is created                            |
| updated_at   | DateTime  | Timestamp when the user is last updated                       |


#### Place
| Attribute   | Type      | Description                                                      |
|--------------|-----------|------------------------------------------------------------------|
| id           | String    | Unique identifier for each place                                 |
| title        | String    | The title of the place (max 100 chars)             |
| description  | String    | Detailed description of the place (Optional)                 |
| price        | Float     | Price per night (Must be a positive value)                   |
| latitude     | Float     | Latitude coordinate (range: -90.0 to 90.0)                       |
| longitude    | Float     | Longitude coordinate (range: -180.0 to 180.0)                    |
| owner        | User      | User instance who owns the place |
| created_at   | DateTime  | Timestamp when the place is created                              |
| updated_at   | DateTime  | Timestamp when the place is last updated                         |


#### Amenity
| Attribute  | Type      | Description                                                   |
|-------------|-----------|---------------------------------------------------------------|
| id          | String    | Unique identifier for each amenity                            |
| name        | String    | The name of the amenity (max 50 chars) |
| created_at  | DateTime  | Timestamp when the amenity is created                         |
| updated_at  | DateTime  | Timestamp when the amenity is last updated                    |


#### Review
| Attribute  | Type      | Description                                                                 |
|-------------|-----------|-----------------------------------------------------------------------------|
| id          | String    | Unique identifier for each review                                           |
| text        | String    | The content of the review                                         |
| rating      | Integer   | Rating given to the place (Must be between 1 and 5)                         |
| place       | Place     | Place instance being reviewed                |
| user        | User      | User instance who wrote the review          |
| created_at  | DateTime  | Timestamp when the review is created                                        |
| updated_at  | DateTime  | Timestamp when the review is last updated                                   |


### Repository
This is a temporary solution to replace the database that will be implemented in the next part of the project. It contains :
- UserRepository
- PlaceRepository
- AmenityRepository
- ReviewRepository

### Facade
The role of the Facade is to redirect all actions, it acts as a receptionnist in a hotel, distributing the communication between the client and the business layer.
It handles to following methods:
| Method | Description |
|--------|-------------|
| **User Methods** | |
| create_user(user_data) | Creates a new user with the provided data |
| get_all() | Retrieves all users |
| get_user(user_id) | Retrieves a user by their unique ID |
| get_user_by_email(email) | Finds a user using their email address |
| update_user(user_id, user_data) | Updates an existing user by ID |
| **Amenity Methods** | |
| create_amenity(amenity_data) | Creates a new amenity |
| get_amenity(amenity_id) | Retrieves an amenity by ID |
| get_all_amenities() | Retrieves all amenities |
| update_amenity(amenity_id, amenity_data) | Updates an existing amenity by ID |
| **Place Methods** | |
| create_place(place_data) | Creates a new place |
| get_place(place_id) | Retrieves a place by ID |
| get_all_places() | Retrieves all places |
| update_place(place_id, place_data) | Updates an existing place by ID |
| **Review Methods** | |
| create_review(review_data) | Creates a new review for a place |
| get_review(review_id) | Retrieves a review by ID |
| get_all_reviews() | Retrieves all reviews |
| get_reviews_by_place(place_id) | Retrieves all reviews for a specific place |
| update_review(review_id, review_data) | Updates an existing review by ID |
| delete_review(review_id) | Deletes a review by ID |


### API - endpoints
Here you will find the list of all possible operations.

**Users operations**
| Endpoint         | Method | Description |
|-----------------|--------|-------------|
| /users/         | POST   | Register a new user. Validates input and checks email uniqueness. Returns the created user with ID. |
| /users/         | GET    | Retrieve a list of all users with their details (id, first_name, last_name, email). |
| /users/<user_id> | GET    | Retrieve details of a specific user by their unique ID. Returns 404 if user not found. |
| /users/<user_id> | PUT    | Update an existing user's information (first_name, last_name, email). Validates input. Returns 404 if user not found. |

**Places operations**
| Endpoint         | Method | Description |
|-----------------|--------|-------------|
| /places/        | POST   | Register a new place. Validates input and creates a new place. Returns the created place with ID and owner_id. |
| /places/        | GET    | Retrieve a list of all places with basic details (id, title, latitude, longitude). |
| /places/<place_id> | GET    | Retrieve full details of a specific place by its ID, including owner info and associated amenities. Returns 404 if place not found. |
| /places/<place_id> | PUT    | Update an existing place's information (title, description, price). Validates input. Returns 404 if place not found_
| /places/<place_id>/reviews | GET    | Retrieve all reviews for a specific place. Returns 404 if the place is not found. |

**Amenities operations**
| Endpoint            | Method | Description |
|--------------------|--------|-------------|
| /amenities/         | POST   | Register a new amenity. Validates input and creates a new amenity. Returns the created amenity with ID. |
| /amenities/         | GET    | Retrieve a list of all amenities with their IDs and names. |
| /amenities/<amenity_id> | GET    | Retrieve details of a specific amenity by its ID. Returns 404 if amenity not found. |
| /amenities/<amenity_id> | PUT    | Update an existing amenity's information (name). Validates input. Returns 404 if amenity not found. |

**Reviews operations**
| Endpoint                        | Method | Description |
|--------------------------------|--------|-------------|
| /reviews/                       | POST   | Register a new review. Validates input and adds the review to the associated place. Returns the created review with ID. |
| /reviews/                       | GET    | Retrieve a list of all reviews with basic details (id, text, rating). |
| /reviews/<review_id>            | GET    | Retrieve details of a specific review by its ID. Returns 404 if review not found. |
| /reviews/<review_id>            | PUT    | Update an existing review's information (text, rating). Validates input. Returns 404 if review not found. |
| /reviews/<review_id>            | DELETE | Delete a review by its ID. Returns 404 if review not found. |





## Test examples
To test our APIs we used POSTMAN, and we will show you some of our tests to explain the expected outcomes.
Note that you can do the same tests using cURL by juste taping
```bash
curl -X POST [the URL that you see on the POSTMAN screenshots] \
     -H "Content-Type: application/json" \
     -d '{
           [the JSON body you will see on the POSTMAN screenshots]
         }'
```
The output should be similar to the one shown in examples.
Note also that for all examples, if you use POSTMAN as shown bellow, you'll need to make sure that in the header section you add as key-value : Content-Type: application/json

Let’s say you own a place, but making ends meet is difficult. You just heard about a new website that allows you to rent your place and earn some extra money, so you decide to try it out.
First you'll need to register as a user.

*When a client registers as a new user, this is what it is supposed to look like:*
![user - POST](/part2/images/1%20-%20USER%20creation.png)

Now that you have created your account as a new user, you want to publish your place for rent.
You'll need to create a new place, belonging to you.

*When a new place is created, it looks like this:*
![place - POST](/part2/images/4%20-%20PLACE%20creation.png)

You can of course always change the attributes of your place, for example if times are getting harder you can always increase the price of your place.

*Updating a place would look like this:*
![place - PUT](/part2/images/3%20-%20PLACE%20update.png)
*Here the URL should be api/v1/places/<place_id>*

It's always good to take a look at the reviews before booking a place (just in case), with Hbnb you can do that by retrieving the list of reviews left to a specific place.

*Retreiving the reviews of a specific place looks like this:*
![review - GET](/part2/images/5-%20REVIEWS%20list.png)
*Here the URL should be api/v1/places/<place_id>/reviews*
Here we can see that someone left a bad review, it's quite a shame. It’s even sadder knowing that the user got a bit carried away when posting their review, only to realize afterward that their goods were safely in their suitcase and hadn’t actually been stolen. Fortunately, they have the option to delete their review.

*Deleting a review looks like this:*
![review - DEL](/part2/images/5%20-%20REVIEW%20delete.png)
*Here the URL should be api/v1/reviews/<review_id>*

Since the ids change each time you run the server, you might find unmathcing user's or place's id in our examples.


We also used unittests to tests our endpoints, you can find them in the `tests` directory at the root of the folder.
Here are all the cases that we tested in those files:

- **USER :**

| Post | Put | Get |
|------------|------------|------------|
| valid input | valid input | get a list of user |
| empty name | id not found | retrieve a user's detail with valid id |
| empty surname | empty name | retrieve a user's detail with invalid id |
| name > 50 | surname > 50 |  |
| surname > 50 | invalid mail format |  |
| invalid email format |  |  |


- **PLACE :**

| Post | Put | Get |
|------------|------------|------------|
| valid input | valid input | get a list of existing places |
| empty title | partial update | get a place's details with valid id |
| price < 0 | invalid title | get a place's details with invalid id |
| invalid latitude | place's id not found |  |
| invalid longitude |  |  |
| owner's id not found |  |  |


- **AMENITY :**

| Post | Put | Get |
|------------|------------|------------|
| valid input | valid input | get a list of all existing amenities |
| empty name | invalid  id | get an amenity with id with valid id |
| name > 50 | empty name | get an amenity with id with invalid id |
|  | name > 50 |  |


- **REVIEW :**

| Post | Put | Get | Delete |
|------------|------------|------------|------------|
| valid input | valid input | get a review with valid id | valid id |
| empty string  | empty string | get a review with invalid id | invalid id |
| rate is not integer | rate < 0 | get the reviews from a place with valid place's id | 
| rate < 0 | review's id not found | get the reviews from a place with valid place's id |
| user's id not found | 
| place's id not found | 