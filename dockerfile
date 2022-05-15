FROM python:latest

RUN mkdir -p /app/src
WORKDIR /app/src

COPY ./dockerfile .
COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]