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

The command-line interface tool is named ```main.py```
(or ```meme.py```).

> Note: The project rubric specifies that the CLI tool
> should be called ```main.py```, whereas the project
> description and starter code refer to it as
> ```meme.py```. I have addressed this inconsistency
> by creating ```main.py``` as a symbolic link to
> ```meme.py```.

It can be called with any or all of three optional
arguments:

- ```--path```: the path to an input image file
- ```--body```: the body of the quotation to add
- ```--author```: the author of the quotation to add

Any argument that is not supplied by the user will
instead be drawn from the default data.

Example:<br>
```
python main.py --path /path/to/some/image
--body 'Veni, vidi, vici' --author 'Julius Caesar'
```

The result will be saved under a random file name in
the ```tmp``` directory.

## Flask App

description here
