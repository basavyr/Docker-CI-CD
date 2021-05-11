[![Test-Applications](https://github.com/basavyr/Py-Docker-CI-CD/actions/workflows/test-pipeline.yml/badge.svg)](https://github.com/basavyr/Py-Docker-CI-CD/actions/workflows/test-pipeline.yml)[![Build-Applications](https://github.com/basavyr/Py-Docker-CI-CD/actions/workflows/build-pipeline.yml/badge.svg)](https://github.com/basavyr/Py-Docker-CI-CD/actions/workflows/build-pipeline.yml)[![Release-Applications](https://github.com/basavyr/Py-Docker-CI-CD/actions/workflows/release.yml/badge.svg)](https://github.com/basavyr/Py-Docker-CI-CD/actions/workflows/release.yml)

# Python+Docker 

![](https://www.docker.com/sites/default/files/d8/2019-07/horizontal-logo-monochromatic-white.png)

*CI/CD Pipelines for Python development using Docker containers.*

## Python Development

The current project uses an [Ubuntu based image](https://hub.docker.com/repository/docker/basavyr/pyenv-ubuntu) that is configured with Python + support for **virtual environments**.

* pyenv
* pipenv
* stable python version `3.8.6`
* other useful python packages
    - numpy
    - scipy
    - matplotlib
    - psutil
    - watchdog