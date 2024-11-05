FROM python:3
WORKDIR /usr/src/app 
COPY . .
CMD [ "python", "/usr/src/app/app2.py" ]
