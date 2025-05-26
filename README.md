# GrowJournal AI

> Smart Grow Journal web app with AI‑driven, personalized cultivation advice.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license)  

---

## 📖 Table of Contents

1. [🚀 Project Overview](#-project-overview)  
2. [✨ Key Features](#-key-features)  
3. [🛠 Tech Stack & Architecture](#-tech-stack--architecture)  
4. [⚙️ Installation & Setup](#️-installation--setup)  
5. [📂 Project Structure](#-project-structure)  
6. [🤝 Contributing](#-contributing)  
7. [📄 License](#-license)  
8. [👤 Contact & Support](#-contact--support)  

---

## 🚀 Project Overview

**GrowJournal AI** is a Progressive Web App (PWA) designed for cannabis cultivators of every level. It automates your grow journal, tracks every key event, and—powered by embedded AI—delivers timely, scientific cultivation advice tailored to your environment, strain and growth phase.

---

## ✨ Key Features

- **Automated Grow Logs**  
  Record germination, transplant, irrigation, flowering, flush, harvest—with date, notes and photos.  
- **Smart Reminders & Notifications**  
  Schedule custom alerts for watering, feeding, pruning, flush and more.  
- **AI Grower Assistant**  
  - **Rule‑based** advice for ideal temperature, pH, nutrient timing  
  - **Machine Learning** suggestions from your historical grow data  
  - **Computer Vision (future)** to diagnose leaf issues and mold from photos  
- **Strain Database & Guides**  
  In‑app reference for hundreds of strains: genetics, flowering time, typical yields, terpene profiles.  
- **Interactive Dashboard**  
  Visualize growth curves, EC/pH trends, and yield projections.  
- **Export & Share**  
  Generate PDF/CSV reports or publish a “grow diary” to your community.  

---

## 🛠 Tech Stack & Architecture

### Frontend  
- **Framework:** React (Create React App)  
- **Styling:** Tailwind CSS  
- **Routing & State:** react-router, React Context / Zustand  
- **Forms & Validation:** react-hook-form  

### Backend  
- **Runtime:** Node.js, Express  
- **Database:** MongoDB (Mongoose)  
- **Auth:** JWT (JSON Web Tokens)  
- **AI/ML Services:** Python microservices (Flask / FastAPI) for predictive advice & image analysis  

### DevOps & Hosting  
- **Frontend Hosting:** Vercel / Netlify  
- **API Hosting:** Render / Heroku / AWS Elastic Beanstalk  
- **CI/CD:** GitHub Actions  
- **Containerization (future):** Docker  

---

## ⚙️ Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone git@github.com:<your-org>/GrowJournal-AI.git
   cd GrowJournal-AI
