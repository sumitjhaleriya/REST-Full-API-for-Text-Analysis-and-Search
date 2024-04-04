# aideveloper

"""
Application Title: RESTful API for Text Analysis
Name : Sumit Jhaleriya

Version: v1.0

Summary: This Python code implements a REST API for text analysis, including user authentication, word tokenization, word-to-paragraph indexing, paragraph ID generation, search functionality, and PostgreSQL data storage.

API Endpoints:
1. /auth/login (POST) - User login endpoint
2. /auth/signup (POST) - User signup endpoint
3. /text/paragraphs (POST) - Add paragraphs endpoint
4. /text/search (GET) - Search for paragraphs containing a word endpoint

"""

from flask import Flask, request, jsonify # type: ignore
from flask_restful import Resource, Api, reqparse# type: ignore
import psycopg2# type: ignore
import uuid

# Configure PostgreSQL connection details
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'text_analysis_db'
DB_USER = 'postgres'
DB_PASS = 'admin@123'

# Create Flask app and API
app = Flask(__name__)
api = Api(app)

# PostgreSQL connection setup
conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
cur = conn.cursor()

# User authentication data (dummy data for demonstration)
users = {'user1@example.com': 'password1', 'user2@example.com': 'password2'}
auth_tokens = {}  # To store authentication tokens

# Helper function to authenticate users
def authenticate(email, password):
    if email in users and users[email] == password:
        token = str(uuid.uuid4())
        auth_tokens[token] = email
        return token
    else:
        return None

# Resource for user login
class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email is required')
        parser.add_argument('password', type=str, required=True, help='Password is required')
        args = parser.parse_args()

        token = authenticate(args['email'], args['password'])
        if token:
            return {'token': token}, 200
        else:
            return {'message': 'Invalid credentials'}, 401

# Resource for user signup
class UserSignup(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email is required')
        parser.add_argument('password', type=str, required=True, help='Password is required')
        args = parser.parse_args()

        if args['email'] in users:
            return {'message': 'Email already exists'}, 400
        else:
            users[args['email']] = args['password']
            return {'message': 'User registered successfully'}, 201

# Resource for adding paragraphs
class AddParagraphs(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str, required=True, help='Text is required')
        args = parser.parse_args()

        paragraphs = args['text'].split('\n\n')
        for paragraph in paragraphs:
            paragraph_id = str(uuid.uuid4())
            words = paragraph.lower().split()
            for word in words:
                cur.execute("INSERT INTO word_paragraph_mapping (word, paragraph_id) VALUES (%s, %s)", (word, paragraph_id))
                conn.commit()
        return {'message': 'Paragraphs added successfully'}, 201

# Resource for searching paragraphs
class SearchParagraphs(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('word', type=str, required=True, help='Word is required')
        args = parser.parse_args()

        cur.execute("SELECT paragraph_id, COUNT(*) as count FROM word_paragraph_mapping WHERE word=%s GROUP BY paragraph_id ORDER BY count DESC LIMIT 10", (args['word'],))
        rows = cur.fetchall()
        result = [{'paragraph_id': row[0], 'word_count': row[1]} for row in rows]
        return jsonify(result)

# API endpoints
api.add_resource(UserLogin, '/auth/login')
api.add_resource(UserSignup, '/auth/signup')
api.add_resource(AddParagraphs, '/text/paragraphs')
api.add_resource(SearchParagraphs, '/text/search')

if __name__ == '__main__':
    app.run(debug=True)