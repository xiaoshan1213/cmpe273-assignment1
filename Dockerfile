FROM python:2.7.13
MAINTAINER Your Name "wenjin.ma@sjsu.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install PyYAML
ENTRYPOINT ["python", "app.py"]
CMD ["app.py", arg]
#CMD ["https://github.com/xiaoshan1213/cmpe273-assignment1-config"]