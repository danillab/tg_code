FROM python:3.7
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app/ .
# CMD ["python", "main.py"]
CMD ["gunicorn", "-b 0.0.0.0:80", "main:app"]