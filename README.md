# MSP Admin Dashboard

**Local-only IT operations visibility with auth event tracking, service health, staff inventory, and adapter integrations.**

![License](https://img.shields.io/badge/License-MIT-FFB300.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active_Development-FFB300.svg?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Python-FFB300.svg?style=for-the-badge)
![Stack](https://img.shields.io/badge/Stack-Docker_FastAPI_TimescaleDB-FFB300.svg?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux-FFB300.svg?style=for-the-badge)

MSP Admin Dashboard provides local-only IT operations visibility through a Nginx-served HTML UI backed by FastAPI and TimescaleDB. It aggregates auth events, service health, staff records, and adapter integrations for email, osTicket, and password resets. Designed for MSP and internal IT teams who require self-hosted control planes without SaaS dependencies.

- Single `docker compose up -d` deployment.
- Time-series auth event storage via TimescaleDB.
- Adapter-driven extensibility for email, ticketing, and identity flows.
- Local-only access with no outbound SaaS dependencies.
- Static frontend served through Nginx for minimal attack surface.

- Deploy the full stack with `make deploy` or `docker compose up -d`.
- Track auth events, MFA status, and service access logs in TimescaleDB.
- Inspect staff and service inventory from the admin UI.
- Extend behavior through adapters for email, osTicket, and password reset.
- Persist metrics, events, and staff records in TimescaleDB for retention and query.

```
Client browser → Nginx (3000) → FastAPI (42000) → TimescaleDB (5433)
                                            ├── Email adapter
                                            ├── osTicket adapter
                                            └── Password reset adapter
```

### Technology Stack

- **Runtime**: Docker Compose
- **Frontend**: HTML5 / Nginx (hello image + custom admin UI)
- **Backend**: Python / FastAPI / Uvicorn
- **Database**: TimescaleDB / PostgreSQL 16
- **ORM**: SQLAlchemy
- **Adapters**: Python modules for email, osTicket, password reset
- **VCS**: Git + GitHub

### Quickstart

1. Clone the repository.
   ```bash
   git clone https://github.com/OneByJorah/msp-dashboard.git
   cd msp-dashboard
   ```
2. Copy the environment template.
   ```bash
   cp compose.env.example .env
   # Edit .env with DATABASE_URL, SECRET_KEY, and database credentials.
   ```
3. Start the stack.
   ```bash
   make deploy
   ```
4. Verify the admin UI at `http://localhost:3000`.

### Configuration

All configuration lives in `.env` (never committed). See `compose.env.example` for documented placeholders.

| Variable | Purpose | Default |
|---|---|---|
| `DASHBOARD_PORT` | Nginx dashboard port | `3000` |
| `API_PORT` | FastAPI backend port | `42000` |
| `DATABASE_URL` | Database connection string | *(none)* |
| `SECRET_KEY` | FastAPI secret key | *(none)* |
| `POSTGRES_USER` | TimescaleDB username | *(none)* |
| `POSTGRES_PASSWORD` | TimescaleDB password | *(none)* |
| `POSTGRES_DB` | TimescaleDB database name | *(none)* |

### Roadmap

- [ ] Add LDAP / AD sync adapter
- [ ] Implement RBAC for admin UI
- [ ] Export auth events to SIEM formats (CEF / LEEF)
- [ ] Add automated snapshot and restore workflows

### License

MIT © JorahOne, LLC

---

*Built by [JorahOne, LLC](https://github.com/JorahOne-Services) — network security, AD/M365, and infrastructure automation for SMBs and public sector.*
