FROM golang:latest

RUN apt update

RUN go get github.com/bitly/go-nsq
RUN go get github.com/go-sql-driver/mysql

COPY ./crawl/*.go /go/
COPY ./credential.json /go/
RUN go fmt *.go
RUN go build -o twitter_crawler
CMD ./twitter_crawler
