from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import motor.motor_asyncio
from bson import ObjectId

app = FastAPI()

# Connect to Mongo Atlas
# client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://admin:admin123@de-cluster.4ayns.mongodb.net/test")

import os
mongo_uri = os.environ.get("MONGO_URI")
client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)

db = client.game_assets_api

# Model for player scores
class PlayerScore(BaseModel):
    player_name: str
    score: int

# Upload and Get Sprites
@app.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):
    sprite_doc = {
        "filename": file.filename,
        "content_type": file.content_type
    }
    result = await db.sprite.insert_one(sprite_doc)
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}

@app.get("/sprites")
async def get_sprites():
    sprites = []
    async for sprite in db.sprite.find():
        sprite["_id"] = str(sprite["_id"])  # Convert ObjectId to string
        sprites.append(sprite)
    return sprites


# Upload and Get Audio Files
@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    content = await file.read()
    audio_doc = {"filename": file.filename, "content": content}
    result = await db.audio.insert_one(audio_doc)
    return {"message": "Audio file uploaded", "id": str(result.inserted_id)}

@app.get("/audio")
async def get_audio():
    audio_files = []
    async for audio in db.audio.find():
        audio["_id"] = str(audio["_id"])
        del audio["content"]  # remove binary content from response
        audio_files.append(audio)
    return audio_files

# Upload and Get Player Scores
@app.post("/player_score")
async def add_score(score: PlayerScore):
    score_doc = score.dict()
    result = await db.score.insert_one(score_doc)
    return {"message": "Score recorded", "id": str(result.inserted_id)}

@app.get("/scores")
async def get_scores():
    scores = []
    async for doc in db.score.find():
        doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
        scores.append(doc)
    return scores

