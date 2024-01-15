# FastAPI Pokedex API

FastAPI Pokedex API project – a small yet powerful Pokedex implementation. This project serves as a testing ground to explore FastAPI's capabilities and gain hands-on experience in building APIs.


## Features and Highlights

1. Database Configuration
   - The project is configured to use PostgreSQL as its database. The config.py file contains the necessary settings, including the database URL, SQLAlchemy engine, and session management.

  
2. SQLAlchemy Models
   - The models.py file defines the SQLAlchemy model for the Pokedex, including fields such as ID, Pokedex Number, Name, Description, Types, Abilities, and Location.

  
3. API Routes
   - Explore various API routes to retrieve Pokemon information:

      * Get All Pokemon: /
      * Get Pokemon by Name: /pokemon-name/{pokemon_name}
      * Get Pokemon by Pokedex Number: /pokedex-index/{pokemon_num}
      * Get Pokemon by Ability: /ability/{ability}
      * Create Pokemon: POST /create-pokemon/
      * Delete Pokemon by Name: DELETE /delete/{pokemon_name}
      * Update Pokemon: PUT /update-pokemon


4. Database Operations
   - The API supports basic CRUD operations (Create, Read, Update, Delete) for managing Pokemon data in the Pokedex.

  
5. Data Validation with Pydantic
   - The schemas.py file utilizes Pydantic to define data models for input validation. This ensures data integrity and consistency in API requests.
  

## Observations

While the project successfully demonstrates FastAPI functionalities, there's an opportunity for improvement in the logic of each view. Exploring alternative approaches to create and structure the views could enhance the overall project design and maintainability
