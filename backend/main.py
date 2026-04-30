from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI(title="Sales Dashboard API")

# CORS set karna taaki Frontend (React) isse connect ho sake
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Processed data ka rasta
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "processed")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend is running!"}

@app.get("/api/revenue")
def get_revenue():
    try:
        df = pd.read_csv(os.path.join(DATA_PATH, "monthly_revenue.csv"))
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=404, detail="Revenue data not found")

@app.get("/api/top-customers")
def get_top_customers():
    try:
        df = pd.read_csv(os.path.join(DATA_PATH, "top_customers.csv"))
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=404, detail="Customer data not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)