from python:3.10

WORKDIR /app

COPY ./funnel/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./funnel /app/

ENTRYPOINT ["python", "main.py"]
