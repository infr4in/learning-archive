from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

MOVIE_DB_API_KEY = "YOUR API KEY"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config["SECRET_KEY"] = "kagebunshinodjutsu"
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# CREATE TABLE SCHEMA
with app.app_context():
    db.create_all()


# FORMS
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")  # neet to be StringField because FloatField is DataRequired
    review = StringField("Your Review")
    submit = SubmitField("Done")


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    # READ ALL RECORDS
    all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()

    # UPDATE MOVIES RANKING BY RATING
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": form.title.data})
        data = response.json()["results"]
        return render_template("select.html", data=data)

    return render_template("add.html", form=form)


@app.route("/find")
def find():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(url, params={"api_key": MOVIE_DB_API_KEY})
        data = response.json()

        # CREATE RECORD
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))

    return redirect(url_for("home"))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()

    # SELECT MOVIE BY ID
    movie_id = request.args.get("id")
    selected_movie = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        # UPDATE RECORD
        selected_movie.rating = float(form.rating.data) if form.rating.data else selected_movie.rating
        selected_movie.review = form.review.data if form.review.data else selected_movie.review
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", movie=selected_movie, form=form)


@app.route("/delete")
def delete():
    # DELETE RECORD BY ID
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
