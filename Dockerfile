FROM python:3.8

WORKDIR /app
ENV PYTHONPATH=/app

COPY ./promocode_generator /app
RUN pip3 install -r requirements.txt