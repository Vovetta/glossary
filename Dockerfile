FROM python:3.10-alpine

RUN mkdir /app
WORKDIR /app

COPY . .

RUN pip install wheel setuptools && pip install -r requirements.txt

CMD ["python", "main.py"]
