# SQLAlchemy with Python

This project demonstrates how to use SQLAlchemy with Python to create and manipulate a SQLite database. It includes examples of creating tables, inserting data, and using foreign keys to establish relationships between tables.

## Requirements

- Python 3.x
- SQLAlchemy

## Installation

1. Create a virtual environment and activate it:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    ```

2. Install the required packages:
    ```sh
    pip install sqlalchemy
    ```

## Usage

1. Run the `MyClass.py` script to create the database and insert data:
    ```sh
    python MyClass.py
    ```

2. The script will create a SQLite database file named `mydb.db` and populate it with data.

## Code Overview

### Key Sections

1. **Imports and Base Class Definition**
    - Import necessary modules from SQLAlchemy.
    - Define a base class using `declarative_base()`.

2. **Person Class Definition**
    - Define the `Person` class with attributes: `id`, `firstname`, `lastname`, `age`, and `gender`.
    - Implement the `__init__` and `__repr__` methods.

3. **Thing Class Definition**
    - Define the `Thing` class with attributes: `t_id`, `description`, and `o_id` (foreign key referencing `Person.id`).
    - Implement the `__init__` and `__repr__` methods.

4. **Database Setup and Data Insertion**
    - Create an engine and bind it to the base class metadata.
    - Create a session to interact with the database.
    - Insert data into the `Person` and `Thing` tables.

5. **Querying Data**
    - Query the database to display persons who own a thing.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)