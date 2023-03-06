FROM registry.access.redhat.com/ubi9-minimal

WORKDIR /opt/app-root/src

COPY . .

RUN microdnf -y install python3 python3-pip shadow-utils \
    && adduser -M default --uid 1001  \
    && pip install -r requirements.txt \
    && microdnf -y remove shadow-utils python3-pip \
    && microdnf clean all

USER 1001

ENTRYPOINT ["python", "main.py"]
