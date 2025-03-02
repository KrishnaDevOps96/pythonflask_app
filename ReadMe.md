# Flask Task API

This is a simple Flask-based API for managing tasks. It supports CRUD operations and is designed to be deployed on Google Cloud Run.

## Features
- Get all tasks
- Add a new task
- Update a task
- Delete a task

## Project Structure
```
.
|-- flaskapp.py           # Flask API application
|-- Dockerfile           # Docker configuration for containerization
|-- requirements.txt     # Python dependencies
```

## Requirements
- Python 3.11
- Flask 3.0.0
- Docker
- Google Cloud SDK (for deployment)

## Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. **Create a virtual environment (optional but recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the app locally:**
```bash
python flaskapp.py
```

The app will be available at `http://localhost:8080`.

## Docker Usage

1. **Build the Docker image:**
```bash
docker build -t flask-task-api .
```

2. **Run the Docker container:**
```bash
docker run -p 8080:8080 flask-task-api
```

## Deployment to Google Cloud Run with Cloud Build

1. **Authenticate with Google Cloud:**
```bash
gcloud auth login
```

2. **Set your project:**
```bash
gcloud config set project your-project-id
```

3. **Enable required services:**
```bash
gcloud services enable cloudbuild.googleapis.com run.googleapis.com artifactregistry.googleapis.com
```

4. **Create an Artifact Registry (if not created):**
```bash
gcloud artifacts repositories create your-repo-name \
  --repository-format=docker \
  --location=your-region \
  --description="Docker repository"
```

5. **Trigger Cloud Build to build and deploy:**
Create a `cloudbuild.yaml` file like this:
```yaml
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'your-region-docker.pkg.dev/your-project-id/your-repo-name/flask-task-api', '.']

- name: 'gcr.io/cloud-builders/docker'
  args: ['push', 'your-region-docker.pkg.dev/your-project-id/your-repo-name/flask-task-api']

- name: 'gcr.io/cloud-builders/gcloud'
  args: ['run', 'deploy', 'flask-task-api', '--image', 'your-region-docker.pkg.dev/your-project-id/your-repo-name/flask-task-api', '--platform', 'managed', '--region', 'your-region', '--allow-unauthenticated']
```

6. **Run Cloud Build:**
```bash
gcloud builds submit --config cloudbuild.yaml .
```

7. **Access the deployed app:**
Grab the URL from the deployment output and test the endpoints.

## API Endpoints

- **GET /tasks** – Get all tasks
- **POST /tasks** – Add a new task
- **PUT /tasks/<task_id>** – Update an existing task
- **DELETE /tasks/<task_id>** – Delete a task

## Contributing
Feel free to fork the project and submit pull requests.

## License
This project is licensed under the MIT License.

