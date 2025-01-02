# CloudForge

<p align="center">
  <img src="docs/assets/img/CloudForge.png" alt="CloudForge" width="300"/>
</p>

[![License](https://img.shields.io/badge/license-GNU-blue)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.10%2B-brightgreen)
[![GitHub Issues](https://img.shields.io/github/issues/leoBitto/CloudForge)](https://github.com/leoBitto/CloudForge/issues)
[![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-green)](https://github.com/leoBitto/CloudForge)
[![CI - Tests](https://github.com/leoBitto/CloudForge/actions/workflows/CI.yml/badge.svg)](https://github.com/leoBitto/CloudForge/actions/workflows/CI.yml)

Welcome to **CloudForge** 🚀, a flexible and scalable platform designed to orchestrate **data engineering workflows** for small and medium-sized enterprises (SMEs).  

CloudForge seamlessly integrates tools for **data automation**, **monitoring**, and **business analytics**:  
- **Django**: Build business-driven web applications with ease.  
- **Streamlit**: Deliver interactive **visual insights** and data visualizations.  
- **Airflow**: Automate and manage your data pipelines.  
- **PostgreSQL**: Separate data storage layers (**Gold** & **Silver** & **Bronze**) for different quality of the data.   

Together, these tools provide an **end-to-end solution** for automating workflows, analyzing data, and supporting business decision-making.

---

## Features ✨

- **Django**: Core framework for building dynamic and robust business applications.  
- **Streamlit**: Visualize your data interactively with custom dashboards.  
- **Airflow**: Automate workflows and orchestrate complex data pipelines.  
- **PostgreSQL (Gold & Silver & Bronze)**: Three instances to manage raw, refined and aggregated data.   
- **Nginx**: Proxy and route requests efficiently.  

---

## Getting Started 🛠️

Follow these steps to get CloudForge up and running locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/leoBitto/CloudForge.git
   cd CloudForge
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
   - **Streamlit**: [http://localhost/streamlit](http://localhost/streamlit)  

---

## Project Structure 📂

```plaintext
CloudForge/
├── docker
│   ├── dev
│   │   ├── compose.airflow.yml
│   │   ├── compose.base.yml
│   │   ├── compose.databases.yml
│   │   ├── compose.django.yml
│   │   ├── compose.nginx.yml
│   │   └── compose.streamlit.yml
│   └── prod
├── LICENSE
├── manager.sh
├── README.md
└── src
    ├── airflow
    │   ├── config
    │   │   ├── airflow.conf
    │   │   └── airflow-db.conf
    │   └── plugins
    ├── django
    │   ├── app
    │   │   ├── authentication
    │   │   │   ├── admin.py
    │   │   │   ├── apps.py
    │   │   │   ├── __init__.py
    │   │   │   ├── models.py
    │   │   │   ├── signals.py
    │   │   │   ├── templates
    │   │   │   │   └── authentication
    │   │   │   │       ├── login.html
    │   │   │   │       └── logout.html
    │   │   │   ├── tests.py
    │   │   │   ├── urls.py
    │   │   │   └── views.py
    │   │   ├── backoffice
    │   │   │   ├── admin.py
    │   │   │   ├── apps.py
    │   │   │   ├── __init__.py
    │   │   │   ├── models.py
    │   │   │   ├── templates
    │   │   │   │   └── backoffice
    │   │   │   │       └── backoffice.html
    │   │   │   ├── tests.py
    │   │   │   ├── urls.py
    │   │   │   └── views.py
    │   │   ├── base
    │   │   │   ├── asgi.py
    │   │   │   ├── __init__.py
    │   │   │   ├── settings.py
    │   │   │   ├── urls.py
    │   │   │   └── wsgi.py
    │   │   ├── create_superuser.py
    │   │   ├── manage.py
    │   │   └── website
    │   │       ├── admin.py
    │   │       ├── apps.py
    │   │       ├── __init__.py
    │   │       ├── migrations
    │   │       │   └── __init__.py
    │   │       ├── models.py
    │   │       ├── templates
    │   │       │   └── website
    │   │       │       └── home.html
    │   │       ├── tests.py
    │   │       ├── urls.py
    │   │       └── views.py
    │   ├── config
    │   │   ├── databases
    │   │   │   ├── bronze.conf
    │   │   │   ├── gold.conf
    │   │   │   └── silver.conf
    │   │   └── django.conf
    │   ├── Dockerfile
    │   └── requirements.txt
    ├── nginx
    │   └── config
    │       └── nginx.dev.conf
    └── streamlit
        ├── app
        │   ├── app.py
        │   ├── authentication.py
        ├── config
        │   ├── authorized_groups.yml
        │   └── streamlit.conf
        ├── Dockerfile
        └── requirements.txt

33 directories, 68 files

```

---

## Contributing 🤝

Contributions are welcome! If you'd like to contribute to **CloudForge**, please follow these steps:

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

For any questions, suggestions, or feedback, feel free to open an issue on [GitHub](https://github.com/leoBitto/CloudForge/issues).

---
