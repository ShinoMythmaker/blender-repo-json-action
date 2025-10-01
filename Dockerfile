FROM python:3.11-slim
WORKDIR /app
COPY update_repo_json.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "update_repo_json.py"]