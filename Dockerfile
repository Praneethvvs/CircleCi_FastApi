FROM python:3.7
COPY . /usr/app
WORKDIR /usr/app
RUN chmod +x ./start.sh
RUN pip install -r requirements.txt
CMD ["./start.sh"]