FROM postgres:14-alpine
LABEL authors="AndranikTorosan"

ARG USER_NAME
ARG USER_PASSWORD

ENV POSTGRES_PASSWORD=VishupHell
ENV POSTGRES_USER=VishupHell
ENV POSTGRES_DB=project

RUN apk add --no-cache tzdata
EXPOSE 9000
ENV TZ=Europe/London