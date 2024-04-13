FROM ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install telebot
RUN mkdir /root/tgdiary
RUN mkdir /root/tgdiary/data
ADD main.py /root/tgdiary/main.py
WORKDIR /root/tgdiary

CMD python3 /root/tgdiary/main.py