# Property Fundamentals - Backend
The is the [FastAPI](https://fastapi.tiangolo.com/) backend that performs the API routing and data transform/loading. This README assumes you have set up the developer environment as detailed in the base directory of this repository.

## Installation

Install the required python packages:

```
python -m pip install propertyfundamentals/.
python -m pip install backend/.
```

If you're developing this package a handy line to reinstall is:
```
python -m pip uninstall backend -y; python -m pip install backend/.
```

## Usage

TODO

## Testing

Run the testing scripts in the base directory:

```
python -m autopep8 backend/ --in-place --aggressive --recursive --max-line-length 120
python -m flake8 backend/ --max-line-length=120
python -m pytest -svv backend/tests/
```
