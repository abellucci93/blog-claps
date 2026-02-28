FROM python:3.14-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /install

COPY requirements.txt .

RUN apk add --no-cache \
    build-base \
    libffi-dev \
    && pip install --upgrade pip \
    && pip install --prefix=/install/deps --no-cache-dir -r requirements.txt

FROM python:3.14-alpine AS runtime

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

RUN addgroup -S app && adduser -S app -G app
WORKDIR /app

COPY --from=builder /install/deps /usr/local

COPY --link . .
RUN chown -R app:app /app

USER app
EXPOSE 8000


FROM runtime AS development
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

FROM runtime AS production
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
