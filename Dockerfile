FROM tiangolo/uwsgi-nginx-flask:latest
# RUN apk update && apk add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install --no-cache-dir -r  /var/www/requirements.txt
COPY ./nltk_modules.py /var/www/nltk_modules.py
RUN python /var/www/nltk_modules.py