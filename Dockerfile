# syntax=docker/dockerfile:1
FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN pip install --upgrade pip
COPY ./VotingMatch/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 VotingMatch/votingproject.wsgi:application
