# MSP Admin Dashboard — IT Operations Visibility

Local-only admin dashboard to track staff activity across helpdesk, password reset, email, and future services. Private view for you; built at enterprise MSP quality.

- Stack: Ubuntu/Docker + FastAPI + Admin UI + Time-series DB + Telegram alerts
- Ports: isolated from existing stack (IT System on 8080/9000/6333/11434)
- Privacy: admin-only auth, no public endpoints

## Quick start

```bash
git clone https://github.com/OneByJorah/msp-dashboard.git
cd msp-dashboard
cp compose.env.example .env
make deploy
open http://localhost:3000
```

## Docs

- `docs/ARCHITECTURE.md`
- `docs/DEPLOY.md`
- `docs/DATA_MODEL.md`
- `ops/runbook.md`
