FROM python:3.9.18-alpine3.18

COPY . /app
WORKDIR /app
RUN pip3 install --no-cache-dir -r requirements.txt

ENV TZ Asia/Seoul

CMD [ "python3", "-u", "server/main.py" ]