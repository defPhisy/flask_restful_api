# Flask Book API

A simple Flask-based REST API for managing a collection of books. It supports creating, reading, updating, and deleting books, with additional features like filtering by author and paginated results.

## Features

- **GET /api/books**: Retrieve all books with optional filtering by author and pagination.
- **POST /api/books**: Add a new book (requires `title` and `author`).
- **PUT /api/books/\<id>**: Update a book's details by its ID.
- **DELETE /api/books/\<id>**: Delete a book by its ID.

## Endpoints

### 1. Get All Books

- **Endpoint**: `GET /api/books`
- **Query Parameters**:
  - `author` (optional): Filter books by author name.
  - `page` (optional): Page number for pagination (default is 1).
  - `limit` (optional): Number of books per page (default is 10).
- **Example Request**:
  ```
  GET /api/books?page=2&limit=2
  ```
- **Example Response**:
  ```json
  [
    {
      "id": 3,
      "title": "Book 3",
      "author": "Author 3"
    },
    {
      "id": 4,
      "title": "Book 4",
      "author": "Author 4"
    }
  ]
  ```

### 2. Add a New Book

- **Endpoint**: `POST /api/books`
- **Request Body (JSON)**:
  ```json
  {
    "title": "1984",
    "author": "George Orwell"
  }
  ```
- **Response**:
  - **201 Created**
  - Example Response:
    ```json
    {
      "id": 101,
      "title": "1984",
      "author": "George Orwell"
    }
    ```

### 3. Update a Book by ID

- **Endpoint**: `PUT /api/books/<id>`
- **Request Body (JSON)**:
  ```json
  {
    "title": "Animal Farm",
    "author": "George Orwell"
  }
  ```
- **Example Request**:
  ```
  PUT /api/books/1
  ```
- **Example Response**:
  ```json
  {
    "id": 1,
    "title": "Animal Farm",
    "author": "George Orwell"
  }
  ```

### 4. Delete a Book by ID

- **Endpoint**: `DELETE /api/books/<id>`
- **Example Request**:
  ```
  DELETE /api/books/2
  ```
- **Example Response**:
  ```json
  {
    "id": 2,
    "title": "Book 2",
    "author": "Author 2"
  }
  ```

### Error Responses

- **404 Not Found**: When a book or endpoint is not found.
  ```json
  {
    "error": "Not Found"
  }
  ```
- **405 Method Not Allowed**: When an unsupported HTTP method is used.
  ```json
  {
    "error": "Method Not Allowed"
  }
  ```
- **400 Bad Request**: When the provided data is invalid.
  ```json
  {
    "error": "Invalid book data"
  }
  ```

## How to Run the Application

### Prerequisites

- Python 3.x installed on your machine.
- `pip` package manager.

### Installation Steps

1. **Clone the repository**:

   ```bash
   https://github.com/defPhisy/flask_restful_api.git
   cd flask_book_api
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**:

   ```bash
   python app.py
   ```

5. **Access the API**:
   - Open your browser or API client (like Postman) and go to:
     ```
     http://localhost:5001/api/books
     ```

## Example Books Data

When the server starts, it preloads 100 sample books in the following format:

```json
[
  {
    "id": 1,
    "title": "Book 1",
    "author": "Author 1"
  },
  {
    "id": 2,
    "title": "Book 2",
    "author": "Author 2"
  },
  {
    "id": 3,
    "title": "Book 3",
    "author": "Author 3"
  }
]
```

## License

This project is licensed under the [MIT License]().

---
