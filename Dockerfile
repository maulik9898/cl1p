FROM python:3.8-alpine as base

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD . .
RUN pip install -r requirements.txt \
    && pip install -e .

