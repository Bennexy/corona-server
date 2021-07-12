FROM ubuntu:20.04 AS builder-image


ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
RUN python3 -m venv /app/venv
ENV PATH = "/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel
RUN pip3 install --no-cache-dir -r requirements.txt

FROM ubuntu:20.04 AS runner-image
RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3-venv && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder-image /app/venv /app/venv

RUN mkdir /app/code
WORKDIR /app/code
COPY . .
RUN chmod 777 .*

EXPOSE 8080

ENV PYTHONUNBUFFERED=1

# activate virtual environment
ENV VIRTUAL_ENV=/app/venv
ENV PATH="/app/venv/bin:$PATH"

CMD ["gunicorn","-b", "0.0.0.0:8080", "-w", "4", "-k", "gevent", "--worker-tmp-dir", "/dev/shm", "server:app"]

