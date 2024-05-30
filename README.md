# SmartLearn
A platform for AI-generated course creation

## Project Structure
```
SmartLearn/
├── courses/ # Django app for course-related features
├── smartlearn/ # Django project settings and configurations
├── Dockerfile # Docker configuration file
├── docker-compose.yml # Docker Compose configuration
├── LICENSE # MIT License
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── manage.py # Django management script
```

## Getting Started
### Prerequisites
- Docker
- Docker Compose
- Python 3.10+
- PostgreSQL

### Installation
1. **Clone the repository**:
```bash
git clone https://github.com/juanfril/SmartLearn.git
cd SmartLearn
```
2. **Build and run docker containers**:
```bash
make build
```
3. **Create a superuser**:
```bash
make createsuperuser
```

## Usage
* Access the applicaton at `http://localhost:8000`
* Access the Django Admin at `http://localhost:8000/admin`
