FROM python:3.9
LABEL maintainer="Dinesh Babu TG <tgdinesh_babu@yahoo.co.in>"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app
EXPOSE 8000
ENTRYPOINT [ "python" ]

CMD [ "candidate_service_app.py" ]