FROM python:3.8.0-alpine3.10
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
CMD ["python", "start.py"]
