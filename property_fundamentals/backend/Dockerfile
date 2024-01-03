FROM python:3.11

WORKDIR /backend
ADD . /backend/

RUN python -m pip install -r requirements.txt
CMD uvicorn main:app
