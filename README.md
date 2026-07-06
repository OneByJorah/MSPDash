<!-- j1-brand:v2 -->
<div align="center">

# MSP Dashboard

A self-hosted IT operations control plane — authentication event tracking, service health monitoring, staff records, and adapter-based integrations.

[![GitHub](https://img.shields.io/badge/github-OneByJorah%2Fmsp--dashboard-FFB300?style=for-the-badge&labelColor=0d0d0c)](https://github.com/OneByJorah/msp-dashboard)
[![License](https://img.shields.io/badge/license-MIT-FFB300?style=for-the-badge&labelColor=0d0d0c)](LICENSE)
[![Language](https://img.shields.io/badge/Python-FFB300?style=for-the-badge&labelColor=0d0d0c)](https://python.org)
[![Built by](https://img.shields.io/badge/built%20by-JorahOne%20LLC-FFB300?style=for-the-badge&labelColor=0d0d0c)](https://github.com/OneByJorah)

</div>

---

## Why This Exists

MSPs juggle multiple clients, each with their own authentication events, service health, and staff access. The MSP Dashboard pulls it all into one place — real-time service monitoring, Auth event feeds, ticketing adapters, and self-service password resets — on a FastAPI + TimescaleDB stack deployed with Docker Compose.

## Key Features

| Feature | Why It Matters |
|---|---|
| Real-time service monitoring | See client service health at a glance |
| Auth event tracking | Monitor login attempts, failures, and suspicious patterns |
| Adapter-based integrations | Email, osTicket, self-service password resets — plug in what you need |
| PostgreSQL + TimescaleDB | Time-series optimized for event data at scale |
| Nginx reverse proxy | Production-ready TLS termination out of the box |

## Quick Start

```bash
git clone https://github.com/OneByJorah/msp-dashboard.git
cd msp-dashboard
cp compose.env.example .env   # configure database, integrations, etc.
docker compose up -d
```

## Architecture

```
┌──────────┐     ┌──────────┐     ┌──────────────┐
│  Browser  │────▶│  Nginx   │────▶│  FastAPI      │
│  (HTTPS)  │     │  Proxy   │     │  Backend      │
└──────────┘     └──────────┘     └──────┬───────┘
                                          │
                              ┌───────────┼───────────┐
                              ▼           ▼           ▼
                       ┌──────────┐ ┌──────────┐ ┌──────────┐
                       │TimescaleDB│ │ Adapters │ │  Admin   │
                       │(Postgres) │ │ Email    │ │  Panel   │
                       └──────────┘ │ osTicket │ └──────────┘
                                    │ SSPR     │
                                    └──────────┘
```

## Documentation

| Doc | Description |
|---|---|
| [Setup Guide](docs/setup.md) | Configuration and deployment walkthrough |
| [Adapter Configuration](docs/adapters.md) | Connecting email, osTicket, and SSPR |

---

## License

MIT © JorahOne, LLC — see [LICENSE](LICENSE)

<sub>Part of the JorahOne infrastructure ecosystem.</sub>
