FROM python:3
WORKDIR /usr/src/app
COPY dist/ ./
RUN pip install test_bot-0.1.tar.gz
CMD startapp