from fastapi import FastAPI,HTTPException
import uvicorn
app = FastAPI()

jobs = [{
        "id": "uniqueId1",
        "title": "accountant",
        "description": "financial decisions"
    },
    {
        "id": "uniqueId2",
        "title": "housekeeper",
        "description": "cleans and sanitizes"
    },
    {
        "id": "uniqueId3",
        "title": "programmer",
        "description": "program management"
    }]


@app.get("/job")
def getJobs():
    return jobs
    
@app.get("/job/{id}")
def getJob(id):
    for job in jobs:
        if job["id"] == id:
            return job
    raise HTTPException(status_code=404, detail="Job with id" + id + "not found")

if __name__ =="_worker_":
    uvicorn.run(app, host="0.0.0.0", port=80)



