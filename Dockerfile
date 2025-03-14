FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py
COPY templates/ templates/
COPY static/ static/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

CMD ["python", "-m", "flask", "run", "--port=5001"]
