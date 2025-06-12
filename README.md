# 🏋️‍♂️ AI Gym Personal Trainer App

[![Build](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/vedantt-22/ai-gym-trainer-app/actions)  
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Platform](https://img.shields.io/badge/platform-android%20%7C%20ios-lightgrey)](https://expo.dev/)

An AI-powered personal fitness trainer that provides **real-time posture correction**, **form validation**, and **custom workout plans** using pose detection and ML-based recommendations. Built with **React Native**, **TensorFlow.js**, and **Flask API**.

---

## 📚 Table of Contents

- [🚀 Features](#-features)  
- [🛠️ Tech Stack](#️-tech-stack)  
- [⚙️ Getting Started](#-getting-started)  
- [📦 Deployment](#-deployment)  
- [🖼️ Screenshots](#️-screenshots)  
- [🔮 Future Enhancements](#-future-enhancements)  
- [🤝 Contributing](#-contributing)  
- [📝 License](#-license)  

---

## 🚀 Features

- 🎥 **Real-time Pose Detection** with TensorFlow.js (MoveNet)
- 🎯 **AI-driven Form Validation** to correct posture on the fly
- 🧠 **ML-Based Workout Plan Generator** using user stats and goals
- 📊 **Analytics Dashboard** for tracking workout duration, consistency, and intensity
- 🔄 **Session History & Feedback Loop** for personalized improvements

---

## 🛠️ Tech Stack

| Layer        | Technologies                                 |
|--------------|----------------------------------------------|
| **Frontend** | React Native, Expo, TailwindCSS              |
| **AI/ML**    | TensorFlow.js, MoveNet, Flask + Python       |
| **Backend**  | Flask REST API, FastAPI (optional), SQLite   |
| **Database** | Firebase or MongoDB (optional)               |
| **Deployment**| Expo for Android/iOS, Flask on Render       |

---

## ⚙️ Getting Started

### 🧩 Prerequisites
- Node.js, npm or yarn
- Expo CLI (`npm install -g expo-cli`)
- Python 3.x for backend API

### 📱 App Setup

```bash
# Clone the repo
git clone https://github.com/vedantt-22/ai-gym-trainer-app.git
cd ai-gym-trainer-app

# Install dependencies
npm install
# or
yarn install

# Start the development server
npm start
````

### 🧠 Backend Setup

```bash
# Move to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install Flask & requirements
pip install -r requirements.txt

# Run the API server
python app.py
```

API will be available at `http://localhost:5000`

---

## 📦 Deployment

* **Mobile App**: Use Expo for live preview or publish via Play Store / App Store
* **Backend**: Deploy Flask API on Render, Railway, or AWS (Lambda + API Gateway for serverless)

---

## 🖼️ Screenshots

> *(Include screenshots or screen recordings showing pose detection, real-time feedback, and dashboard UI)*

---

## 🔮 Future Enhancements

* 🗣️ Voice assistant integration for guided sessions
* 🍽️ Diet planner & caloric analysis using LLMs
* ⌚ Integration with fitness trackers and wearables
* 🧠 AI coach for long-term progress adaptation

---

## 🤝 Contributing

Want to improve this project? Contributions are welcome!
Fork the repo, create a branch, make changes, and open a Pull Request.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

**Made with 💪 by [Vedant Karekar](https://github.com/vedantt-22)**

```
