FROM python:3.11.9-slim
WORKDIR /app
COPY . /app
RUN pip install --progress-bar off -r requirements.txt
EXPOSE 80
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
