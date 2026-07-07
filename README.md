<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge">
</div>

<br>

<div align="center">
  <h1>📊 MSP Admin Dashboard</h1>
  <p><strong>Self-Hosted IT Operations Control Plane</strong></p>
  <p>Aggregate auth events, service health, staff records, and adapter integrations — all self-hosted</p>
  <p>
    <a href="#-features">Features</a> •
    <a href="#-quick-start">Quick Start</a> •
    <a href="#-architecture">Architecture</a> •
    <a href="#-adapters">Adapters</a>
  </p>
</div>

---

## 📸 Screenshot

This is a CLI/backend-only tool. No screenshots available.

## ✨ Features

- **Auth Event Tracking** — Monitor authentication events across systems
- **Service Health** — Real-time service status monitoring
- **Staff Records** — Technician and staff management
- **Adapter Integrations** — Email, osTicket, password reset adapters
- **Self-Hosted** — No SaaS dependencies, full data control
- **TimescaleDB** — Time-series optimized PostgreSQL
- **FastAPI Backend** — Modern async Python backend
- **Nginx Reverse Proxy** — Production-grade serving

## 🚀 Quick Start

```bash
git clone https://github.com/OneByJorah/msp-dashboard.git
cd msp-dashboard
cp compose.env.example .env
# Edit .env with your configuration
docker compose up -d
```

Open **http://localhost:8080** in your browser.

## 🏗️ Architecture

```
Browser → Nginx → FastAPI Backend → TimescaleDB
                ↓
         Adapter Layer
         ├── Email (notifications)
         ├── osTicket (ticketing)
         └── Password Reset
```

## 🔌 Adapters

| Adapter | Description |
|---------|-------------|
| **Email** | Email integration for notifications and alerts |
| **osTicket** | Ticket system integration for incident management |
| **Password Reset** | Self-service password reset workflow |

## 📁 Project Structure

```
msp-dashboard/
├── adapters/              # Integration adapters
│   ├── email/             # Email integration
│   ├── osticket/          # osTicket integration
│   └── password-reset/    # Password reset service
├── admin/                 # Admin UI
├── api/                   # FastAPI backend
├── docker-compose.yml     # Docker deployment
└── README.md
```

## 🐳 Docker

```bash
# Start service
docker compose up -d

# View logs
docker compose logs -f

# Stop service
docker compose down
```

## 📄 License

MIT © Jhonattan L. Jimenez

---

<div align="center">
  <p>🖥️ Your MSP operations, self-hosted</p>
  <p><a href="https://github.com/OneByJorah">@OneByJorah</a></p>
</div>
