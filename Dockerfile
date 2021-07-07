# init a base image
FROM python:3.6.1-alpine

ENV LISTEN_PORT=5000
EXPOSE 5000

RUN pip install --upgrade pip

# define the present working directory
WORKDIR /todolist-app

# copy the contents into the working dir
ADD . /todolist-app


# run pip to install the dependencies of the flask app
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
# RUN pip install -r requirements.txt

# define the command to start the container
CMD ["python","app.py"]