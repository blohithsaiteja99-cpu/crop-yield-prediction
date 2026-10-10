# 🌾 Smart Crop Yield Predictor Web App

A production-ready Flask web application that predicts crop yield (in tons/hectare) using machine learning based on region, soil type, crop variety, weather condition, rainfall, temperature, fertilizer, irrigation, and days to harvest.

---

## 🚀 Easy Deployment Guide

All necessary deployment files (`vercel.json`, `api/index.py`, `.vercelignore`, `.python-version`, `requirements.txt`, `Procfile`, `Dockerfile`, `render.yaml`, `.gitignore`, `app.py`) are pre-configured.

### Option 1: Deploy to Vercel (Fast & Serverless)

#### Method A: Via GitHub (Recommended)
1. **Push your code to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Deploy smart crop yield predictor to Vercel"
   git branch -M main
   git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
   git push -u origin main
   ```
2. Go to **[Vercel.com](https://vercel.com/)** and log in with your GitHub account.
3. Click **Add New...** → **Project**.
4. Import your GitHub repository.
5. Vercel automatically detects the Python framework and `vercel.json` configuration.
6. Click **Deploy**. Your app will be live with a free `*.vercel.app` URL!

#### Method B: Direct Deploy via Vercel CLI
If you have Node.js installed, simply run from this directory:
```bash
npx vercel
```
Follow the interactive prompts:
- *Set up and deploy?* → `y`
- *Which scope?* → (Select your Vercel account)
- *Link to existing project?* → `N`
- *What's your project's name?* → `crop-yield-predictor`
- *In which directory is your code located?* → `./`
To deploy to production directly:
```bash
npx vercel --prod
```

---

### Option 2: Deploy to Render (Free Cloud Web Service)

1. **Push your code to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Deploy crop yield predictor"
   git branch -M main
   git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
   git push -u origin main
   ```
2. Go to **[Render.com](https://render.com/)** and sign in with your GitHub account.
3. Click **New +** → **Web Service**.
4. Select your GitHub repository.
5. Render will automatically detect the settings from `render.yaml` / `Procfile`:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: `Free`
6. Click **Deploy Web Service**.
7. In ~2 minutes, your live URL will be ready!

---

### Option 2: Deploy to Railway (Free / Starter)

1. Push your repository to GitHub.
2. Go to **[Railway.app](https://railway.app/)** and click **New Project** → **Deploy from GitHub repo**.
3. Select your repository.
4. Railway will automatically detect the `Procfile` / `Dockerfile` and deploy your app.

---

### Option 3: Deploy to Hugging Face Spaces (Free ML Hosting)

1. Go to **[Hugging Face Spaces](https://huggingface.co/spaces)** and click **Create new Space**.
2. Set Space SDK to **Docker** (or Blank).
3. Push your repository files to the Space git remote.
4. The space will automatically build using the included `Dockerfile` and launch your web app.

---

### Option 4: Deploy to PythonAnywhere (Free Tier)

1. Create a free account on **[PythonAnywhere](https://www.pythonanywhere.com/)**.
2. Open a **Bash Console** and clone your repository or upload your files.
3. Create a virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 crop-env
   pip install -r requirements.txt
   ```
4. Go to the **Web** tab → **Add a new web app** → **Manual configuration** (Python 3.10).
5. In the WSGI configuration file (`/var/www/<username>_pythonanywhere_com_wsgi.py`), point to the app:
   ```python
   import sys
   import os

   path = '/home/<username>/crop_project'
   if path not in sys.path:
       sys.path.append(path)

   from app import app as application
   ```
6. Click **Reload** to make your site live.

---

### Option 5: Run Locally or with Docker

#### Local Python:
```bash
pip install -r requirements.txt
python app.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

#### With Docker:
```bash
docker build -t crop-predictor .
docker run -p 5000:5000 crop-predictor
```
Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📁 Project Structure

```
crop_project/
├── api/
│   └── index.py             # Serverless entrypoint for Vercel
├── vercel.json              # Vercel routing, rewrites & bundling rules
├── .vercelignore            # Excludes datasets & caches from Vercel bundle
├── .python-version          # Specifies Python version for Vercel runtime
├── app.py                   # Root WSGI entrypoint for production
├── requirements.txt         # Production dependencies (Flask, pandas, scikit-learn, joblib)
├── Procfile                 # Production web process command (gunicorn app:app)
├── Dockerfile               # Production container definition
├── render.yaml              # 1-click Render blueprint configuration
├── .dockerignore            # Optimizes Docker image size
├── .gitignore               # Ignores large raw datasets and caches
├── crop_project/
│   ├── crop_app.py          # Flask app implementation & routes
│   ├── yield_model.pkl      # Pre-trained ML pipeline model (14.7 MB)
│   └── templates/
│       └── index.html       # Modern Glassmorphic UI frontend
```
