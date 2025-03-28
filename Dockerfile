FROM python:3.11

WORKDIR /app/core

COPY requirements.txt . /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED=1

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]