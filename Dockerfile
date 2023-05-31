FROM python:3.9.15-slim
LABEL Name="PDFChat"

LABEL Description="Chat with any pdf"
LABEL Version="python==3.9.15"

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install ffmpeg -y \
    && apt install software-properties-common -y \
    && apt-get install build-essential -y \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
COPY app app

RUN python3 -m pip install --no-cache-dir -r /requirements.txt

WORKDIR app
ENTRYPOINT ["python3", "main.py"]
