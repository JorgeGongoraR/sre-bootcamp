FROM python:3-alpine

RUN mkdir /login

WORKDIR /login

COPY . /login/

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "python3" "apy.py" ]

# Add your instructions to dockerize the application
# App must run on port 8000
