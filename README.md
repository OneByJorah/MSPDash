# MSP Admin Dashboard — IT Operations Visibility

**Version:** v1.0  
**Status:** Active Development  
**Repository:** https://github.com/OneByJorah/msp-dashboard

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Features](#features)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Service Management](#service-management)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Overview

MSP Admin Dashboard is a local-only admin dashboard for IT operations visibility. It aggregates auth events, service health, staff records, and adapter integrations (email, osTicket, password reset) into a single control plane backed by TimescaleDB.

Designed for MSP and internal IT teams who want self-hosted visibility without SaaS dependencies.

---

## Architecture

Client browser → Nginx (`nginxdemos/hello` image, port `3000`) → FastAPI backend (`api/app.py`, port `42000`) → TimescaleDB (`5433:5432`) → adapters (email, osTicket, password reset).

Data model:
- `admin_users`, `services`, `staff`, `auth_events`

---

## Technology Stack

| Layer | Stack |
|---|---|
| Runtime | Docker Compose |
| Frontend | Static HTML (Nginx hello image + `admin/index.html`) |
| Backend | Python / FastAPI / Uvicorn |
| Database | TimescaleDB / PostgreSQL 16 |
| ORM | SQLAlchemy |
| VCS | Git + GitHub (`github.com/OneByJorah/msp-dashboard`) |

---

## Features

- **Admin UI**: local-only dashboard at `http://localhost:3000`.
- **Auth event tracking**: login, MFA, and service access logs.
- **Staff + service inventory**: structured staff and service records.
- **Adapter integrations**:
  - Email adapter (`adapters/email/adapter.py`)
  - osTicket adapter (`adapters/osticket/adapter.py`)
  - Password reset adapter (`adapters/password-reset/adapter.py`)
- **Time-series ready**: TimescaleDB storage for events and metrics.

---

## Getting Started

```bash
# 1. Clone
git clone https://github.com/OneByJorah/msp-dashboard.git
cd msp-dashboard

# 2. Environment
cp compose.env.example .env

# 3. Deploy
make deploy
# or
docker compose up -d

# 4. Open admin UI
open http://localhost:3000
```

---

## Environment Variables

Configure via `.env` (see `compose.env.example`):

| Variable | Purpose |
|---|---|
| `DASHBOARD_PORT` | Nginx dashboard port (default `3000`) |
| `API_PORT` | FastAPI backend port (default `42000`) |
| `DATABASE_URL` | Database connection string |
| `SECRET_KEY` | FastAPI secret |
| `POSTGRES_USER` / `POSTGRES_PASSWORD` / `POSTGRES_DB` | TimescaleDB settings |

Keep `.env` out of VCS.

---

## Service Management

```bash
# Start
docker compose up -d

# View logs
docker compose logs -f msp-api

# Stop
docker compose down
```

---

## Project Structure

```
msp-dashboard/
├── admin/
│   └── index.html               # Local admin UI
├── api/
│   ├── app.py                   # FastAPI backend
│   ├── Dockerfile
│   └── requirements.txt
├── adapters/
│   ├── email/adapter.py
│   ├── osticket/adapter.py
│   └── password-reset/adapter.py
├── docker-compose.yml
├── compose.env.example
├── Makefile
└── README.md
```

---

## Screenshots

_(Screenshots will be added after build/run capture.)_

---

## Contributing

1. Create a feature branch off `main`.
2. Test adapter integrations locally before submitting.
3. Submit a PR with description and screenshots for UI changes.

---

## License

MIT

---

## Author

Built by **Jhonattan L. Jimenez**.
