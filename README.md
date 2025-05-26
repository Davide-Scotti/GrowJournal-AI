# GrowJournal AI

> The ultimate AI-powered Grow Journal — from seed to harvest, personalized guidance at every step.

---

## 📖 Table of Contents

1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Technology Stack](#technology-stack)
4. [Getting Started](#getting-started)
5. [Project Structure](#project-structure)
6. [API Endpoints](#api-endpoints)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

---

## Overview

**GrowJournal AI** is a Progressive Web App (PWA) designed for cannabis cultivators of all levels. It automates your grow journal, tracks every key event, and—powered by embedded AI—delivers timely, data-driven cultivation advice tailored to your strain, environment, and growth phase.

## Key Features

*Automated Grow Logs*
Record germination, transplant, irrigation, flowering, flush, and harvest events with dates, notes, and photos.

*Smart Reminders & Notifications*
Custom alerts for watering, feeding, pruning, pH checks, and more based on your personalized schedule.

*AI Grower Assistant*

* Rule-based advice for temperature, pH, lighting, and nutrient management
* Machine-learning suggestions derived from your historical grow data
* Future vision: computer vision diagnostics for leaf health, nutrient deficiencies, and pests.

*Strain Database & Guides*
In-app reference for hundreds of strains: genetics, flowering time, expected yield, terpene and cannabinoid profiles.

*Interactive Dashboard*
Visualize growth curves, EC/pH trends, and yield projections in real time.

*Export & Share*
Generate PDF/CSV reports or publish a public grow-diary for community feedback.

---

## Technology Stack

### Frontend

* React (Create React App)
* Tailwind CSS
* React Router
* react-hook-form

### Backend

* Node.js, Express
* MongoDB with Mongoose
* JWT Authentication
* Python (Flask/FastAPI) for AI microservices

### DevOps & Hosting

* Frontend: Vercel or Netlify
* Backend: Render or Heroku
* CI/CD: GitHub Actions
* Containerization (future): Docker

---

## Getting Started

1. **Clone the repository**

   ```bash
   git clone git@github.com:<your-org>/GrowJournal-AI.git
   cd GrowJournal-AI
   ```
2. **Install dependencies**

   ```bash
   # Frontend
   cd web && npm install

   # Backend
   cd ../api && npm install
   ```
3. **Configure environment variables**
   Create a `.env` file in both `/web` and `/api` directories with:

   ```ini
   MONGO_URI=your_mongo_connection_string
   JWT_SECRET=your_jwt_secret
   AI_SERVICE_URL=http://localhost:5000
   ```
4. **Run in development**

   ```bash
   # Backend
   cd api && npm run dev

   # Frontend
   cd ../web && npm start
   ```
5. **Build for production**

   ```bash
   # Frontend
   cd web && npm run build

   # Backend
   cd api && npm run build
   ```

---

## Project Structure

```
GrowJournal-AI/
├── web/    # React PWA client
│   ├── public/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── api/
│       └── utils/
└── api/    # Node.js + Express server
    ├── controllers/
    ├── models/
    ├── routes/
    └── utils/
```

---

## API Endpoints

* `POST /api/users/register` — Register a new user
* `POST /api/users/login` — Authenticate and receive a JWT
* `GET  /api/growlogs` — List all grow logs for the authenticated user
* `POST /api/growlogs` — Create a new grow log
* `GET  /api/growlogs/:id` — Retrieve details of a specific grow log
* `POST /api/growlogs/:id/events` — Add an event (e.g., watering, nutrient feed)
* `GET  /api/advice/:id` — Fetch AI-driven cultivation advice for a grow log

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeatureName`
3. Commit your changes with clear messages
4. Push to your branch & open a pull request

Please read the [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## Contact

**Lead Developer:** Your Name — [your.email@example.com](mailto:your.email@example.com)
**GitHub Issues:** Use this repo’s Issues tab for bug reports and feature requests.

Let’s build the future of smart cultivation together! 🌱🤖
