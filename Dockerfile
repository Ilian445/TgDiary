FROM ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install telebot
RUN mkdir /root/tgdiary
COPY main.py /root/tgdiary/main.py
RUN ls -l /root/tgdiary/
ENTRYPOINT python3 root/tgdiary/main.py
