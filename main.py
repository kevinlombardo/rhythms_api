from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# Example Cloudflare Stream API interaction
@app.get("/streams/")
def get_streams():
    return {"message": "This will connect to Cloudflare Stream API"}

# Example User API
class User(BaseModel):
    username: str
    password: str

@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.username} created (stub, replace with real DB logic)"}

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 9000)))