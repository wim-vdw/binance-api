FROM python:3.11-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "gunicorn", "--workers", "4", "--bind", "0.0.0.0:80", "--access-logfile", "-", "app:create_app()" ]
