FROM python:3.11.9-slim
WORKDIR /app
COPY . /app
RUN pip install --progress-bar off -r requirements.txt
RUN pip install --progress-bar off gunicorn
EXPOSE 80
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app"]
#  Use Gunicorn to spawn multiple workers without relying heavily on threading.
