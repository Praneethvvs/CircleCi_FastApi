FROM python:3.7
COPY . /usr/app
EXPOSE 7000
WORKDIR /usr/app
RUN pip install -r requirements.txt
