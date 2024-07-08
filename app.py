from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    genre = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    reviews = db.relationship('Review', backref='movie', lazy=True, cascade="all, delete-orphan")

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    review_text = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        description = request.form.get('description', '')
        new_movie = Movie(title=title, genre=genre, description=description)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_movie.html')

@app.route('/movie/<int:id>', methods=['GET', 'POST'])
def view_movie(id):
    movie = Movie.query.get_or_404(id)
    if request.method == 'POST':
        review_text = request.form['review_text']
        new_review = Review(movie_id=id, review_text=review_text)
        db.session.add(new_review)
        db.session.commit()
    reviews = Review.query.filter_by(movie_id=id).all()
    return render_template('view_movie.html', movie=movie, reviews=reviews)

@app.route('/search_movie', methods=['GET', 'POST'])
def search_movie():
    if request.method == 'POST':
        search_query = request.form['search_query']
        search_results = Movie.query.filter((Movie.title.contains(search_query)) | (Movie.genre.contains(search_query))).all()
        return render_template('search_movie.html', movies=search_results)
    return render_template('search_movie.html', movies=[])

@app.route('/delete_movie/<int:id>', methods=['POST'])
def delete_movie(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/api/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([{'id': movie.id, 'title': movie.title, 'genre': movie.genre, 'description': movie.description} for movie in movies])

@app.route('/api/movies', methods=['POST'])
def add_movie_api():
    data = request.get_json()
    new_movie = Movie(title=data['title'], genre=data['genre'], description=data.get('description', ''))
    db.session.add(new_movie)
    db.session.commit()
    return jsonify({'id': new_movie.id, 'title': new_movie.title, 'genre': new_movie.genre, 'description': new_movie.description}), 201

if __name__ == '__main__':
    app.run(debug=True)
