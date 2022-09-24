# pull official base image
FROM python:3.9.5-alpine
# create the appropriate directories
ENV APP_HOME=/usr/src/app
# install psycopg2 dependencies
RUN apk update \
    && apk add libcurl curl-dev python3-dev libc-dev postgresql-dev build-base gcc python3-dev musl-dev libffi-dev \
    py3-pillow freetype-dev libpng-dev openblas-dev g++ \
    jpeg-dev zlib-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libxslt-dev
RUN mkdir $APP_HOME
# copy entrypoint-prod.sh
COPY ./build/entrypoint.sh $APP_HOME
COPY ./cronjob/crontab.txt $APP_HOME
COPY ./cronjob/script.sh $APP_HOME
RUN chmod 755 $APP_HOME/script.sh $APP_HOME/entry.sh
RUN /usr/bin/crontab $APP_HOME/crontab.txt
# copy project
COPY ./requirements/production.txt .
RUN pip install -r production.txt
WORKDIR $APP_HOME
# copy project
COPY ./src $APP_HOME/src
COPY ./settings $APP_HOME/settings
# COPY ./certs $APP_HOME/certs
COPY ./manage.py $APP_HOME
COPY ./core $APP_HOME/core
COPY ./assets $APP_HOME/assets
# COPY ./locale $APP_HOME/locale
RUN addgroup -S app && adduser -S app -G app
# chown all the files to the app user
RUN chown -R app:app $APP_HOME
RUN chmod +x $APP_HOME/manage.py
# change to the app user
USER app
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]