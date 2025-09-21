# TrackFit Backend
![TrackFit Banner](.github/assets/banner.png)

A fitness tracking API built with modern for workout performance tracking.

<!-- [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) -->
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-00a393.svg)](https://fastapi.tiangolo.com)

---

## ✨ Features

- **📊 Advanced Analytics** - Performance calculations and exercise progression tracking
- **🌐 RESTful API** - Auto-generated OpenAPI documentation with interactive testing

### Core Functionality

- Workout performance calculation (1RM, Volume, Progressive overload and intesity)
- Workout data analysis and trend tracking


## 🚀 Getting Started

### Prerequisites
- **Python 3.11+** (for local development)
- **Docker** (for containerized development)
- **exercisedb API key** [www.exercisedb.dev](https://www.exercisedb.dev/docs)

### Local Development Setup

1. Set .env variable
    ```
        IMAGE_NAME=trackfit-service
        EXERCISEDB_API_KEY=YOUR-API-KEY
        EXERCISEDB_HOST_KEY=YOUR-API-KEY
    ```


### Quick Start
```bash
# Clone the repository
git clone https://github.com/CarlosOchoa8/trackfit.git
cd trackfit-backend

# Run the following command
docker compose build --no-cache
docker compose up -d 
# You can remove flag -d to show in terminal logs while container is running.
```


#### API Documentation
Once running, access the interactive API documentation at:
- **Swagger UI**: http://localhost:80/docs

---


## 📊 API Endpoints

### Exercise Management
- `GET /performance/get_exercises` - Retrieve paginated exercise list from exercisedb service

### Performance Analytics
- `POST /performance/calculate` - Calculate performance metrics

<!-- ### Health & Monitoring -->
<!-- - `GET /health` - Service health check -->

---

## 🤝 Contributing

We welcome contributions!

- Setting up the development environment
- Code style and formatting guidelines (Black, isort, ruff)
- Type annotation requirements
- Testing standards and coverage expectations
- Pull request process
##### As were said, the project is in current development,therefore it is possible if you investigate on it, probably get any  kind of error or improvements areas. If that's the case, feel yourself free to contribute with your comments, features, issues or pull request. I'll take a look. Thanks!

### Development Workflow
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes with proper type annotations
4. Commit changes: `git commit -m "Add amazing feature"`
5. Push to branch: `git push origin feature/amazing-feature`
6. Submit a Pull Request

---

## 📋 Roadmap

### 📡 API Enhancement (In Progress)
- [x] OpenAPI documentation
- [x] Exercise CRUD endpoints
- [x] Performance calculation endpoints
- [x] Pagination and filtering
- [ ] Rate limiting and throttling
- [ ] Advanced query capabilities
<!-- - [ ] Bulk operations support -->

<!-- ### 🚀 Advanced Features (Future)
- [ ] User authentication and authorization
- [ ] Multi-tenant architecture
- [ ] Real-time notifications
- [ ] Machine learning integrations
- [ ] Data export/import capabilities -->

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Related Projects

- [TrackFit Frontend](https://github.com/CarlosOchoa8/trackfit-frontend) - React-based web interface

---

## 📞 Support

For questions, issues, or contributions:
<!-- - 📧 Email: support@trackfit.com -->
- 🐛 Issues: [GitHub Issues](https://github.com/CarlosOchoa8/trackfit/issues)
<!-- - 💬 Discussions: [GitHub Discussions](https://github.com/CarlosOchoa8/trackfit/discussions) -->
