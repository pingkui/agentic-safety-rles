FROM python:3.12-slim
RUN pip install --no-cache-dir "pytest>=8,<9" trustme
RUN useradd -m -u 1000 agent
COPY workspace /workspace
COPY make_certs.py /tmp/make_certs.py
RUN mkdir -p /workspace/certs && python /tmp/make_certs.py && rm /tmp/make_certs.py \
 && chown -R agent:agent /workspace
COPY verifier /verifier
RUN chown -R root:root /verifier && chmod -R go-rwx /verifier
USER agent
WORKDIR /workspace
