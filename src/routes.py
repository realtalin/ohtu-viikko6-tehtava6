from flask import redirect, render_template, request
from app import app
from services.book_citation_service import book_service
from services.bibtex_service import BibTexService

@app.route("/")
def index():
    """Avaa etusivun
    """

    return render_template("index.html", book=book_service.get_last())

@app.route("/form")
def form():
    """Avaa lomakkeen, johon täytetään lähdeviitaus
    """

    return render_template("form.html")

@app.route("/create", methods=["POST"])
def create():
    """Luo lomakkeen pohjalta lähdeviitauksen
    """

    author_name = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    publisher = request.form["publisher"]
    book_service.save_citation(author_name, title, year, publisher)
    return redirect("/")

@app.route("/all")
def view_all_citations():
    """Näyttää kaikki lähdeviittauksen ihmisluettavassa muodossa
    """

    return render_template(
        "citations.html",
        citations = book_service.get_all()
    )

@app.route("/bibtex")
def generate_bibtex():
    """Muodostaa lähdeviittauksista bibtex muotoisen tekstin
    """

    bibtex_service = BibTexService()

    bibtex_service.turn_books_to_bibtex()

    bibtex = bibtex_service.get_bibtex()

    return render_template("bibtex.html", bibtex=bibtex)
