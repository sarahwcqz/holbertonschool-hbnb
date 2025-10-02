# HBnB Project

## Presentation of the following document
- Presentation of the project  
- Technical documentation  
    - Package diagram  
    - Class Diagram  
    - Sequence Diagram  

---

## Presentation of the project
This is the second trimester of Holberton School’s project. The purpose is to put what we have learned so far, and what we are still learning into practice to be able to recreate an Airbnb clone.

### The purpose of the website
There are two main kinds of users to this service:

- **People looking for a holiday accommodation**  
  They can register, find a list of accommodations based on certain criteria (price, location…), rent it, and leave reviews about the accommodation they rented.

- **People providing accommodation**  
  They also need to register, and can create, update, and delete a page for their accommodation, select the amenities it contains, display the price, location, and availability.

This project helps put into practice key concepts of software engineering such as OOP, Databases, API services, and front-end integration.

### The team
- Mustapha Chermat  
- Sarah Wacquiez  

---

## Technical documentation
The UML diagrams included in this documentation represent the conceptual and structural design of HBnB. They clarify the relationships between entities and layers, serving as a blueprint for implementation.

### Diagrams overview
- **Package Diagram**: High-level organization of the system into modules or subsystems.  
- **Class Diagram**: Core entities, their attributes, methods, and relationships.  
- **Sequence Diagram**: Dynamic flow of interactions between components during specific use cases.  

---

## High-level Package Diagram
### Purpose
The diagram illustrates the layered architecture of the application. It shows how responsibilities are divided into three main layers—Presentation, Business Logic, and Persistence—to promote modularity, separation of concerns, and maintainability.

### Key Components

#### Presentation Layer (Interface) - Front-end
Where the user interacts with the services. Whenever the client requests a service, the interface communicates it to the business logic layer.

#### Business Logic Layer - Back-end
Contains the core logic of the web application.  
- **Logic part**: Functions on which the functioning relies.  
- **Model part**: Classes and objects.  

#### Persistence Layer - Back-end
Where all data is stored (the database).  

---

## Class Diagram
### Purpose of the Diagram
Defines the core domain model of the application. Shows the main entities (User, Place, Review, Amenity), their attributes, methods, and the relationships between them. Purpose: clarify the structure of the application’s business objects and their interactions.

### Key Components

#### User
- **Attributes**  
  id, first name, last name, email, password, admin (y/n), creation date, update date  
- **Methods**  
  register, update profile, delete  

#### Place
- **Attributes**  
  id, title, description, price, latitude, longitude, creation date, update date  
- **Methods**  
  create, update, delete, list  

#### Review
- **Attributes**  
  id, rating, comment, creation date, update date  
- **Methods**  
  create, update, delete, list_by_place()  

#### Amenity
- **Attributes**  
  id, name, description, creation date, update date  
- **Methods**  
  create, update, delete, list  

### Design Decisions and Rationale
- Each class corresponds to a core domain entity.  
- Each class defines its own operations (create, update, delete, list).  
- Relation types:  
  - Place --* User: A place cannot exist without its owner (composition).  
  - Place --o Amenity: Amenities can exist independently but may be associated with places.  
  - Review --* Place: Reviews are tightly bound to places, so they cannot exist without them.  
  - User --o Review: A user can leave several reviews, but if the user deletes their profile, the reviews remain.  

---

## Sequence Diagrams
### Purpose of the Diagrams
Show what happens when a user makes a request. Illustrate how the 3 layers interact with one another when a service is requested. Help visualize how the different components of the system interact to fulfill specific use cases, showing the step-by-step process of handling API requests.

### Example client services
1. **User Registration**: A user signs up for a new account.  
2. **Place Creation**: A user creates a new place listing.  
3. **Review Submission**: A user submits a review for a place.  
4. **Fetching a List of Places**: A user requests a list of places based on certain criteria.  

#### User registration
Process of a new user signing up.  

#### Place creation
User wants to create a new place.  
- The API gets the list of amenities from DB and displays it.  
- User enters all details of the new place.  
- API saves it in DB.  
- DB confirms creation.  

#### Review submission
User submits a review for a place.  
- API sends review to DB.  
- DB stores it and confirms success.  

#### Fetching a list of places
User requests existing places based on criteria.  
- API queries DB with the criteria.  
- DB returns the list of matching places.  
