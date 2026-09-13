<div align="center">

![MSPDash banner](docs/assets/banner.svg)

# MSPDash

**Self-hosted IT ops dashboard for MSPs** — auth events, service health, staff records, and adapter integrations.

[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776ab?logo=python&logoColor=fff)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?logo=fastapi&logoColor=fff)](https://fastapi.tiangolo.com)
[![TimescaleDB](https://img.shields.io/badge/TimescaleDB-Time--Series-fdb515?logo=postgresql&logoColor=fff)](https://timescale.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=fff)](https://docker.com)

</div>

---

## What It Does

MSPDash is a **unified IT operations dashboard** built for Managed Service Providers. It aggregates authentication events, service health checks, staff records, and adapter integrations into a single self-hosted interface.

## Quick Start

```bash
git clone https://github.com/OneByJorah/MSPDash.git
cd MSPDash
cp compose.env.example .env
docker compose up -d
```

Open **http://localhost:3000**

## Features

- **Auth Event Tracking** — Monitor authentication events across all systems
- **Service Health** — Real-time service status with uptime monitoring
- **Staff Records** — Technician and staff management
- **Adapter Integrations** — Email, osTicket, and password reset adapters
- **Time-Series Data** — TimescaleDB for efficient historical event storage
- **FastAPI Backend** — Modern async Python API
- **Docker Ready** — One-command deployment with health checks

## Architecture

```
Browser → Nginx :3000 → FastAPI :42000 → TimescaleDB
                              ↓
                        Adapter Layer
                        ├── Email
                        ├── osTicket
                        └── Password Reset
```

## Adapters

| Adapter | Description |
|---------|-------------|
| **Email** | Email notifications and alerts |
| **osTicket** | Ticket system integration |
| **Password Reset** | Self-service password reset |

## Use Cases

1. **MSPs** — Unified view of client infrastructure health
2. **IT Departments** — Staff management and auth event auditing
3. **Helpdesks** — Ticket-to-alert workflows with osTicket

## License

MIT © Jhonattan L. Jimenez (OneByJorah)

---

<p align="center">Built with 🌴 by <a href="https://github.com/OneByJorah">OneByJorah</a> · <a href="https://jorahone.com">jorahone.com</a></p>
