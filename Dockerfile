FROM python:3.9.6-alpine

WORKDIR /app

COPY . .

RUN pip install --user -r requirements.txt

ENTRYPOINT ["python3", "-m", "src.check_services"]
