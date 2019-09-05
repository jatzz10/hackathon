FROM ubuntu:16.04
MAINTAINER "AYUSH PATIDAR"


RUN mkdir /app
WORKDIR /app

RUN apt-get update \
            && apt-get -y install python3-pip

COPY . /app
RUN pip3 install -r requires.txt

EXPOSE 80

CMD echo WORKDIR

ENTRYPOINT ["python3"]
CMD  ["start.py"]