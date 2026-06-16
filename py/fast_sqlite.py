import sqlite3
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr

# Connects directly to your custom database module file
from SqliteEx import DatabaseManager

app = FastAPI(title="My BootCamp SQLite API", version="1.0.0")
db = DatabaseManager()

# ==========================================
# PYDANTIC MODEL SCHEMAS (Slide 4)
# ==========================================

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None
    created_at: str

class PostCreate(BaseModel):
    user_id: int
    title: str
    content: str

class PostResponse(BaseModel):
    id: int
    user_id: int
    title: str
    content: Optional[str] = None
    created_at: str

class PostResponseForUser(BaseModel):
    id: int
    title: str
    content: Optional[str] = None
    created_at: str

# ==========================================
# API ENDPOINT ROUTING LOGIC (Slides 5-8)
# ==========================================

@app.get("/")
async def root():
    return {"status": "Online", "database": db.db_name}

@app.post("/users/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    user_id = db.create_user(user.name, user.email, user.age)
    if user_id:
        return {"message": "User created successfully", "user_id": user_id}
    raise HTTPException(status_code=400, detail="Email already exists or invalid data.")

@app.get("/users/", response_model=List[UserResponse])
async def get_all_users():
    raw_users = db.get_all_users()
    return [
        UserResponse(id=u[0], name=u[1], email=u[2], age=u[3], created_at=str(u[4]))
        for u in raw_users
    ]

@app.post("/posts/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate):
    post_id = db.create_post(post.user_id, post.title, post.content)
    if post_id:
        return {"message": "Post created successfully", "post_id": post_id}
    raise HTTPException(status_code=400, detail="Could not create post. Verify User ID.")

@app.get("/users/{user_id}/posts", response_model=List[PostResponseForUser])
async def get_user_posts(user_id: int):
    raw_posts = db.get_user_posts(user_id)
    return [
        PostResponseForUser(id=p[0], title=p[1], content=p[2], created_at=str(p[3]))
        for p in raw_posts
    ]

@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    success = db.delete_user(user_id)
    if success:
        return {"message": f"User {user_id} and their posts have been purged."}
    raise HTTPException(status_code=404, detail="User target profile not found.")

# ==========================================
# SERVER INITIALIZER (Slide 8)
# ==========================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fast_sqlite:app", host="127.0.0.1", port=8000, reload=True)
