"""Start the flask app to begin to generate memes."""

import random
import os
import requests
from flask import Flask, render_template, request
from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor, QuoteModel

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = [
        "_data/DogQuotes/DogQuotesTXT.txt",
        "_data/DogQuotes/DogQuotesDOCX.docx",
        "_data/DogQuotes/DogQuotesPDF.pdf",
        "_data/DogQuotes/DogQuotesCSV.csv"]
    quotes = []
    for f in quote_files:
        quotes.append(Ingestor.parse(f))
    if len(quotes) == 0:
        raise Exception("No quotes were parsed from qoute files")

    images_path = "_data/photos/dog/"
    imgs = []
    for file in os.listdir(images_path):
        imgs.append(f'{images_path}{file}')
    if len(imgs) == 0:
        raise Exception("No quotes were parsed from qoute files")
    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(random.choice(quotes))
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme."""
    img_url = request.form.get("image_url")
    try:
        response = requests.get(img_url, stream=True)
    except requests.exceptions.RequestException:
        return render_template("meme_form.html")

    img_path = f"./z{random.randint(0, 9999)}.jpg"
    with open(img_path, "wb") as f:
        f.write(response.content)

    body = request.form.get("body", "")
    author = request.form.get("author", "")

    try:
        path = meme.make_meme(img_path, body, author)
    except requests.exceptions.RequestException:
        return render_template("meme_form.html")
    else:
        os.remove(img_path)

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
