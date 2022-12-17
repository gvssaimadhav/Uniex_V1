FROM python:3.9

#Use working directory /app
WORKDIR /app

#Copy all the content of current directory to /app
ADD . /app
ADD folder /root/

#Installing required packages
RUN pip install -r requirements.txt 
# RUN /usr/bin/python train.py
#Open port 5000
EXPOSE 5000

#Set environment variable
ENV NAME OpentoAll

#Run python program
CMD ["python","app.py"]