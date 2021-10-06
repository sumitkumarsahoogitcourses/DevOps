FROM python:3.9
WORKDIR /backend

COPY ./requirements.txt ./app.py ./.flaskenv ./
RUN pip install -r ./requirements.txt
ENV FLASK_ENV development

EXPOSE 7001
# CMD ["gunicorn", "-b", ":7001", "backend:app"]
CMD ["gunicorn -b 0.0.0.0:7001 app:app"]