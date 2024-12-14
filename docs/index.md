# DataFoundry Documentation  

Welcome to the official documentation for **DataFoundry**, a modular and scalable platform designed to orchestrate **data engineering workflows** for small and medium-sized enterprises (SMEs). This documentation will guide you through the **installation**, **configuration**, **usage**, and **development** of DataFoundry.  

---

## Table of Contents  

1. [Introduction](#introduction)  
2. [Getting Started](#getting-started)  
   - [Installation]({{ site.baseurl }}/installation/)  
   - [Running the Project]({{ site.baseurl }}/run-project/)  
   - [Environment Setup]({{ site.baseurl }}/env-setup/)  
3. [Project Structure](#project-structure)  
4. [Services Overview](#services-overview)  
   - [Django]({{ site.baseurl }}/services/django/)  
   - [Airflow]({{ site.baseurl }}/services/airflow/)  
   - [Streamlit]({{ site.baseurl }}/services/streamlit/)  
   - [PostgreSQL (Gold & Silver)]({{ site.baseurl }}/services/postgresql/)  
   - [Grafana & Prometheus]({{ site.baseurl }}/services/monitoring/)  
   - [Nginx]({{ site.baseurl }}/services/nginx/)  
5. [Usage](#usage)  
   - [Managing Workflows with Airflow]({{ site.baseurl }}/usage/airflow/)  
   - [Building Dashboards with Streamlit]({{ site.baseurl }}/usage/streamlit/)  
   - [Monitoring with Grafana & Prometheus]({{ site.baseurl }}/usage/monitoring/)  
6. [Configuration](#configuration)  
   - [Environment Variables]({{ site.baseurl }}/configuration/env-vars/)  
   - [Service-Specific Configuration]({{ site.baseurl }}/configuration/service-configs/)  
7. [Development Guidelines](#development-guidelines)  
   - [Extending DataFoundry]({{ site.baseurl }}/development/extending/)  
   - [Adding New Airflow DAGs]({{ site.baseurl }}/development/airflow-dags/)  
   - [Custom Django Applications]({{ site.baseurl }}/development/django-apps/)  
8. [Contributing]({{ site.baseurl }}/CONTRIBUTING/)  
9. [Code of Conduct]({{ site.baseurl }}/CODE_OF_CONDUCT/)  
10. [License]({{ site.baseurl }}/LICENSE/)  

---

## Introduction  

**DataFoundry** is a robust platform that combines **data automation**, **monitoring**, and **business analytics** into a single environment. It provides:  

- **Workflow orchestration** with Airflow.  
- **Interactive dashboards** using Streamlit.  
- **System monitoring** with Grafana and Prometheus.  
- A modular architecture that ensures flexibility and scalability for SMEs.  

This documentation will help you get started with DataFoundry, configure its components, and extend its functionalities.  

---

## Getting Started  

If you are new to DataFoundry, start with:  

1. **Installation**: Learn how to install and set up the platform locally.  
2. **Running the Project**: Instructions to spin up the entire stack using Docker.  
3. **Environment Setup**: Setting up variables and configurations.  

---

## Project Structure  

DataFoundry is organized into modular components for easy management. Explore the [Project Structure]({{ site.baseurl }}/project-structure) section to understand the role of each directory.  

---

## Services Overview  

DataFoundry integrates the following services:  

- **Django**: Build robust web applications.  
- **Airflow**: Orchestrate and automate data workflows.  
- **Streamlit**: Create visualizations and interactive dashboards.  
- **PostgreSQL (Gold & Silver)**: Dual-layered database management for refined and raw data.  
- **Grafana & Prometheus**: Monitor system health and performance metrics.  
- **Nginx**: Proxy and route requests efficiently.  

---

## Usage  

### Workflow Automation  
Manage and monitor complex data workflows with **Airflow**. See the [Airflow Usage Guide]({{ site.baseurl }}/usage/airflow).  

### Dashboard Creation  
Build interactive dashboards to visualize your data using **Streamlit**. Learn more in the [Streamlit Usage Guide]({{ site.baseurl }}/usage/streamlit).  

### Monitoring  
Get real-time insights and alerts on your system health with **Grafana & Prometheus**.  

---

## Configuration  

Learn how to configure DataFoundry to suit your environment:  

- Set up environment variables.  
- Adjust configurations for each service.  

---

## Development Guidelines  

Want to extend or customize DataFoundry? Check out the development section for:  

- Adding new **Airflow DAGs**.  
- Creating custom **Django applications**.  
- Extending platform functionalities.  

---

## Contributing  

Contributions are welcome! To get started, read our [Contributing Guidelines]({{ site.baseurl }}/CONTRIBUTING/).  

## Code of Conduct  

Please adhere to our [Code of Conduct]({{ site.baseurl }}/CODE_OF_CONDUCT/) to maintain a welcoming community.  

## License  

DataFoundry is licensed under the **GNU GPL**. See the [License]({{ site.baseurl }}/LICENSE) file for details.  

---

## Contact  

For any questions or feedback, feel free to open an issue on [GitHub](https://github.com/leoBitto/DataFoundry/issues).  

---
