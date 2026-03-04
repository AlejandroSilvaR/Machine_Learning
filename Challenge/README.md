# Wizeline ML Regression Challenge

## 📌 Project Overview:

This project implements a production-ready end-to-end Machine Learning pipeline for a multivariate regression problem.

It includes:

- Model training pipeline
- Experiment tracking with MLflow
- Model persistence
- Batch prediction generation
- REST API serving with FastAPI
- Streamlit UI for non-technical users
- Docker containerization
- Notebook-based step-by-step exploration

The solution was designed to support both:
- Quick evaluation (non-technical reviewers)
- Technical deep dive (ML engineers)


# 🧠 Architectural Design:

The project follows a modular ML engineering structure:

- src/ → Core ML logic
- api/ → Serving layer
- app_ui/ → UI layer
- notebooks/ → Experimentation
- model/ → Artifacts
- mlruns/ → Experiment tracking
- Dockerfile → Containerization

This separation ensures:

- Reproducibility
- Scalability
- Maintainability
- Production readiness


---
---

# 🚀 HOW TO RUN THE PROJECT

You have **three different ways** to run and evaluate the solution.

---
---


# 🥇 OPTION 1 — Run the App in Your Browser (Easiest Way)

1. Double click: run_app_navegador.bat

2. The script will:
   - Create a virtual environment (if not exists)
   - Install required dependencies
   - Train the model (if not trained)
   - Launch the Streamlit web application

3. Your browser will automatically open: http://localhost:8501


---


# 🥈 OPTION 2 — Run as a Dockerized API Service

### 👉 Recommended for production-like evaluation

⚠️ Requires Docker Desktop installed:
https://www.docker.com/products/docker-desktop


1. Double click: run_app_docker.bat

2. The script will:
   - Check if Docker is installed
   - Build a Docker image
   - Run the FastAPI service

3. Open your browser at: http://localhost:8000/docs


---


# 🥉 OPTION 3 — Technical Deep Dive (Notebook Mode)

### 👉 Recommended for ML Engineers

Open the project in VSCode or Jupyter and open: notebooks/full_pipeline_demo.ipynb


## Notebook Walkthrough:

The notebook demonstrates:

### 1️⃣ Data Loading
- Loads training dataset
- Displays dataset structure

---

### 2️⃣ Model Training
- Splits data
- Trains model using configuration
- Displays metrics:
  - RMSE
  - R2
  - Cross-validation RMSE

---

### 3️⃣ MLflow Logging
- Logs experiment
- Logs parameters
- Logs metrics
- Registers model artifact

You can optionally run: mlflow ui
And open:http://localhost:5000

---

### 4️⃣ Blind Test Prediction
- Loads blind test dataset
- Generates predictions
- Saves predictions.csv
- File saved in `/data`

---

### 5️⃣ API Simulation
- Loads saved model
- Simulates prediction request
- Shows prediction output


---
---
---


# 👨‍💻 Author:
Alejandro Silva  
Mid-Senior ML Engineer Candidate
