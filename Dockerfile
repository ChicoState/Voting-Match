# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN pip install --upgrade pip
COPY ../VotingMatch/requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000