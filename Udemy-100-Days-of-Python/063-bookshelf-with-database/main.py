from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# Create table schema in the database
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # READ ALL RECORDS
    # all_books = [<Book 1>, <Book 2>, ... <Book N>]
    all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()  # list(all_books) if w/o .all()
    return render_template('index.html', books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # CREATE RECORD
        new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    # SELECT BOOK BY ID
    book_id = request.args.get('id')
    if request.method == 'POST':
        # UPDATE RECORD
        # book_id = request.form['id']
        book_selected = db.get_or_404(Book, book_id)
        book_selected.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))

    book_selected = db.get_or_404(Book, book_id)
    return render_template('edit.html', book=book_selected)


@app.route('/delete')
def delete():
    # DELETE RECORD BY ID
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
