# syntax=docker/dockerfile:1
FROM basavyr/pyenv-ubuntu:latest


SHELL ["usr/bin/bash", "-c"]

COPY . .

CMD ["ls"]