# Dockerized Python Todo API

This project is a containerized backend application built using Python and PostgreSQL, designed to simulate a real-world service architecture with CI/CD integration.

## 🚀 Features

- Python Flask API
- PostgreSQL database integration
- Docker containerization
- Multi-container setup using Docker Compose
- Persistent storage using Docker volumes
- CI/CD pipeline using GitHub Actions
- Environment-based configuration (no hardcoded secrets)
- Non-root container execution (improved security)
- Optimized multi-stage Docker build

## 🧠 Project Purpose

This project demonstrates how backend services are structured, containerized, and automated in modern development workflows.

It simulates a real-world setup where:
- application and database run in separate services
- environment variables manage configuration
- CI pipelines validate builds automatically

## 🏗️ Architecture

- App: Flask API running in a Docker container
- Database: PostgreSQL container
- Orchestration: Docker Compose
- CI/CD: GitHub Actions

## 🛠️ Technologies Used

- Python
- Flask
- PostgreSQL
- Docker
- Docker Compose
- GitHub Actions

## ▶️ How to Run Locally

```bash
docker-compose up --build
