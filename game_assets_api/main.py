from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import motor.motor_asyncio

app = FastAPI()

# Connect to Mongo Atlas
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://admin:admin123@de-cluster.4ayns.mongodb.net/test")
db = client.game_assets_api

class PlayerScore(BaseModel):
    player_name: str
    score: int

@app.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):
    sprite_doc = {
        "filename": file.filename,
        "content_type": file.content_type
    }
    result = await db.assets.insert_one(sprite_doc)
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}


@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    content = await file.read()
    audio_doc = {"filename": file.filename, "content": content}
    result = await db.audio.insert_one(audio_doc)
    return {"message": "Audio file uploaded", "id": str(result.inserted_id)}

@app.post("/player_score")
async def add_score(score: PlayerScore):
    score_doc = score.dict()
    result = await db.scores.insert_one(score_doc)
    return {"message": "Score recorded", "id": str(result.inserted_id)}