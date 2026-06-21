# MSP Dashboard (msp-dashboard)

**Version:** v0.1  
**Status:** Active Development  
**Repository:** https://github.com/OneByJorah/msp-dashboard

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Features](#features)
- [Getting Started](#getting-started)
- [Service Management](#service-management)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Overview

Managed Service Provider admin dashboard with staff management and reporting.

---

## Architecture

Client → Local service (`msp-dashboard`) → data/processing modules → output/api layer.
Secrets and environment configuration are managed via environment files with restrictive permissions.

---

## Technology Stack

|| Layer | Stack |
|---|---|
| Runtime | Linux (Ubuntu 22.04+) |
| Primary Stack | React / FastAPI |
| VCS | Git + GitHub (`github.com/OneByJorah/msp-dashboard`) |
| Dev Port | Localhost / systemd service |

---

## Features

- Operational dashboard and monitoring (per repo).
- Exportable data / reports where supported.
- Extensible service-based design.
- Dark-themed UI where applicable.

---

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/OneByJorah/msp-dashboard.git
cd msp-dashboard

# 2. Install dependencies
# (see specific subproject docs)

# 3. Start the service
# (see Service Management below)
```

---

## Service Management

```bash
# Start the service (example)
sudo systemctl start msp-dashboard.service
sudo systemctl enable msp-dashboard.service
```

Access the service via your configured localhost port or reverse proxy.

---

## Project Structure

```
msp-dashboard/
├── README.md
├── (additional project files)
```

---

## Screenshots

All screenshots are live captures from the local dev instance.

_(Screenshots will be added after build/run capture.)_

---

## Contributing

1. Create a feature branch off `main`.
2. Follow the existing code style.
3. Submit a PR with description and screenshots for UI changes.

---

## License

MIT

---

## Author

Built by **Jhonattan L. Jimenez**.
