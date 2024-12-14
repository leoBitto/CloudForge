# Installation Guide  

[⬅ Back to Documentation Home]({{ site.baseurl }}/index/)  

This guide will walk you through the steps to install and set up **DataFoundry** in both **development** and **production** environments.  

---

## Table of Contents  

1. [Development Environment](#development-environment)  
2. [Production Environment](#production-environment)  

---

## Development Environment  

Follow these steps to set up DataFoundry for local development:  

### Prerequisites  

Ensure the following tools are installed:  
- **Docker** (minimum version: `20.x`)  
- **Docker Compose** (minimum version: `1.29.x`)  
- **Git**  
- **Python 3.10+**  
- **pip** 

### Steps  

1. **Clone the Repository**  

   ```bash
   git clone https://github.com/leoBitto/DataFoundry.git
   cd DataFoundry
   ``` 

1. **Start Services**  

   Use the provided Docker Compose file to launch the services:  

   ```bash
   docker-compose -f docker-compose.dev.yml up --build
   ```

   - Airflow: [http://localhost:8080](http://localhost/airflow)  
   - Django: [http://localhost:8000](http://localhost/)  
   - Streamlit: [http://localhost:8501](http://localhost/streamlit)  

1. **Verify Services**  

   - Check the logs to ensure all containers are running properly.  
   - Use the following command to list active services:  

     ```bash
     docker ps -a 
     ```

     there should be several up services and some down, the down services are the one the allow initial setup

---

## Production Environment  

For deploying DataFoundry in a production environment, automated pipelines are provided through **CI/CD flows**.  

### Prerequisites  

Ensure the following requirements are met:  
- **Docker** and **Docker Compose** installed on the target server.  
- A **CI/CD pipeline** configured (e.g., GitHub Actions).  
- A domain name and SSL certificates for secure access to the services.

### Steps  

1. **CI/CD Overview**  

   DataFoundry uses a robust CI/CD process for deployment. The pipeline includes:  
   - Building Docker images.  
   - Running tests (unit, integration, E2E).  
   - Pushing images to a container registry (e.g., GHCR).  
   - Deploying to the production environment.  

   Refer to the [CI/CD Overview]({{ site.baseurl }}/cicd/overview/) for detailed setup instructions.  

2. **Manual Deployment (Optional)**  

   If CI/CD is unavailable, you can deploy manually:  

   ```bash
   docker-compose -f docker-compose.prod.yml up --build -d
   ```

   Services will be available at:  
   - Airflow: `https://<your-domain>/airflow`  
   - Django: `https://<your-domain>/`  
   - Streamlit: `https://<your-domain>/dashboard`  

3. **Environment Variables**  

   Ensure all production-specific environment variables are set correctly. For details, refer to the [Environment Setup Guide]({{ site.baseurl }}/env-setup/).  

---

## Next Steps  
 
- [Environment Setup]({{ site.baseurl }}/env-setup/)  
- [CI/CD Overview]({{ site.baseurl }}/cicd/overview/)  

---

Questo schema mantiene la pagina chiara e organizzata, fornendo istruzioni dettagliate per entrambi gli ambienti con i riferimenti necessari ad altre sezioni. Cosa ne pensi?