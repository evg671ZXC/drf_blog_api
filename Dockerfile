FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ENV UV_LINK_MODE=copy \
    UV_SYSTEM_PYTHON=1

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

WORKDIR /app

# TODO: Place entry points in the environment at the front of the path
COPY pyproject.toml .
RUN uv pip install -r pyproject.toml
COPY . /app
RUN uv pip install -e .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh