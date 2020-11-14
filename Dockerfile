FROM python:3.8

COPY ./conf.d/requirements.txt /app/

WORKDIR /app

RUN pip install -U pip
RUN pip install -r requirements.txt

WORKDIR /app

CMD ["python", "run.py"]
