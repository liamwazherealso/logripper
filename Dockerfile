FROM python:3.6
RUN adduser logripper root
RUN chmod -R 775 /home/logripper/app
RUN chown -R logripper:root /home/logripper/app
USER 1000
WORKDIR /home/logripper/app
COPY . .
RUN pip install --user pipenv && pipenv install
CMD ["pipenv", "run", "python", "./logripper.py"]
