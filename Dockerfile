FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=${PORT}

EXPOSE ${PORT}

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:${PORT}" ]