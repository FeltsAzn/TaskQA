import uvicorn
from fastapi import FastAPI
from fastapi_app.verify.heandlers import router


app = FastAPI(title='Digital signature',
              description='Endpoints for providing a digital signature and verifying it',
              version='0.0.1')
app.include_router(router=router)

if __name__ == '__main__':
    uvicorn.run("fastapi_app.start_app:app", host="127.0.0.1", port=8000, reload=True)



