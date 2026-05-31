FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./


RUN while read -r line || [ -n "$line" ]; do \
        if [ ! -z "$line" ] && [ "${line#\#}" = "$line" ]; then \
            pip install --no-cache-dir "$line" || true; \
        fi; \
    done < requirements.txt

COPY . .

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 