from fastapi import FastAPI,Form

app = FastAPI()


@app.get("/")
async def root_get():
    return {"message": "Hello World"}

@app.post("/", tags=["post测试结构"]
          ,deprecated=True)
async def root_post():
    return {"message": "Hello World post"}

@app.post("/item/")
async def from_item(name):
    return {"name": name}

@app.put("/")
async def root_put():
    return {"message": "Hello World put"}
    
@app.delete("/")
async def root_delete():
    return {"message": "Hello World delete"}
@app.post("/item1/")
async def from_item(name: str = Form(...),
                    password: str = Form(...)):
    print(f"name:{name},password:{password}")
    return {"name": name}