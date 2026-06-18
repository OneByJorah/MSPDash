#!/usr/bin/env python3
"""
OsTicket -> MSP Dashboard adapter.

Expected: this runs on the same host as OsTicket or is reachable from it.
Config:
- MSP_API (default http://localhost:42000)
- MSP_INGEST_PATH (default /ingest/service-login)

Env for auth:
- OSTICKET_API_URL
- OSTICKET_API_KEY
- MSP_API (optional)
- MSP_INGEST_PATH (optional)

Behavior:
- /export/export -> login event for ticket thread starter (best-effort)
- Falls back if ticket thread is not a login.
"""
import os, requests
MSP_API=os.getenv("MSP_API","http://localhost:42000")
MSP_INGEST=os.getenv("MSP_INGEST_PATH","/ingest/service-login")

# This is a skeleton. Use the OsTicket API to fetch ticket => map to staff by email.
# Then call MSP.
