WORKDIR /github/workspace
COPY update_repo_json.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "/github/workspace/update_repo_json.py"]