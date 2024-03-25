FROM python:3.9

RUN pip install mysql-connector-python

WORKDIR /app

COPY commands.py /app/

CMD [ "python", "./commands.py" ]
