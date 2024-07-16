# Meme Generator Project for Udacity Course (Large Python Codebases with Libraries)

This is my submission for the Meme Generator project,
which is the final part of the Udacity course on Large
Python Codebases with Libraries.

As per the requirements given in the course, this
project contains Python code to superimpose short
quotations over images. These quotations and images
can be supplied by the user, or they can be drawn at
random from default data (which I have left as the
collection of "dog" data included with the starter
code).

This project contains both a command-line interface
(CLI) tool and a Flask app, as described below.

## Command-Line Interface Tool

The command-line interface tool is named `main.py`
(or `meme.py`).

> Note: The project rubric specifies that the CLI tool
> should be called `main.py`, whereas the project
> description and starter code call it `meme.py`.
> I have addressed this inconsistency by creating
> `main.py` as a symbolic link to `meme.py`.

It can be called with any or all of three optional
arguments:

- `--path`: the path to an input image file
- `--body`: the body of the quotation to add
- `--author`: the author of the quotation to add

Any argument that is not supplied by the user will
instead be drawn from the default data.

Example:<br>
```
python main.py --path /path/to/some/image --body 'Veni, vidi, vici' --author 'Julius Caesar'
```

The result will be saved under a random file name in
the `tmp` directory.

## Flask App

The app can be run as `python app.py` and accessed in
a browser by navigating to
[http://127.0.0.1:5000](http://127.0.0.1:5000).
The Random button generates an image and quotation at
random, while the Creator button takes the user to a
form where an input image and quotation can be
supplied.

## Dependencies

This project's dependencies are specified in the file
`requirements.txt`. The recommended way to handle
these dependencies is to install them in a virtual
environment:
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
Note that the virtual environment name `env` can be
replaced by another name of the user's choice.

When finished executing the project, simply run
`deactivate` to deactivate the virtual environment.

## Description of Components

Although the recommended way to interact with this
project is via the CLI tool or the Flask app, the user
may still find this description of the individual
components of the project to be helpful. Perhaps more
honestly, this section is here only because the
project seems to require it.

> Note: Each component's list of dependencies below
> includes only those dependencies not found in the
> Python standard library.

### `main.py` (or `meme.py`)

This file provides the aforementioned CLI tool.

Dependencies: `Pillow` (external), `QuoteEngine`,
`MemeEngine`

### `app.py`, `static`, `templates`, `tmp`

The file `app.py` provides the Flask app.
The directories `static`, `templates`, `tmp` are used
by this app.

Dependencies: `flask` (external), `Pillow` (external),
`QuoteEngine`, `MemeEngine`

### `_data`, `fonts`

These directories simply provide default data and fonts.

Dependencies: none

### `MemeEngine.py`

This file provides the `MemeEngine` class, which has
`make_meme` and `random_file_path` methods. Please
refer to the associated documentation for further
details of how to use these methods.

Dependencies: `Pillow` (external)

### `QuoteEngine`

This module contains several submodules:

#### `QuoteModel.py`

This submodule provides the `QuoteModel` class.

Dependencies: none

#### `IngestorInterface.py`

This submodule provides `IngestorInterface`, an
abstract base class for ingesting quotes, which has
`can_ingest` and `split_fail` methods. Please refer to
the associated documentation for further details of
how to use these methods. It also has an abstract
method `parse`, which is realized by various
subclasses.

This submodule also provides a custom IngestionError
exception that can be raised if quote ingestion fails.

Dependencies: `QuoteModel`

#### `CsvIngestor.py`, `DocxIngestor.py`, 'PdfIngestor.py`, `TextIngestor.py`

These submodules respectively provide the subclasses
`CsvIngestor`, `DocxIngestor`, 'PdfIngestor`, and
`TextIngestor`. Each subclass provides a realization
of the abstract `parse` method that ingests quotes
from the appropriate file type.

Dependencies:  `QuoteModel`, `IngestorInterface`

#### `Ingestor.py`

This submodule provides a final subclass `Ingestor`
with a realization of `parse` that determines and
applies the appropriate ingestion strategy for a file
provided.


Dependencies:  `QuoteModel`, `IngestorInterface`,
`CsvIngestor`, `DocxIngestor`, `PdfIngestor`,
`TextIngestor`
