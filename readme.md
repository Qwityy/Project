# Test Project
## Structure
```
Project/
├── frontend/          # only html+css (пока что)
└── backend/           # Python FastAPI Server
```

## Start
### Backend
```
docker build -t backend .
docker run backend
```
### Frontend
```
cd frontend
python -m http.server 3000
```

## Access 
```
backend: http://localhost:8000
frontend: http://localhost:3000
FastAPI Docs: http://localhost:8000/docs
```
