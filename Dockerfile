FROM python:3-onbuild

COPY ./pogo_async /pogo_async

RUN for r in `cat requirements.txt`; do pip install $r; done
