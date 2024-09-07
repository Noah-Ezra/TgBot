FROM python:3.9-slim
WORKDIR /app
COPY . /app
EXPOSE 8080
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
