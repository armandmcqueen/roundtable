FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

RUN apt-get update  \
    && apt-get install -y python3.11  \
    python3.11-distutils  \
    python3.11-venv \
    python3.11-dev \
    redis-server  \
    curl \
    gcc \
    sudo \
    make \
    git



COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Install pip
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

# Make Python 3.11 the default Python
RUN ln -s /usr/bin/python3.11 /usr/bin/python

# Copy the monorepo into the container
COPY . /app
WORKDIR /app

# Install the monorepo
RUN uv sync


# Streamlit port
EXPOSE 8501