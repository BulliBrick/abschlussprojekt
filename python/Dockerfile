# Image: python:3.9.13
FROM python:3.9.13

# pip install den mysql-connector-python
RUN pip install --no-cache-dir mysql-connector-python

# das Verzeichnis /app wird erstellt und als Arbeitsverzeichnis festgelegt
WORKDIR /app

# die Datei 'commands.py' wird in das Verzeichnis /app kopiert
COPY commands.py /app/

# der Container führt das Python-Skript 'commands.py' aus
CMD [ "python", "./commands.py" ]

