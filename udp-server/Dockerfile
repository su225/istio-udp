FROM python:3.10.2-alpine3.15

ENV SERVER_PORT="2000"
ENV SERVER_VERSION="v1"

WORKDIR /app

COPY udp.py ./

ENTRYPOINT [ "python", "-u", "./udp.py"]