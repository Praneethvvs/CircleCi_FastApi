FROM python:3.7
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
COPY . /usr/app
WORKDIR /usr/app
RUN pip install -r requirements.txt
CMD ["./start.sh"]