FROM riversafe/eze-cli:latest
WORKDIR /data
COPY . .
USER ezeuser
ENTRYPOINT [ "eze", "test" ]