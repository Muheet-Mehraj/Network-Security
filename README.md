# Network-Security

**Production-grade ML pipeline for network threat classification — containerized, cloud-deployed, and CI/CD automated.**

![python](https://img.shields.io/badge/python-3.9+-blue)
![ml](https://img.shields.io/badge/ml-classification-green)
![docker](https://img.shields.io/badge/docker-ready-blue)
![aws](https://img.shields.io/badge/AWS-ECR-orange?logo=amazonaws)
![ci/cd](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black?logo=githubactions)
![mlflow](https://img.shields.io/badge/tracking-MLflow-blue)
![status](https://img.shields.io/badge/project-active-success)

---

## Overview

Classifies network traffic as **legitimate or malicious (phishing)** using a supervised ML pipeline built to production standards. The system covers the full lifecycle — data ingestion from MongoDB, schema validation, KNN imputation, automated model selection, artifact sync to AWS S3, and a FastAPI inference endpoint — all containerized with Docker and deployed to AWS ECR via GitHub Actions.

---

## Model Performance

| Metric     | Score                          |
|------------|-------------------------------|
| F1 Score   | **97.65%**                    |
| Precision  | **97.00%**                    |
| Recall     | **98.31%**                    |
| Baseline   | 93.00% (Logistic Regression)  |
| Best Model | Random Forest (GridSearchCV)  |
| Dataset    | 11,055 samples · 56% legitimate / 44% phishing |
| Validation | 10 MLflow runs on DagsHub     |

Model selected via **GridSearchCV across 5 classifiers and 30+ hyperparameter combinations**. All runs tracked and versioned in MLflow.

---

## Architecture

```
MongoDB Atlas (Raw Data)
        ↓
  Data Ingestion — push_data.py
        ↓
  Schema Validation — data_schema/
        ↓
  KNN Imputation + Feature Engineering
        ↓
  GridSearchCV — 5 classifiers, 30+ hyperparameters
        ↓
  KS-2 Drift Detection (train vs test split)
        ↓
  best_model.pkl → AWS S3 artifact sync
        ↓
  FastAPI Inference API — app.py
        ↓
  Docker Container
        ↓
  AWS ECR → GitHub Actions CI/CD
```

---

## Engineering Highlights

- **Automated model selection** — GridSearchCV across Logistic Regression, Random Forest, Decision Tree, Gradient Boosting, and AdaBoost; best model improved F1 from 93% to 97.65%
- **KS-2 drift detection** — statistical test between train and test splits to catch distribution shift before deployment
- **MLflow experiment tracking** — all 10 runs logged on DagsHub with metrics, parameters, and artifacts
- **Modular pipeline** — ingestion, validation, training, and inference fully decoupled as separate stages
- **Schema-driven validation** — data quality enforced at ingestion before every training run
- **S3 artifact sync** — model and preprocessor automatically pushed to AWS S3 after every successful training run
- **19 automated CI/CD deployments** — zero manual deployments, full GitHub Actions → Docker → AWS ECR pipeline

---

## Technology Stack

| Category        | Technology                              |
|-----------------|-----------------------------------------|
| Language        | Python 3.9+                             |
| ML              | Scikit-learn, XGBoost                   |
| Experiment Tracking | MLflow, DagsHub                     |
| Data            | NumPy, Pandas, KNN Imputation           |
| API             | FastAPI                                 |
| Database        | MongoDB Atlas                           |
| Artifact Storage| AWS S3                                  |
| Containerization| Docker                                  |
| Container Registry | AWS ECR                              |
| CI/CD           | GitHub Actions                          |

---

## Project Structure

```
Network-Security/
│
├── .github/workflows/     # GitHub Actions → AWS ECR CI/CD pipeline
│
├── Network_Data/          # Training dataset (phishing detection)
├── valid_data/            # Validation / test data
├── data_schema/           # Schema validation rules
├── final_model/           # Model artifacts
├── best_model.pkl         # Trained classification model
│
├── Networksecurity/       # Core ML pipeline package
├── templates/             # FastAPI inference UI
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

## Local Setup

### Prerequisites
- Python 3.9+
- Docker
- MongoDB Atlas connection string
- AWS credentials (for S3 and ECR)

### Run Locally

```bash
git clone https://github.com/Muheet-Mehraj/Network-Security.git
cd Network-Security

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

Create a `.env` file in the root:

```env
MONGO_DB_URL=your_mongodb_connection_string
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=your_region
AWS_BUCKET_NAME=your_bucket
```

Then run:

```bash
python push_data.py   # Ingest data into MongoDB
python main.py        # Run training pipeline
python app.py         # Start FastAPI inference server
```

### Docker

```bash
docker build -t network-security .
docker run -p 5000:5000 network-security
```

---

## CI/CD Pipeline

Every push to `main` triggers:

1. GitHub Actions workflow starts
2. Docker image built automatically
3. Image pushed to **AWS Elastic Container Registry (ECR)**
4. Deployment updated

**19 successful automated deployments** — no manual intervention at any stage.

---

## Limitations

- Relies on supervised patterns in training data — novel, unseen attack vectors may be missed
- Not a real-time packet capture system; operates on pre-collected network traffic features
- Dataset quality directly impacts detection accuracy

---

## Future Improvements

- [ ] Real-time traffic ingestion via packet capture
- [ ] SHAP / LIME explainability for model decisions
- [ ] Auto-retraining pipeline triggered by drift detection
- [ ] Kubernetes deployment for horizontal scaling
- [ ] Deep learning models (LSTM) for sequential traffic pattern detection

---

## Author

**Muheet Mehraj**
[GitHub](https://github.com/Muheet-Mehraj) · [LinkedIn](https://linkedin.com/in/muheet-mehraj) · muheetmehraj93@gmail.com

---

## License

MIT License — free to use, modify, and distribute.
