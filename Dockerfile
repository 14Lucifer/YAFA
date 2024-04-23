FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 80
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
