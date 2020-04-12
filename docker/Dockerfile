FROM python:3.6

WORKDIR /app/src

ADD requirements /app/requirements

#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN export PYCURL_SSL_LIBRARY=openssl \
    && pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip \
    && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r /app/requirements/test.txt

ADD docker /app/docker
ADD src /app/src