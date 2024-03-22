# https://hub.docker.com/_/python
FROM python:3.9.9-alpine3.15
# Still needs testing
#FROM python:3.11.0-alpine3.16
MAINTAINER David Chappell <David.Chappell@trincoll.edu>
ARG uid
COPY requirements.txt /tmp/requirements.txt
RUN apk add --no-cache git \
	&& pip3 install -r /tmp/requirements.txt \
	&& adduser -u $uid -G users -D app
WORKDIR /app
COPY . .
EXPOSE 5000
USER app
#CMD ["python", "start.py"]
CMD ["gunicorn", "--workers=4", "--bind=:5000", "--access-logfile=-", "app.production:app"]
