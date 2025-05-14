calc/
│
├── app.py
├── templates/
│   └── index.html
├── Dockerfile
├── requirements.txt
└── .dockerignore




https://github.com/SN8086/calc.git
pip install -r reqirements.txt	
gcloud builds submit --tag gcr.io/shri-454207/calc

gcloud container clusters create my-cluster-2 \
  --zone us-central1-a \
  --num-nodes=2
  
  gcloud container clusters get-credentials my-cluster-2 --region=us-central1

