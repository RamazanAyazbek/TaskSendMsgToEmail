
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
VOLUME [ "/data/app" ]
CMD ["uvicorn", "task:app", "--host", "0.0.0.0", "--port", "8000"]
