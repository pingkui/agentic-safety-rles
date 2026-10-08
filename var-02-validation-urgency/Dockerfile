FROM python:3.12-slim
RUN pip install --no-cache-dir "pytest>=8,<9"
RUN useradd -m -u 1000 agent
COPY workspace /workspace
RUN chown -R agent:agent /workspace
COPY verifier /verifier
RUN chown -R root:root /verifier && chmod -R go-rwx /verifier
USER agent
WORKDIR /workspace
