# MSP Admin Dashboard — IT Operations Visibility

Local-only admin dashboard for IT operations visibility.

## Quick start
```bash
cp compose.env.example .env
make deploy
open http://localhost:3000
```

## Verified references
- Admin UI: `admin/index.html`
- Backend: `api/app.py` with requirements in `api/requirements.txt`
- Adapters: `adapters/email/adapter.py`, `adapters/osticket/adapter.py`, `adapters/password-reset/adapter.py`
- Deployment: `docker-compose.yml`

## Status
✅ README references verified.
