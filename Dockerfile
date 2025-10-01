FROM python:3

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY update_repo_json.py /update_repo_json.py

CMD ["python", "/update_repo_json.py"]