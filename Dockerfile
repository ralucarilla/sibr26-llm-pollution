FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update &&\
  apt-get install -y\
  bash \
  build-essential\
  gcc\
  libffi-dev\
  musl-dev\
  openssl\
  libpq-dev

COPY . .
RUN pip install -r ./requirements.txt
RUN pip freeze
# Remove local database. otr-ee resetdb doesn't work because env variables are not set
RUN rm -f db.sqlite3

EXPOSE 8000 5055
CMD ["otree","prodserver", "0.0.0.0:8000"]
