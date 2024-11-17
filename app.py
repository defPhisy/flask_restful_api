from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app=app, key_func=get_remote_address)

books = [
    {
        "id": i + 1,
        "title": f"Book {i + 1}",
        "author": f"Author {i + 1}",
    }
    for i in range(100)
]


@app.route("/api/books", methods=["GET", "POST"])
@limiter.limit("30/minute")
def handle_books():
    # POST REQUEST: "{'title': '1984', 'author': 'George Orwell'}"
    if request.method == "POST":
        new_book = request.get_json()

        # validate book
        if not validate_book_data(new_book):
            return jsonify({"error": "Invalid book data"}), 400

        # add new book
        new_book["id"] = max(book["id"] for book in books) + 1
        books.append(new_book)
        return jsonify(new_book), 201

    # QUERY PARAMETER: "?author=xxxx" -- filter books with author
    author = request.args.get("author")
    if author:
        filtered_books = [
            book for book in books if book.get("author") == author
        ]
        return jsonify(filtered_books)

    # QUERY PARAMETER: "?page=2&limit=5" -- pagination
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    if page and limit:
        start_index = (page - 1) * limit
        end_index = start_index + limit
        paginated_books = books[start_index:end_index]
        return jsonify(paginated_books)

    # POST REQUEST: "{'title': '1984', 'author': 'George Orwell'}"
    if request.method == "POST":
        new_book = request.get_json()

        # validate book
        if not validate_book_data(new_book):
            return jsonify({"error": "Invalid book data"}), 400

        # add new book
        new_book["id"] = max(book["id"] for book in books) + 1
        books.append(new_book)
        return jsonify(new_book), 201

    # ELSE: return all books
    return jsonify(books)


@app.route("/api/books/<int:id>", methods=["PUT"])
@limiter.limit("30/minute")
def handle_book(id):
    book = find_book(id)
    if book is None:
        return "", 404

    new_data = request.get_json()
    if not has_valid_keys(new_data):
        return jsonify({"error": "Invalid book data"}), 400

    book.update(new_data)

    return jsonify(book)


@app.route("/api/books/<int:id>", methods=["DELETE"])
@limiter.limit("30/minute")
def delete_book(id):
    book = find_book(id)
    if book is None:
        return jsonify({"error": f"Book with ID:{id} not Found"}), 404

    books.remove(book)

    return jsonify(book)


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404


@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({"error": "Method Not Allowed"}), 405


@app.errorhandler(429)
def request_error(error):
    return jsonify(error="Too Many Requests"), 429


def find_book(id):
    for book in books:
        if book["id"] == id:
            return book
    return None


def validate_book_data(data):
    return "title" in data and "author" in data


def has_valid_keys(data):
    for key in data:
        if key not in ("title", "author"):
            return False
    return True


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
