# syntax=docker/dockerfile:1
FROM python:3.10.5-slim-buster

# Set the working directory
WORKDIR /app

# Copy the contexts of the requirements file into a new file in our 
#working directory
COPY requirements.txt requirements.txt

# Run the install command to install all the dependencies in requirements file
RUN pip3 install -r requirements.txt


# Copy all the fiels in the current directory into the working directory of image
COPY . .

# Tell docker what command we want to run when our image is executed inside a container
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]