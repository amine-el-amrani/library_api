# Library API

The Library API is a RESTful service built to manage books and authors in a library. It allows users to create, view, update, and delete books and authors. With an easy-to-use Swagger UI documentation, users can interact with the API directly from their browser.

## Technologies utilisées
- Flask: Web framework for Python.
- Flask-RESTX: Simplifies building REST APIs and adds Swagger UI.
- Flask-SQLAlchemy: ORM for managing SQLite database interactions.
- Flask-Marshmallow and Marshmallow: For validating and serializing input and output data.
- SQLite: Embedded SQL database for storing books and authors.

## Installation Instructions

1. Clone this repository: :
```bash
    git clone https://github.com/amine-el-amrani/library_api.git
    cd library_api
```

2. Install dependencies:
```bash
    poetry install
```

3. Start the Flask application:
```bash
    poetry run python app.py
```

## API Documentation
The Library API provides Swagger-based interactive documentation available at:

- Swagger UI:  ``` bash vhttp://127.0.0.1:5000/docs ```