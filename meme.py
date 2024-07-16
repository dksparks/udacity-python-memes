import os
import random
from argparse import ArgumentParser
from PIL import UnidentifiedImageError
from QuoteEngine.Ingestor import Ingestor
from QuoteEngine.QuoteModel import QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        # For some reason, the starter code treated path as a List,
        # with img taken as the first element of path:
        #
        # img = path[0]
        #
        # This is inconsistent with the specifications for the project,
        # in which path is described as a single path to a single image.
        # Thus, I have changed this line to the following:
        #
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    try:
        path = meme.make_meme(img, quote.body, quote.author)
        return path
    except FileNotFoundError:
        return f'The input image {img} could not be found.'
    except UnidentifiedImageError:
        return f'The input image {img} could not be identified.'
    except OSError:
        return 'The output image could not be written.'


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate a meme.")
    # Arguments will default to None if not provided,
    # as expected by generate_meme defined above.
    parser.add_argument('--path', type=str, help='path to an image file')
    parser.add_argument(
        '--body', type=str, help='quote body to add to the image',
    )
    parser.add_argument(
        '--author', type=str, help='quote author to add to the image',
    )
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
