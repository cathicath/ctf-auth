FROM python:3.9

# Ställ in arbetskatalogen
WORKDIR /app

# Kopiera filerna till containern
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY templates/ templates/
COPY static/ static/

# Installera beroenden
RUN pip install --no-cache-dir -r requirements.txt

# Exponera porten
EXPOSE 5001

# Se till att Flask körs på rätt host
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

# Starta appen
CMD ["python", "-m", "flask", "run", "--port=5001"]
