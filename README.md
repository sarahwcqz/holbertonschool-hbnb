# Hbnb

## Overview
1. [Presentation of the project](#presentation-of-the-project)
2. The 4 stages of the project
3. Presentation of the team

## Presentation of the project
HBnB is a full-stack project designed to progressively build a complete clone of the Airbnb platform. Developed through four successive stages, it guides students from the fundamentals of backend architecture to the implementation of a fully dynamic web application. The project emphasizes clean design, modularity, scalability, and collaboration.

At its core, HBnB introduces key concepts such as data modeling, storage engines, API design, templating, front-end interaction. Each stage adds new layers of functionality, allowing the project to evolve from a simple command-line interface into a fully integrated web platform.

### The users of the website
There are two main kinds of users to this service:

- **People looking for a holiday accommodation**  
  They can register, find a list of accommodations based on certain criteria (price, location…), rent it, and leave reviews about the accommodation they rented.

- **People providing accommodation**  
  They also need to register, and can create, update, and delete a page for their accommodation, select the amenities it contains, display the price, location, and availability.


## The 4 stages of the project

### 1 - UML
As part of the HBnB project, a dedicated [UML section](!https://github.com/sarahwcqz/holbertonschool-hbnb/tree/develop/part1) is introduced to formalize the structure and behavior of the application. This stage emphasizes the importance of visual modeling as a tool for understanding, designing, and communicating complex systems.

The UML work centers on creating diagrams that describe the core elements of HBnB, including models, relationships, interactions, and data flow. These diagrams provide a clear, technology-agnostic blueprint of the platform before any implementation takes place, ensuring consistency across all stages of development.

The primary goals of this section are to:
- Define the domain model and its relationships through class diagrams.
- Illustrate how components interact using sequence diagrams.
- Map out the system’s high-level structure with component or package diagrams.
- Support maintainability, collaboration, and architectural clarity throughout the project.

This UML foundation serves as the conceptual backbone of the HBnB platform, guiding both backend and frontend implementation in a coherent and structured way.

### 2 - BL and API
The [Business Logic and API phase](!https://github.com/sarahwcqz/holbertonschool-hbnb/tree/develop/part2) introduces the core functional layer that drives the HBnB application. This stage focuses on separating responsibilities between data handling, application rules, and external communication, ensuring a clean and maintainable architecture.

The business logic defines how the application behaves: how objects are validated, created, updated, retrieved, and linked together. It establishes consistent rules across the system, independent of storage or interface concerns. This separation enables better scalability, easier testing, and clearer reasoning about the system’s behavior.

Building on top of this logic, the RESTful API exposes the platform’s functionality to external clients. Through well-structured endpoints, it allows the front-end and other services to interact with the underlying models in a predictable and standardized way. The API handles request parsing, validation, error management, and serialization of data into JSON.

The main objectives of this stage are to:
- Implement robust application rules within a dedicated business layer.
- Provide a clean, stateless REST API following standard HTTP conventions.
- Ensure consistent data serialization and validation across all endpoints.
- Enable integration with future front-end components and external services.

Together, the business logic and API form the operational core of HBnB, enabling controlled access to data and supporting all subsequent layers of the project.

### 3 - Auth and DB
The [Authentication and Database stage](!https://github.com/sarahwcqz/holbertonschool-hbnb/tree/develop/part3) introduces the foundations of secure access control and persistent data management within the HBnB platform. This phase strengthens the application by ensuring that users are properly identified, and that data is stored, retrieved, and structured reliably.

The authentication layer focuses on validating user identity and managing access to protected resources. It introduces mechanisms such as credential verification, session or token-based authentication, and permission checks. This ensures that only authorized users can perform sensitive operations, adding a critical security layer to the platform.

The database component provides durable storage for all application data. It defines the schema, relationships, indexing strategies, and queries used to manage HBnB’s core models. This stage emphasizes consistency between the data model and the business logic, ensuring that information is stored efficiently and accessed safely. Proper data validation, referential integrity, and transactional behavior are central to this part of the work.

The main goals of this section are to:
- Implement secure user authentication and access control.
- Establish a reliable and scalable database layer aligned with the project’s data model.
- Ensure data integrity, validation, and efficient querying.
- Provide a solid foundation for all higher-level features of the HBnB platform.

Together, authentication and database management form the structural backbone of the application, enabling secure user interactions and stable long-term data persistence.


### 4 - Simple Web Client
The Simple Web Client phase introduces the first front-end layer of the HBnB platform. Its purpose is to provide a lightweight interface that interacts directly with the API, allowing users to visualize and manipulate data through a browser.

This stage focuses on building a minimal, functional client capable of fetching, displaying, and updating information in real time. It emphasizes the fundamentals of front-end integration: structured HTML, dynamic rendering with JavaScript, and clean communication with the REST API. The client remains intentionally simple, prioritizing clarity, responsiveness, and correctness over visual complexity.

The main goals of this section are to:
- Create a basic but functional web interface connected to the API.
- Implement dynamic content loading using JavaScript and asynchronous requests.
- Display core HBnB data such as places, users, and relationships.
- Demonstrate end-to-end communication between the front-end and the server.

This simple client serves as the first visible layer of the HBnB application, laying the groundwork for more advanced user interfaces and richer front-end functionality.

This stage is the only one carried out independently. All aesthetic choices are therefore personal, giving us complete freedom to express ourselves in any way we choose.

## Presentation of the team

- [Mustapha Chermat](!https://github.com/stafach)

- [Sarah Wacquiez](!https://github.com/sarahwcqz)