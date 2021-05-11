# syntax=docker/dockerfile:1
FROM basavyr/pyenv-ubuntu:latest

ENV PATH="/root/.pyenv/plugins/pyenv-virtualenv/shims:/root/.pyenv/shims:/root/.pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV HOME="/root"
WORKDIR $HOME

SHELL ["/bin/bash", "-c"]

COPY . .

RUN pyenv global 3.8.6
RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade pipenv

RUN chmod 777 ./entrypoint.sh

CMD ["/bin/bash","./entrypoint.sh"]

# CMD ["python","./py/get_process/py_process.py"]
