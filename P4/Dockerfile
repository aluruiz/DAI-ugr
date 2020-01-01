FROM python:3.7-alpine
WORKDIR /flask

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development

RUN pip3 install Jinja2
RUN pip install pickleshare
COPY . .
RUN pip install -r requirementsFlask.txt

CMD ["flask", "run"]
 