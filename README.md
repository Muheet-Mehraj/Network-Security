# 🔐 Network-Security

*Production-grade Machine Learning Pipeline for Network Threat Classification*

![python](https://img.shields.io/badge/python-3.9+-blue)
![ml](https://img.shields.io/badge/ml-classification-green)
![docker](https://img.shields.io/badge/docker-ready-blue)
![aws](https://img.shields.io/badge/AWS-ECR-orange?logo=amazonaws)
![ci/cd](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black?logo=githubactions)
![status](https://img.shields.io/badge/project-active-success)
![license](https://img.shields.io/badge/license-MIT-green)

> Classifies network traffic as **normal or malicious** using a supervised ML pipeline — containerized with Docker, deployed to **AWS ECR** via GitHub Actions CI/CD.

---

## 🚀 Live Deployment

| Component | Platform |
|---|---|
| Container Registry | AWS Elastic Container Registry (ECR) |
| CI/CD | GitHub Actions (19 workflow runs) |
| Inference API | Docker container on port 5000 |

---

## 📊 Model Performance

| Metric | Score |
|---|---|
| Task | Binary Classification |
| Model | Scikit-learn Classifier |
| Training Data | Network traffic features |
| Model File | `best_model.pkl` |

> ⚠️ Add your actual F1-score, precision, recall, and accuracy here after evaluation.

---

## 🏗️ Architecture

```
Raw Network Traffic Data
        ↓
  Data Ingestion (push_data.py)
        ↓
  Schema Validation (data_schema/)
        ↓
  Feature Processing
        ↓
  Model Training (main.py)
        ↓
  best_model.pkl
        ↓
  FastAPI Inference (app.py)
        ↓
  Docker Container
        ↓
  AWS ECR → Deployed
```

---

## ☁️ CI/CD Pipeline (AWS ECR)

This project uses a **fully automated deployment pipeline**:

1. Code pushed to `main` branch
2. GitHub Actions triggers workflow
3. Docker image built automatically
4. Image pushed to **AWS Elastic Container Registry (ECR)**
5. Deployment updated

**Workflow runs:** 19 successful deployments including:
- `Push Docker to ECR` ✅
- `ECR Repository` ✅
- `Deployment Changes` ✅
- `Cloud S3 Storage` integration

---

## 📁 Project Structure

```
Network-Security/
│
├── .github/workflows/     # CI/CD pipeline (GitHub Actions → AWS ECR)
│
├── Network_Data/          # Training dataset
├── valid_data/            # Validation / test data
├── data_schema/           # Schema validation rules
├── final_model/           # Model artifacts
├── best_model.pkl         # Trained classification model
│
├── Networksecurity/       # Core ML pipeline package
├── templates/             # Inference UI templates
│
├── app.py                 # FastAPI application entry point
├── main.py                # Pipeline execution (training)
├── push_data.py           # Data ingestion → MongoDB
├── test_mongodb.py        # Database connectivity test
│
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
└── setup.py               # Package configuration
```

---

## 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Language | Python 3.9+ |
| ML | Scikit-learn |
| Data | NumPy, Pandas |
| API | FastAPI |
| Database | MongoDB |
| Containerization | Docker |
| Container Registry | AWS ECR |
| CI/CD | GitHub Actions |
| Model Storage | Pickle |

---

## ⚡ Quickstart

### Prerequisites
- Python 3.9+
- Docker (for containerized run)
- AWS CLI configured (for ECR deployment)

### Local Setup

```bash
git clone https://github.com/Muheet-Mehraj/Network-Security.git
cd Network-Security

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

### Docker

```bash
docker build -t network-security .
docker run -p 5000:5000 network-security
```

### Pull from AWS ECR

```bash
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-ecr-uri>
docker pull <your-ecr-uri>/network-security:latest
docker run -p 5000:5000 <your-ecr-uri>/network-security:latest
```

---

## 🔑 Engineering Highlights

- **Modular ML pipeline** — ingestion, validation, training, inference fully separated
- **Schema-driven validation** — data quality enforced before every training run
- **Packaged Python project** — installable as a module via `setup.py`
- **Dockerized** — fully containerized, environment-agnostic
- **AWS ECR deployment** — production container registry with automated push
- **GitHub Actions CI/CD** — 19 automated workflow runs, zero manual deployments
- **MongoDB integration** — persistent data ingestion pipeline

---

## ⚠️ Limitations

- Relies on supervised patterns in training data — novel attack vectors may be missed
- Not a real-time packet capture system
- Dataset quality directly impacts model performance

---

## 🔮 Future Improvements

- [ ] Real-time traffic ingestion via packet capture
- [ ] Ensemble / Deep Learning models for improved detection
- [ ] Model explainability with SHAP / LIME
- [ ] Auto-retraining pipeline on new threat data
- [ ] Kubernetes deployment for horizontal scaling

---

## 👤 Author

**Muheet Mehraj**
GitHub: [@Muheet-Mehraj](https://github.com/Muheet-Mehraj)

---

## 📄 License

MIT License — free to use, modify, and distribute.
