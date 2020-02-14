FROM python:3-buster

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

#CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn","--config=gunicorn.py","app:app"]
