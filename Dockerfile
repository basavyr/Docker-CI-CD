# syntax=docker/dockerfile:1
FROM basavyr/pyenv-ubuntu:latest

SHELL ["/bin/bash", "-c"]

COPY . .

CMD ["./entrypoint.sh"]
