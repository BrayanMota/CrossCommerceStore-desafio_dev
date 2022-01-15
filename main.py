from fastapi import FastAPI

app = FastAPI()


@app.get('/hello_world')
def hello():
    return 'Hello Peter'
