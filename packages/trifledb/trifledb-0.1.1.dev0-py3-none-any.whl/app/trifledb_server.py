from fastapi import FastAPI, Request
from fastapi_versioning import VersionedFastAPI, version
from app.trifledb import TrifleDB

app = FastAPI(title="TrifleDB key-value store")
trifledb = TrifleDB()

@app.get("/{key}")
@version(1)
def get(key: str):
    value = trifledb[key]
    if not value:
        return "key not found"
    return value

@app.post("/{key}", status_code=200)
@version(1)
async def put(key: str, request: Request):
    trifledb[key] = await request.body()
    return True
    
app = VersionedFastAPI(app,
    version_format='{major}',
    prefix_format='/v{major}',
    enable_latest=True)