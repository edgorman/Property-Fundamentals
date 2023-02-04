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

To run the backend locally, run the following and then open [the docs page](http://127.0.0.1:5000/docs) to prove it's working.

```
gunicorn -k uvicorn.workers.UvicornWorker -b 127.0.0.1:5000 backend.api:api
```

## Testing

Run the testing scripts in the base directory:

```
python -m autopep8 backend/ --in-place --aggressive --recursive --max-line-length 120
python -m flake8 backend/ --max-line-length=120
python -m pytest -svv backend/tests/
```
