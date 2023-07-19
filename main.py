from fastapi import FastAPI, Request

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# function and config
from database.index import connection 

# controller
from controller.addItemController import create_item

app = FastAPI()

# middlewares
# serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# configuration
# database config connection 
connection()


@app.get("/",response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})


@app.post("/items/")
def call_func():
    create_item()



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)