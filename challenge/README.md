# Wizeline ML Regression Challenge

## 📌 Project Overview:

This project implements a production-ready end-to-end Machine Learning pipeline for a multivariate regression problem.

It includes:

- Model training pipeline
- Experiment tracking with MLflow
- Model persistence
- Batch prediction generation
- App in .EXE for fast execution
- REST API serving with FastAPI
- Streamlit UI for non-technical users
- Docker containerization
- Notebook-based step-by-step exploration

The solution was designed to support both:
- Quick evaluation (non-technical reviewers)
- Technical deep dive (ML engineers)


# 🧠 Architectural Design:

The project follows a modular ML engineering structure:

- api/ → Serving layer
- app_ui/ → UI layer for Serving
- data/ → initial data (CSV)
- model/ → Artifacts
- notebooks/ → Experimentation
- Runs/ → Executables to run the program
- src/ → Core ML logic
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

You have **four different ways** to run and evaluate the solution.

---
---


# 🥇 OPTION 1 — Run the App in .EXE (Easiest Way)

1. Double click: Runs/1-run_app.exe

2. The script will:
   - Open folder to load data to predict (CSV)
   - Generate predictions in "data/" folder called "predictions_method_1.csv"


---


# 🥇 OPTION 2 — Run the App in Your Browser (Using virtual environment)

1. Double click: Runs/2-run_app_navegador.bat

2. The script will:
   - Create a virtual environment (if not exists)
   - Install required dependencies in venv (it could last long time, just wait)
   - Train the model (if not trained)
   - Launch the Streamlit web application

3. Your browser will automatically open: http://localhost:8501


---


# 🥈 OPTION 3 — Run as a Dockerized API Service

⚠️ Requires Docker Desktop installed:
https://www.docker.com/products/docker-desktop


1. Double click: Runs/3-run_app_docker.bat

2. The script will:
   - Check if Docker is installed
   - Build a Docker image
   - Run the FastAPI service

3. Open your browser at: http://localhost:8000/docs

4. In POST /predict or /batch_predict, add feature or features to predict.

5. Press Execute and get the result.


---


# 🥉 OPTION 4 — Technical Deep Dive (Notebook Mode)

Open the project in VSCode or Jupyter and open: Runs/4-full_pipeline_demo.ipynb

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
- Generate predictions in "data/" folder called "predictions_method_4.csv"

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
Senior ML Engineer