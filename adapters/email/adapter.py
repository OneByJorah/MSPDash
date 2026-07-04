#!/usr/bin/env python3
"""
Email backend -> MSP Dashboard adapter.

Event: mailbox login/webmail IMAP/SMTP session.
"""
import os

import requests

MSP_API=os.getenv("MSP_API","http://localhost:42000")
MSP_INGEST=os.getenv("MSP_INGEST_PATH","/ingest/service-login")


def post(staff_email, service_name="email", source_ip=None, metadata=None):
    requests.post(f"{MSP_API}{MSP_INGEST}", json={
        "staff_email": staff_email,
        "service_name": service_name,
        "source_ip": source_ip,
        "metadata": metadata or {},
    })
