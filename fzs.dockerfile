
from python:3.7.4-buster

RUN apt-get update -y

RUN pip3 install    \
                    "rasterstats==0.13.0" \
                    jupyter \
                    jupyterlab \
                    "gdal==2.2.2" 