from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()
version = "1.0.0"

# Perform Health Check
@app.get("/health")
def get_health():
    return {"status": "ok"}

# Perform Version check
@app.get("/version")
def get_version():
    return {"version": version}

#Perform Environment Check
@app.get("/env")
def get_env():
    return {"environment": os.getenv("ENVIRONMENT", "default")}

#Perform Configuration Creation
#Input Validation
config_store: dict[str, str] = {}

class ConfigItem(BaseModel):
    name: str
    value: str

@app.post("/config")
def create_config(item: ConfigItem):
    config_store[item.name] = item.value
    return {"name": item.name, "value": item.value}

# Perform Config Name Query
@app.get("/config/{name}")
def get_config(name: str):
    if name not in config_store:
        raise HTTPException(status_code=404, detail="Config not found")
    return {"name": name, "value": config_store[name]}

# Perform Entry Deletion
@app.delete("/config/{name}")
def delete_config(name: str):
    if name not in config_store:
        raise HTTPException(status_code=404, detail="Config not found")
    del config_store[name]
    return {"deleted": True}