# KT Practical Exam – End-to-End MLOps Pipeline

This project demonstrates a complete MLOps workflow including:

- Data Version Control (DVC)
- Model training with MLflow tracking
- FastAPI model serving
- Email alerts on failure
- Docker containerization
- Docker Compose orchestration
- GitHub Actions CI pipeline

---

# 🚀 Project Overview

We train a simple Linear Regression model to predict house prices based on:

- sqft
- bedrooms
- bathrooms

The model is:
- Versioned using DVC
- Tracked using MLflow
- Served using FastAPI
- Containerized using Docker
- Tested using GitHub Actions

---

# 🛠 Tech Stack

- Python 3.10
- FastAPI
- Scikit-learn
- MLflow
- DVC
- Docker
- GitHub Actions
- Gmail SMTP (for email alerts)

---

# 📂 Project Structure

```
SET 6/
│
├── api/
│   ├── app.py
│   ├── utils.py
│   ├── requirements.txt
│   └── model.pkl
│
├── data/
│   └── data.csv
│
├── ml/
│   ├── train.py
│   └── params.yml
│
├── docker/
│   └── Dockerfile
│
├── dvc.yaml
├── dvc.lock
├── docker-compose.yml
├── .env
└── README.md
```

---

# ⚙️ LOCAL SETUP INSTRUCTIONS

## 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r api/requirements.txt
pip install mlflow dvc pyyaml
```

---

# 📊 DVC SETUP

Initialize DVC (only first time):

```bash
dvc init
```

Track dataset:

```bash
dvc add data/data.csv
git add data/data.csv.dvc .gitignore
git commit -m "Track dataset with DVC"
```

Run pipeline:

```bash
dvc repro
```

This will:
- Train the model
- Save model.pkl
- Create dvc.lock file

---

# 📈 MLflow Tracking

Start MLflow UI:

```bash
mlflow ui
```

Open in browser:

```
http://127.0.0.1:5000
```

You will see:
- Logged parameters
- Metrics (MAE)
- Experiment history

---

# 🧠 Train Model Manually (Without DVC)

```bash
python ml/train.py
```

This will create:

```
api/model.pkl
```

---

# 🌐 Run FastAPI Locally

Navigate to api folder:

```bash
cd api
uvicorn app:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

# 🔮 Test Prediction Endpoint

POST request to:

```
http://127.0.0.1:8000/predict
```

JSON Body:

```json
{
  "sqft": 2000,
  "bedrooms": 3,
  "bathrooms": 2
}
```

---

# 📧 Email Alert Setup

Create a `.env` file in the project root:

```
EMAIL_USER=yourgmail@gmail.com
EMAIL_PASS=your_app_password
EMAIL_RECEIVER=receiver@gmail.com
```

Important:
- Use Gmail App Password
- Do NOT use your real Gmail password

If invalid payload is sent, email alert will be triggered automatically.

Example failure payload:

```json
{
  "sqft": 2000
}
```

---

# 🐳 Docker Build

Build Docker image:

```bash
docker build -t kt-ml-app ./docker
```

Run container:

```bash
docker run -p 8000:8000 --env-file .env kt-ml-app
```

---

# 🐳 Docker Compose

Run full stack:

```bash
docker compose up --build
```

Check running containers:

```bash
docker ps
```

---

# 🔁 GitHub Actions CI/CD

On every push to main branch:

- Install dependencies
- Run training script
- Build Docker image

To manually trigger:

```bash
git commit --allow-empty -m "Trigger CI"
git push
```

Check status in:

GitHub → Actions Tab

---

# 🧪 How to Test Email Failure

Send incorrect payload:

```json
{
  "sqft": 1000
}
```

You should receive an alert email.

---

# 🧹 Troubleshooting

### DVC Validation Error
Ensure:
- No incorrect `.dvc` files inside ml folder
- Use `dvc.yaml` in root

### Model Not Found
Run:
```bash
python ml/train.py
```

### Email Not Working
- Check `.env` file
- Ensure Gmail App Password is correct
- Enable App Passwords in Google Account

---

# 🎯 Evaluation Checklist

- DVC tracking working
- MLflow logging parameters
- FastAPI prediction working
- Email alert on failure
- Docker container running
- GitHub Actions successful

---

# 🏁 Conclusion

This project demonstrates a complete end-to-end MLOps pipeline including:

Data Versioning → Model Training → Experiment Tracking → API Serving → Containerization → CI/CD Automation.

