from flask import Flask, json, jsonify, make_response, request
from config import CREDENTIALS
from lib.author import Author
from lib.book import Book
from lib.bought import Bought
from lib.cabang import Cabang
from lib.customer import Customer
from lib.publisher import Publisher
from lib.revenue import Revenue
from lib.wrote import Wrote

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    if 'key' not in request.args or request.args['key'] != CREDENTIALS["KEY"]:
        return jsonify({'message': 'Restricted access.'}), 401

    if request.method == 'GET':
        data = Book.get_books()
        res = jsonify(data)
        return res

# Endpoint to retrieve a single book by its ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    if 'key' not in request.args or request.args['key'] != CREDENTIALS["KEY"]:
        return jsonify({'message': 'Restricted access.'}), 401

    if request.method == 'GET':
        return jsonify(Book.get_book(id))

# Endpoint to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    if 'key' not in request.args or request.args['key'] != CREDENTIALS["KEY"]:
        return jsonify({'message': 'Restricted access.'}), 401

    if request.method == 'POST':
        try:
            data = request.get_json()
            req = {
                "book_number": data.get('book_number'),
                "book_name": data.get('book_name'),
                "publication_year": data.get('publication_year'),
                "pages": data.get('pages'),
                "pname": data.get('pname')
            }
            
            result = Book.add_book(req)
            
            if result == 'success':
                return jsonify({'message': 'Book added successfully.'}), 201
            else:
                print(result)
                return jsonify({'message': result}), 500
            
        except Exception as err:
            print(err)
            return jsonify({'message': f'Error: {err}'}), 500

# Endpoint to update an existing book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    if 'key' not in request.args or request.args['key'] != CREDENTIALS["KEY"]:
        return jsonify({'message': 'Restricted access.'}), 401

    if request.method == 'PUT':
        try:
            data = request.get_json()
            req = {
                "book_number": data.get('book_number'),
                "book_name": data.get('book_name'),
                "publication_year": data.get('publication_year'),
                "pages": data.get('pages'),
                "pname": data.get('pname')
            }
            
            result = Book.update_book(id, req)
            
            if result == 'success':
                return jsonify({'message': 'Book updated successfully.'}), 200
            else:
                print(result)
                return jsonify({'message': result}), 500
            
            
        except Exception as err:
            print(err)
            return jsonify({'message': f'Error: {err}'}), 500

# Endpoint to delete a book by its ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    if 'key' not in request.args or request.args['key'] != CREDENTIALS["KEY"]:
        return jsonify({'message': 'Restricted access.'}), 401

    if request.method == 'DELETE':
        try:
            result = Book.delete_book(id)
            
            if result == 'success':
                return jsonify({'message': 'Book deleted successfully.'}), 200
            else:
                print(result)
                return jsonify({'message': result}), 500

        except Exception as err:
            print(err)
            return jsonify({'message': f'Error: {err}'}), 500
        






@app.route(f'/authors', methods=['GET'])
def authors():
    if 'key' not in request.args or request.args['key'] != CREDENTIALS["KEY"]:
        return jsonify({'message': 'Restricted access.'}), 401
    
    if request.method == 'GET':
        return jsonify(Author.get_authors())

@app.route(f'/bought', methods=['GET'])
def bought():
    if 'key' not in request.args or request.args['key'] != CREDENTIALS["KEY"]:
        return jsonify({'message': 'Restricted access.'}), 401
    
    if request.method == 'GET':
        return jsonify(Bought.get_bought())
    
@app.route(f'/cabang', methods=['GET'])
def cabang():
    if 'key' not in request.args or request.args['key'] != CREDENTIALS["KEY"]:
        return jsonify({'message': 'Restricted access.'}), 401
    
    if request.method == 'GET':
        return jsonify(Cabang.get_cabang())
    
@app.route(f'/customer', methods=['GET'])
def customer():
    if 'key' not in request.args or request.args['key'] != CREDENTIALS["KEY"]:
        return jsonify({'message': 'Restricted access.'}), 401
    
    if request.method == 'GET':
        return jsonify(Customer.get_customer())
    
@app.route(f'/publisher', methods=['GET'])
def publisher():
    if 'key' not in request.args or request.args['key'] != CREDENTIALS["KEY"]:
        return jsonify({'message': 'Restricted access.'}), 401
    
    if request.method == 'GET':
        return jsonify(Publisher.get_publisher())
    
@app.route(f'/revenue', methods=['GET'])
def revenue():
    if 'key' not in request.args or request.args['key'] != CREDENTIALS["KEY"]:
        return jsonify({'message': 'Restricted access.'}), 401
    
    if request.method == 'GET':
        return jsonify(Revenue.get_revenue())
    
@app.route(f'/wrote', methods=['GET'])
def wrote():
    if 'key' not in request.args or request.args['key'] != CREDENTIALS["KEY"]:
        return jsonify({'message': 'Restricted access.'}), 401
    
    if request.method == 'GET':
        return jsonify(Wrote.get_wrote())
    
@app.route('/',  methods=['GET'])
def root():
    return jsonify({'message': 'Backend API service Running'}), 200

@app.route('/<path:path>')
def handle_not_available(path):
    return jsonify({'message': 'Route not available'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000)
    print('Running')