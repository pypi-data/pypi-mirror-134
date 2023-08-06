# Canvas LMS folder sync

This is a command-line tool and Python package to synchronise a local folder with one in a Canvas LMS course.

In order to use this, you need a Canvas API token linked to an account which has permission to create files in your target course's Files section.
See [the Canvas API documentation](https://canvas.instructure.com/doc/api/file.oauth.html#manual-token-generation) for instructions on how to get a token.

## Installation

Python 3.8 or newer is required.

To install the package, run:

```
pip install canvaslms_sync
```

This provides a shell command `canvas_sync`.

## Usage

```
canvas_sync local_folder remote_url -t CANVAS_API_TOKEN
```

You can store your Canvas API token in a file like this:

```
[Canvas]
canvas_api_token = TOKEN
```

By default, the script looks for this file in `credentials.ini` in the current working directory, but you can specify a different path with the `-c` option.

Hidden files and folders (those whose names start with `.`) are ignored by default. You can include them with the `--include-hidden` option.

## Development

I followed the [Python packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/) to make this package.

To build this package, you need `twine` and `build`:

```
python3 -m pip install twine build
```

First, build the distributable files:

```
python3 -m build
```

That produces `.tar.gz` and `.whl` files in `./dist`. 
You can try installing the package in a different virtualenv with `pip install dist/canvaslms_sync-$VERSION-py3-none-any.whl`.

To upload to PyPI:

```
python3 -m twine upload --repository pypi dist/*
```
