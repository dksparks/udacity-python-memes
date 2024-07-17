import random
import os
import requests
from flask import Flask, render_template, abort, request
from PIL import UnidentifiedImageError
from QuoteEngine.Ingestor import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""

    image_url = request.form.get('image_url')
    try:
        image = requests.get(image_url)
    except:
        return f'The input image {image_url} could not be accessed.'
    # Do not bother with a file extension on the name of the temp file.
    # We do not know the format of the incoming file, and while we could
    # try to infer it from a possible file extension in the URL, there
    # is really no point since the file will be removed later anyway.
    temp_file_path = meme.random_file_path('./tmp', '')
    with open(temp_file_path, 'wb') as temp_file:
        temp_file.write(image.content)

    body, author = request.form.get('body'), request.form.get('author')
    try:
        path = meme.make_meme(temp_file_path, body, author)
        return render_template('meme.html', path=path)
    except UnidentifiedImageError:
        return f'The input image {image_url} could not be identified.'
    finally:
        os.remove(temp_file_path)


if __name__ == "__main__":
    app.run()
