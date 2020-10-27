FROM python:3.8

LABEL "repository"="https://github.com/AcaGroup/DemocracyBot/"
LABEL "homepage"="https://github.com/AcaGroup/DemocracyBot/"

WORKDIR /DemocracyBot

RUN pip install pipenv
COPY . .
RUN pipenv install --system --deply

# Run tests
RUN python ./test/run_tests.py

# Application entrypoint
CMD [ "python", "main.py" ]