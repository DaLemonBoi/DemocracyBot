FROM python:3.8

LABEL "repository"="https://github.com/AcaGroup/DemocracyBot/"
LABEL "homepage"="https://github.com/AcaGroup/DemocracyBot/"

WORKDIR /DemocracyBot

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run tests
RUN python3 ./test/run_tests.py

# Application entrypoint
CMD [ "python3", "-u", "./src/main.py" ]