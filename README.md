# DevOps CI/CD Flask Application

This repository contains a Flask REST API application with full CRUD operations, created as a university project for the DevOps course.  
The main goal of the project is to demonstrate a complete CI/CD process using GitHub Actions and deployment to Azure App Service.

---

## Live Demo

The application is deployed to Azure App Service and publicly available at:

[devops-flask-app.azurewebsites.net](https://devops-flask-app-ejdthwb0bbgngabc.polandcentral-01.azurewebsites.net)

Available endpoints:

- `GET /` – home endpoint
- `GET /products` – returns all products
- `GET /products/<id>` – returns a single product
- `POST /products` – creates a new product
- `PUT /products/<id>` – updates an existing product
- `DELETE /products/<id>` – deletes a product

---

## Technology Stack

- Python 3
- Flask (REST API with CRUD operations)
- Pytest with coverage reporting
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

## API Documentation

### Get All Products

**Request:**

```http
GET /products
```

**Response:**

```json
[
  {
    "id": 1,
    "name": "Dzik",
    "price": 10.99
  },
  {
    "id": 2,
    "name": "Lays",
    "price": 12.99
  }
]
```

### Get Single Product

**Request:**

```http
GET /products/1
```

**Response (200 OK):**

```json
{
  "id": 1,
  "name": "Dzik",
  "price": 10.99
}
```

**Response (404 Not Found):**

```json
{
  "error": "Produkt nie został znaleziony"
}
```

### Create Product

**Request:**

```http
POST /products
Content-Type: application/json

{
  "name": "New Product",
  "price": 99.99
}
```

**Response (201 Created):**

```json
{
  "id": 4,
  "name": "New Product",
  "price": 99.99
}
```

**Response (400 Bad Request):**

```json
{
  "error": "Wymagane pola: name, price"
}
```

### Update Product

**Request:**

```http
PUT /products/1
Content-Type: application/json

{
  "name": "Updated Name",
  "price": 15.99
}
```

**Response (200 OK):**

```json
{
  "id": 1,
  "name": "Updated Name",
  "price": 15.99
}
```

**Response (404 Not Found):**

```json
{
  "error": "Produkt nie został znaleziony"
}
```

### Delete Product

**Request:**

```http
DELETE /products/1
```

**Response (200 OK):**

```json
{
  "message": "Produkt został usunięty"
}
```

**Response (404 Not Found):**

```json
{
  "error": "Produkt nie został znaleziony"
}
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

Unit tests are implemented using pytest and cover all CRUD operations.

**Run all tests:**

```bash
pytest
```

**Run tests with verbose output:**

```bash
pytest -v
```

**Run tests with coverage:**

```bash
pytest --cov=app tests/
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

- Implement REST API with full CRUD operations
- Practice Git workflow with branches and pull requests
- Create a CI pipeline with automated testing
- Create a CD pipeline with cloud deployment
- Deploy a publicly accessible web application
- Apply basic DevOps concepts in practice

## Cleanup

After project evaluation, all Azure resources can be removed by deleting the Resource Group to avoid additional costs.

## Secrets

Sensitive values are stored in **GitHub Secrets** and are not committed to the repository.

Used secrets:

- `AZUREAPPSERVICE_PUBLISHPROFILE` – publish profile for Azure App Service deployment (used by GitHub Actions)

Repo → Settings → Secrets and variables → Actions
