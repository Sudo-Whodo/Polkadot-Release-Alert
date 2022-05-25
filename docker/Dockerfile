FROM python:alpine3.15

LABEL Maintainer="@frazzled_dazzle"
LABEL Company="stkd.io"

#Setup env
RUN apk update;\
    apk add py-pip

RUN pip install feedparser;\
    pip install datetime;\
    pip install time;\
    pip install sys;\
    pip install pathlib

#Patch the image
RUN apk upgrade
 
#Move over main.py and data.dat
COPY /src/main.py /etc/periodic/15min/main.py
COPY /src/data.dat /etc/periodic/15min/data.dat

CMD [ "python", "/etc/periodic/15min/main.py"]
