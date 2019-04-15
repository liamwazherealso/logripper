FROM python:3.7
COPY . .
CMD ["python", "./logripper.py"]
