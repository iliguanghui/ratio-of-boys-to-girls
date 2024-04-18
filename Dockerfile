FROM python:3.12-bookworm
WORKDIR /app
COPY ./ ./
CMD ["/usr/local/bin/python3", "main.py"]