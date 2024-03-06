from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=['Basic'])
async def basic():
    return {"Ping": "Pong"}


# Get  --> Read Todo
@app.get("/todo", tags=['todos'])
async def get_todo():
    return {"data": todos}


# Post --> Create Todo
@app.post("/todo",  tags=['todos'])
async def add_todo(todo:dict):
    todos.append(todo)
    return {"data": "A todo has been added..!"}


# Put --> Update Todo 
@app.put("/todo/{id}",  tags=['todos'])
async def update_todo(id:int, body:dict):
    for todo in todos:
        if int((todo['id'])) == id:
            todo['Activity'] = body['Activity']
            return {"data": f"Todo with id {id} Successfully updated..!"}
    return{"data": f"Todo with this id num {id} not found :( "}


# Delete --> Delete Todo
@app.delete('/todo/{id}', tags=['todos'])
async def delete_todo(id: int):
    for todo in todos:
        if int(todo['id'])==id:
            todos.remove(todo)
            return {"data": f"todo with id {id} has been deleted"}
    return {
        "data": f"this id {id} has not found..!"
    }


todos = [
    {
        "id": "1",
        "Activity": "Wake-up early."
    },
    {
        "id": "2",
        "Activity": "Breakfast before 9 AM."
    },
    {
        "id": "3",
        "Activity": "Do skin care."
    },
     {
        "id": "4",
        "Activity": "Plan your next day."
    },
     {
        "id": "5",
        "Activity": "Dance chillax."

    }
]
