FROM python:3.11-alpine

# Set to non-empty value (commonly set to 1) means it will not wait to show the outputs (logs or error)
ENV PYTHONUNBUFFERED 1
# By 1 means, it will not build RUST extension
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1

RUN apk update \
    # psycopg2 dependencies
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && apk add build-base \
    # Pillow dependencies \
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
    && apk add postgresql-client

# Upgrade PIP
RUN pip install --upgrade pip

# Install via requirements.txt
COPY ./requirements /requirements
RUN pip install -r /requirements/base.txt

COPY ./docker/local/django/entrypoint /entrypoint
# here, s/\r// (search-replace-pattern) => Carriage return (\r) will be replaced by nothing("")
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
# here, s/\r// (search-replace-pattern) => Carriage return (\r) will be replaced by nothing("")
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
