FROM python:latest

WORKDIR /app/code

COPY requirements.txt /app/code

RUN pip install -r requirements.txt

COPY . /app/code

CMD ["pytest","./test_class.py"]
