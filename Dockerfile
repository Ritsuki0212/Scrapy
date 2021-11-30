FROM python:3.8.12-alpine3.15
ADD . /src
WORKDIR /src
# Scrapyをインストールする際に必要になる、GCCなどのCコンパイラをインストール
RUN apk add build-base libffi-dev
RUN pip install -r requirements.txt