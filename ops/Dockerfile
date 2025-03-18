FROM public.ecr.aws/lambda/python:3.12 AS base

COPY private-requirements.txt /tmp/private-requirements.txt
RUN pip install -r /tmp/private-requirements.txt

COPY public-requirements.txt /tmp/public-requirements.txt
RUN pip install -r /tmp/public-requirements.txt

ENV PYTHONPATH $PYTHONPATH:/ihc-install/packages:/ihc-install/dev-packages:/ihc/auth

WORKDIR /ihc

# create a development stage which has dev related packages installed
FROM base AS devl

RUN dnf install -y which
RUN dnf install -y expat

COPY dev-requirements.txt /tmp/dev-requirements.txt
RUN pip install -r /tmp/dev-requirements.txt

ENTRYPOINT [ "py.test", "tests/functional" ]

# create a build stage which has a hardcoded copy of the code
FROM devl AS build

COPY . /ihc

# create a deploy stage with only the layers needed for deployment
FROM base AS deploy

COPY . /ihc

CMD [ "datadog_lambda.handler.handler" ]