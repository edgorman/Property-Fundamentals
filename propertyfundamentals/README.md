# Property Fundamentals - Module
This is the python module that performs the extract, transform and load (ETL) functionality of the property fundamentals app. This README assumes you have set up the developer environment as detailed in the base of this repository.

## Installation

Install the required python packages:

```
python -m pip install propertyfundamentals/.
```

If you're developing this package a handy line to reinstall is:
```
python -m pip uninstall propertyfundamentals -y; python -m pip install propertyfundamentals/.
```

## Usage

TODO

## Testing

Run the testing scripts in the base directory:

```
python -m autopep8 propertyfundamentals/ --in-place --aggressive --recursive --max-line-length 120
python -m flake8 propertyfundamentals/ --max-line-length=120
python -m pytest -svv propertyfundamentals/tests/
```
