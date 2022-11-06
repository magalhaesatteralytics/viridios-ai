FROM python:3.11-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=viridios

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
