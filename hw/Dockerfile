FROM python:3

EXPOSE 5000

WORKDIR /app

ADD requirements.txt ./
ADD app.py ./

HEALTHCHECK --interval=15s --timeout=1s CMD curl http://127.0.0.1:5000/ || exit 1

RUN pip install -r requirements.txt

CMD flask run --host=0.0.0.0