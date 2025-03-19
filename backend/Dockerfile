# use the python 3.12.5-alpine container image
FROM python:3.12.5-alpine

# set working directory
WORKDIR /app

# copy the current directory contents into the container at /app
ADD . /app

# install dependencies
RUN pip install -r requirements.txt

# run the command to start the app
CMD ["fastapi", "run", "main.py"]