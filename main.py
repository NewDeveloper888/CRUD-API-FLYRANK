from fastapi import FastAPI


# create app instance
app = FastAPI(
    title="Task API",
    version="1.0"
)


@app.get('/')
async def read_root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health")
def get_health():
    return {
        "status": "ok"
    }



    
