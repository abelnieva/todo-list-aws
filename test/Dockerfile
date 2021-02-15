FROM python:3.7.9-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers libressl-dev musl-dev libffi-dev
RUN apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt