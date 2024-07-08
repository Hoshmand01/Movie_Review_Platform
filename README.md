
# Movie Review Platform

This project is a Movie Review Platform built using Flask and SQLite. It allows users to add movies, view movies, submit reviews, view reviews, search for movies by title or genre, and delete movies. It also includes RESTful web services for adding and viewing movies.

## Features

- Add a new movie
- View all movies
- Submit a review for a movie
- View reviews for a movie
- Search for a movie by title or genre
- Delete a movie

## RESTful Web Services

- Add a new movie: `POST /api/movies`
- View all movies: `GET /api/movies`

## Setup Instructions

1. Clone the repository:
   
   git clone <repository-url>
   cd movie_review_platform
   

2. Create a virtual environment and activate it:
   
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   

3. Install the required packages:
   
   pip install -r requirements.txt
   

4. Run the Flask application:
  
   python app.py
   

5. Access the application at `http://127.0.0.1:5000`.

## Usage

- Open the application in your browser.
- Use the interface to add movies, view movies, submit reviews, search for movies, and delete movies.
- Use Postman or Curl to test the RESTful web services.
