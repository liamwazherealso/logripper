FROM python:3.6
COPY . .
RUN pip install pipenv && pipenv install
CMD ["pipenv", "run", "python", "./logripper.py"]
