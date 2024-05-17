FROM python:3.10-alpine

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
    # CFFI dependencies
    && apk add libffi-dev py-cffi \
    # cairo
    && apk add cairo cairo-dev pango-dev gdk-pixbuf-dev poppler-utils

RUN apk add git
RUN addgroup -S django \
    && adduser -S -G django django

# Upgrade PIP
RUN pip install --upgrade pip

# Install via requirements.txt
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/staging.txt \
    && rm -rf /requirements

COPY ./docker/staging/django/entrypoint /entrypoint
# here, s/\r// (search-replace-pattern) => Carriage return (\r) will be replaced by nothing("")
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
RUN chown django /entrypoint

COPY ./docker/staging/django/start /start
# here, s/\r// (search-replace-pattern) => Carriage return (\r) will be replaced by nothing("")
RUN sed -i 's/\r//' /start
RUN chmod +x /start
RUN chown django /start

# for celery worker
COPY ./docker/staging/django/celery/worker/start /start-celery-worker
RUN sed -i 's/\r//' /start-celery-worker
RUN chmod +x /start-celery-worker
RUN chown django /start-celery-worker

# for DB migration
COPY ./docker/staging/django/migration/start /start-migration
RUN sed -i 's/\r//' /start-migration
RUN chmod +x /start-migration
RUN chown django /start-migration

COPY . /app
RUN chown -R django /app

USER django

WORKDIR /app
