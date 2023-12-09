from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = 'postgresql://user:password@localhost:5432/db_name'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



# Notes #

# --- Database URL ---

# This variable holds the URL for connecting to the PostgreSQL database. 
# It includes the necessary information like the database type (postgresql), 
# username (postgres), password (password), host (localhost), port (5432), 
# and database name (db_name).



# --- engine ---

# In the context of SQLAlchemy, an engine is a central component responsible for managing the connections to your database. 
# It serves as an intermediary between your Python code and the database, handling the details of how to connect, execute commands, 
# and manage connections efficiently.
# So when we pass the Database URL it parses it to understand the database dialect and stablish the connection.
# Also, basically the engine is the responsible that we can write python code as queries and translate it to the proper 
# SQL statements so the database is able to understand it



# --- sessionmaker ----

# in SQLAlchemy is responsible for creating sessions that allow you to interact with the database.

# - autocommit=False: This setting means that by default, changes made within a session are not automatically committed to the database. 
# You'll need to explicitly commit these changes.

# - autoflush=False: When autoflush is disabled, SQLAlchemy won't automatically synchronize changes made in the session with the database. 
# You'll have more control over when these changes are flushed and written to the database.


# When you want to interact with the database, you create a new session using SessionLocal:
# session = SessionLocal()

# This session acts as a workspace where you can query, add, modify, and delete objects mapped to your database tables (usually using SQLAlchemy ORM).
# Meanwhile, the engine is responsible for handling the low-level details of the database connection.
# It uses the database URL to establish and manage connections to the database, translating the commands and queries from your Python code into SQL statements that the database can understand.


# So, in summary:

# The engine manages the connections and communication with the database.

# The session (created using SessionLocal) uses the engine to execute SQL statements, manage transactions, and perform various database operations within the context of your application.



# ---- declarative_base ----

# Basically we use this in order to create a baseclass that we'll use letter to inherit in our models so i'll give us a lot of properties and setups in order
# to make our models work properly