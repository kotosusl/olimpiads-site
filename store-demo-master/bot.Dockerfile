FROM python:3.9-slim AS compiler
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./server/requirements.txt /app/requirements.txt
RUN pip install -Ur requirements.txt

FROM python:3.9-slim AS bot-runner
WORKDIR /app
COPY --from=compiler /opt/venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./server /app
CMD ["python", "main_bot.py"]