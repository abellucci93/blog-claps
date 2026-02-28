# Blog Clap

**Blog Clap** is a lightweight microservice that enables users to "clap" for blog posts - similar to reactions on modern publishing platforms. It is built with **Python 3.14**, powered by **FastAPI**, and uses **Redis** as its primary data store.

## Table of contents

* [Overview](#overview)
* [Requirements](#requirements)
* [Installation](#installation)
* [Running with Docker Compose](#running-with-docker-compose)
* [Testing](#testing)

## Overview

Blog Clap is a simple and scalable microservice designed to:

* Add claps to a blog post
* Retrieve total claps for a post
* Support high-performance, low-latency reactions
* Be containerized and cloud-ready

This service is ideal for integration into blog platforms or content management systems that need lightweight engagement tracking.

## Requirements

* Python 3.14
* Docker
* Redis (if running locally without Docker)

## Architecture

The Blog Clap microservice is built using:

* Python 3.14
* FastAPI - high-performance ASGI framework
* Redis - in-memory key-value store used as the primary data storage

## Installation

1. Clone the repository

```sh
git clone https://github.com/your-org/blog-clap.git
cd blog-clap
```

2. Create a virtual environment

```sh
python3.14 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```sh
pip install -r requirements.txt
```

4. Run the application

```sh
uvicorn app.main:app --reload
```

The service will be available at: `http://localhost:8000`

Swagger documentation: `http://localhost:8000/docs`

## Running with Docker Compose

The recommended way to run Blog Clap is with Docker Compose, which orchestrates both the API service and Redis.

### Start the services

```sh
docker compose up -d
```

### Stop the services

```sh
docker compose down
```

## Testing

Blog Clap uses:

* pytest for unit and integration testing
* TestContainers for ephemeral Redis instances during integration tests

### Run tests locally

```sh
pytest
```

### Testing strategy

* Unit tests for API logic
* Integration tests with real Redis (via TestContainers)
* Isolated, reproducible test environments

