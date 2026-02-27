# 🎓 Student Performance Prediction – End to End MLOps Project

## 📌 Project Overview

This project is an end to end Machine Learning pipeline that predicts student performance using multiple regression models.  

It includes:

- Data Ingestion
- Data Transformation
- Model Training
- Model Selection
- Model Serialization
- Dockerization
- CI CD Pipeline using GitHub Actions
- AWS ECR Integration
- Deployment on AWS EC2

This project demonstrates a complete real world MLOps workflow.

---

## 🧠 Machine Learning Pipeline

### 1️⃣ Data Ingestion
- Load dataset
- Split into train and test
- Save raw and processed data inside artifacts folder

### 2️⃣ Data Transformation
- Handle missing values
- Feature scaling
- Encoding categorical variables
- Create preprocessing pipeline
- Save preprocessor object

### 3️⃣ Model Training

Multiple regression models are trained:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

Each model is:

- Trained on training data
- Evaluated using R2 score
- Compared to select best performing model

Best model is saved as: artifacts/model.pkl


---

## 🐳 Docker Setup

The application is containerized using Docker.

### Dockerfile Structure

- Python base image
- Copy project files
- Install dependencies
- Expose application port
- Run application

To build locally:
docker build -t studentperformance .
docker run -p 8080:8080 studentperformance

---

## ☁ AWS Deployment Architecture

### Services Used

- AWS IAM
- AWS Elastic Container Registry ECR
- AWS EC2
- GitHub Actions

### Deployment Flow

1. Code pushed to GitHub
2. GitHub Actions builds Docker image
3. Image pushed to AWS ECR
4. EC2 self hosted runner pulls latest image
5. Docker container runs application

---

## 🔄 CI CD Pipeline

Workflow file located at: .github/workflows/main.yaml


Pipeline Stages:

### Continuous Integration
- Code checkout
- Lint check
- Unit test execution

### Continuous Delivery
- Docker build
- ECR login
- Push image to ECR

### Continuous Deployment
- EC2 self hosted runner
- Pull latest image
- Stop old container
- Start new container
- Clean unused docker layers

---

## 🖥 EC2 Setup Commands
sudo apt-get update -y
sudo apt-get upgrade -y

curl -fsSL https://get.docker.com
 -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker ubuntu
newgrp docker


Install GitHub runner on EC2 and configure with repository.

---

## 🔐 GitHub Secrets Required

Add these in repository settings:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION
- ECR_REPOSITORY_NAME

---

## 📂 Project Structure
.
├── artifacts
│ └── model.pkl
├── src
│ ├── components
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ ├── pipeline
│ └── utils.py
├── .github
│ └── workflows
│ └── main.yaml
├── Dockerfile
├── requirements.txt
├── app.py
└── README.md


---

## 🚀 How to Run Project Locally

1. Clone repository
git clone <repo_url>
cd project


2. Create virtual environment


python -m venv venv
source venv/bin/activate


3. Install dependencies


pip install -r requirements.txt


4. Run application


python app.py


---

## 📊 Model Evaluation Metric

Primary evaluation metric:

- R2 Score

Best performing model is automatically selected during training phase.

---

## 🎯 Key Features

- Modular ML architecture
- Config driven pipeline
- Automatic best model selection
- Dockerized deployment
- End to end CI CD
- Cloud deployment ready

## 👨‍💻 Author

Satyam Gajjar  

This project demonstrates practical implementation of Machine Learning with production ready MLOps setup.
