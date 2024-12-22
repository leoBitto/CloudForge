# DataFoundry

<p align="center">
  <img src="docs/assets/img/DataFoundry.png" alt="DataFoundry" width="300"/>
</p>

[![License](https://img.shields.io/badge/license-GNU-blue)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.10%2B-brightgreen)
[![GitHub Issues](https://img.shields.io/github/issues/leoBitto/DataFoundry)](https://github.com/leoBitto/DataFoundry/issues)
[![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-green)](https://github.com/leoBitto/DataFoundry)
![CI - Tests](https://github.com/leoBitto/repo/actions/workflows/tests-pipeline.yml/badge.svg)

Welcome to **DataFoundry** 🚀, a flexible and scalable platform designed to orchestrate **data engineering workflows** for small and medium-sized enterprises (SMEs).  

DataFoundry seamlessly integrates tools for **data automation**, **monitoring**, and **business analytics**:  
- **Django**: Build business-driven web applications with ease.  
- **Streamlit**: Deliver interactive **visual insights** and data visualizations.  
- **Airflow**: Automate and manage your data pipelines.  
- **PostgreSQL**: Separate data storage layers (**Gold** & **Silver**) for different quality of the data.  
- **Grafana & Prometheus**: Monitor and alert on system health and performance.  

Together, these tools provide an **end-to-end solution** for automating workflows, analyzing data, and supporting business decision-making.

---

## Features ✨

- **Django**: Core framework for building dynamic and robust business applications.  
- **Streamlit**: Visualize your data interactively with custom dashboards.  
- **Airflow**: Automate workflows and orchestrate complex data pipelines.  
- **PostgreSQL (Gold & Silver)**: Two instances to manage refined and aggregated data.  
- **Grafana & Prometheus**: Monitor metrics and get real-time system insights.  
- **Nginx**: Proxy and route requests efficiently.  

---

## Getting Started 🛠️

Follow these steps to get DataFoundry up and running locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/leoBitto/DataFoundry.git
   cd DataFoundry
   ```

2. **Build and run the project** using the provided script:
   ```bash
   source manager.sh build
   ```

3. **Access the services**:
   - **Airflow**: [http://localhost/airflow](http://localhost/airflow)  
     Username: `admin` | Password: `admin`
   - **Django Admin**: [http://localhost/admin](http://localhost/admin)  
     Username: `admin` | Password: `admin`
   - **Streamlit**: [http://localhost:8501](http://localhost:8501)  
   - **Grafana**: [http://localhost:3000](http://localhost:3000)  
     Default Login: `admin` / `admin`

---

## Project Structure 📂

```plaintext
DataFoundry/
├── config
│   ├── airflow.conf
│   ├── airflow-db.conf
│   ├── django.conf
│   ├── gold.conf
│   └── silver.conf
├── docker
│   ├── django
│   │   └── Dockerfile
│   ├── docker-compose.airflow.yml
│   ├── docker-compose.dev.yml
│   └── docker-compose.django.yml
├── docs
│   ├── assets
│   │   └── img
│   │       └── DataFoundry.png
│   ├── base.md
│   ├── _config.yml
│   └── index.md
├── LICENSE
├── manager.sh
├── nginx
│   ├── nginx.conf
│   └── nginx.dev.conf
├── README.md
└── src
    ├── airflow
    │   ├── dags
    │   │   └── test.py
    │   ├── logs
    │   │   └── scheduler
    │   └── plugins
    ├── django
    │   ├── base
    │   │   ├── asgi.py
    │   │   ├── __init__.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── create_superuser.py
    │   ├── manage.py
    │   └── requirements.txt
    └── streamlit
```

---

## Contributing 🤝

Contributions are welcome! If you'd like to contribute to **DataFoundry**, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-xyz`).
3. Commit your changes (`git commit -m "Add feature xyz"`).
4. Push to the branch (`git push origin feature-xyz`).
5. Open a Pull Request.

---

## License 📜

This project is licensed under the **GNU General Public License (GPL)**. See the [LICENSE](LICENSE) file for details.

---

## Contact 📬

For any questions, suggestions, or feedback, feel free to open an issue on [GitHub](https://github.com/leoBitto/DataFoundry/issues).

---
