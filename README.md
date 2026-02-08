# DevOps CI/CD Flask Application

This repository contains a simple Flask web application created as a university project for the DevOps course.  
The main goal of the project is to demonstrate a complete CI/CD process using GitHub Actions and deployment to Azure App Service.

---

## Live Demo

The application is deployed to Azure App Service and publicly available at:

[devops-flask-app.azurewebsites.net](https://devops-flask-app-ejdthwb0bbgngabc.polandcentral-01.azurewebsites.net)

Available endpoints:

- `/` – home endpoint
- `/products` – returns a sample list of products in JSON format

---

## Technology Stack

- Python 3
- Flask
- Pytest
- GitHub Actions (CI/CD)
- Azure App Service (Linux)

---

## Project Structure

```bash
.
├── app/
│ ├── __init__.py
│ └── main.py
├── tests/
│ ├── __init__.py
│ └── test_app.py
├── .github/
│ └── workflows/
│ ├── ci.yml
│ └── cd-azure.yml
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Run the Application Locally

### 1. Clone the repository

```bash
git clone https://github.com/achyla/devops-ci-cd-project/
cd devops-ci-cd-project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app/main.py
```

### The application will be available at:

```bash
http://127.0.0.1:5000
```

## Tests

Unit tests are implemented using pytest.

```bash
pytest
```

## CI/CD Pipeline

**Continuous Integration (CI)**

- Implemented with GitHub Actions
- Automatically runs unit tests on every push and pull request to the main branch

**Continuous Deployment (CD)**

- After merging changes into the main branch, the application is automatically deployed to Azure App Service
- Deployment is performed using GitHub Actions and Azure publish profile

## Deployment Details

- Platform: Azure App Service (Linux)
- Runtime: Python
- Web server: Gunicorn
- Startup command:

```bash
gunicorn --bind=0.0.0.0 --timeout 600 app.main:app
```

## Project Objectives

- Practice Git workflow with branches and pull requests
- Create a CI pipeline with automated testing
- Create a CD pipeline with cloud deployment
- Deploy a publicly accessible web application
- Apply basic DevOps concepts in practice

## Cleanup

After project evaluation, all Azure resources can be removed by deleting the Resource Group to avoid additional costs.
