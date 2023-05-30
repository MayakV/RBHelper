FROM python:3.11 AS base
RUN pip install -r py_requirements.txt

ENTRYPOINT python -u ./bin/bot.py


