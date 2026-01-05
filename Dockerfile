FROM python:3.12-slim-bookworm AS build
WORKDIR /app

FROM gcr.io/distroless/python3-debian12
COPY api.py /app/
WORKDIR /app

# Use the pre-existing unprivileged user
USER nonroot
EXPOSE 8080
ENTRYPOINT ["/usr/bin/python3", "api.py"]