#base image
FROM python:3.7-buster

RUN mkdir /app

WORKDIR /app
#copy requirements file to image 

COPY requirements.txt requirements.txt 
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
#directory to store app source code


#switch to /app directory so that everything runs from here


#copy the app code to image working directory
COPY ./app /app

RUN ls
EXPOSE 8000
CMD ["python", "manage.py", "collectstatic"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]