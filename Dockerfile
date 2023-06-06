FROM python:latest

#get dependencies
COPY inclusive-name-checker.py /root/venv/working


RUN mkdir "/root/venv/working"
ENV VIRTUAL_ENV=/root/venv
RUN
    