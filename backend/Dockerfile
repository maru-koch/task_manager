FROM python:3.9-slim-bullseye

WORKDIR /app/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/backend/

# RUN apt-get upgrade \
#     && apt-get install -y netcat gcc postgresql \
#     && apt-get clean

# RUN apt-get install update \
#     && apt-get install -y binutils libproj-dev python-gdal python3-gdal gdal-bin 

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app/backend/

ENTRYPOINT celery -A backend worker -l info

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
