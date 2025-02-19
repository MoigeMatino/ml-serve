# 🤖MLServe - FastAPI ML Model Deployment
🚧 UNDER ACTIVE DEVELOPMENT 🚧

## 🚀 Overview

This project demonstrates how to **serve a machine learning model** using **FastAPI** and **Docker** into production as a RESTful API using FastAPI. The API allows users to send data and receive stock price predictions using [Prophet](https://facebook.github.io/prophet/) ML model.

## 📌 Features

*   **FastAPI-based REST API** for serving ML predictions.
*   **Dockerized deployment** for easy scalability.
*   **Asynchronous request handling** for efficient inference.
*   **Model versioning and logging** to track performance.
*   **CI/CD integration** (future enhancement) for automated deployments.

## 🏗️ Architecture

1.  **Pretrained ML Model** – A trained model is saved and loaded for inference.
2.  **FastAPI Backend** – Exposes RESTful endpoints for making predictions.
3.  **Docker Containerization** – The application runs inside a container for portability.
4.  **(Optional) Cloud Deployment** – Can be deployed on AWS/GCP/Azure using Kubernetes or serverless functions.

## 🛠️ Installation

### 1️⃣ Clone the repository

    git clone https://github.com/yourusername/fastapi-ml-deploy.git
    cd fastapi-ml-deploy
    

### 2️⃣ Install dependencies

    pip install -r requirements.txt
    

### 3️⃣ Run FastAPI server

    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    

### 4️⃣ Test API

Open your browser and visit:

    http://127.0.0.1:8000/docs
    

## 🐳 Docker Setup

### 1️⃣ Build the Docker image

    docker build -t fastapi-ml-app .
    

### 2️⃣ Run the container

    docker run -p 8000:8000 fastapi-ml-app
    

## 📡 API Endpoints

### 🔹 Root Endpoint

    GET /
    

_Response:_ "Welcome to FastAPI ML Deployment"

### 🔹 Predict

    POST /predict/
    

**Request Body:**

    {
        "feature1": 1.23,
        "feature2": 4.56,
        "feature3": 7.89
    }
    

**Response:**

    {
        "prediction": 0.92
    }
    

## 🧠 Machine Learning Model Details

The model used in this project is a **pretrained scikit-learn model**. It takes input features and returns a numerical prediction. You can replace it with any trained ML model (XGBoost, TensorFlow, PyTorch, etc.).

## 🚀 Future Enhancements

*   ✅ **Deploy on Kubernetes** using Minikube or cloud providers.
*   ✅ **Implement batch predictions** for processing large datasets.
*   ✅ **Add authentication & API rate limiting** for security.
*   ✅ **CI/CD pipeline** to automate testing & deployment.
