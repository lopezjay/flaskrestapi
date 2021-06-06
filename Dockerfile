FROM python:3.9-alpine
COPY . .
WORKDIR /api
RUN pip3 install -r requirements.txt --user
ENV PYTHONUNBUFFERED=1
CMD ["python", "api.py"]
