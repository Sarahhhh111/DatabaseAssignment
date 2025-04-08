~ Game Assets API – Database Essentials Assignment

This project is a RESTful API created using FastAPI and Python. It allows uploading and retrieving sprites, audio files, and player scores, all stored in a MongoDB Atlas cloud database. The project is deployed using Railway for public access and tested locally using Postman.

---

~ Technologies Used

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic
- Motor (MongoDB async driver)
- Pydantic
- Python-dotenv
- MongoDB Atlas
- Postman (API Testing)
- Railway 
- Git (for version control)

---

~ Setup Instructions

Clone the repository
git clone https://github.com/Sarahhh111/DatabaseAssignment.git
cd DatabaseAssignment


Open VS Code & Create folder game_assest_api
Create Virtual Evnironment by entering whats needed in VS Code terminal:
python -m venv env

env\Scripts\activate

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

.\env\Scripts\activate

pip install fastapi uvicorn motor pydantic python-dotenv requests

To add requirements.txt:
pip freeze > requirements.txt

---

~ Deployment

The API is publicly deployed via Railway at:
https://databaseassignment-production.up.railway.app

You can test the API using Postman or access interactive docs at:
https://databaseassignment-production.up.railway.app/docs

https://databaseassignment-production.up.railway.app/sprites
https://databaseassignment-production.up.railway.app/audio
https://databaseassignment-production.up.railway.app/scores

---

~ Documentation

- Database Secuity
    - Secure Credentials: Used .env file and os.environ.get("MONGO_URI") to protect the MongoDB URI.
    - IP Whitelisting: Only specific IPs (e.g., Railway deployment server) are allowed in MongoDB Atlas.
    - Injection Prevention: Inputs are sanitized via Pydantic’s validation. Extra fields are disallowed using:
        class Config:
         extra = "forbid"

- Setup
    - FastAPI is used to create a modern RESTful API with automatic documentation.
    - motor.motor_asyncio is the async driver used to connect to MongoDB Atlas.
    - bson.ObjectId helps in converting MongoDB _id fields into strings.

- MongoDB Connection
    - Connects to MongoDB Atlas using your cluster URI.
    - Selects the game_assets_api database where all collections (sprites, audio, score) will be stored.

- Endpoints
- Upload Sprite
    - Method: POST
    - Route: /upload_sprite
    - Description: Uploads a sprite image’s metadata (filename and content type) to the sprite collection.

    - Database Interaction:
        - Inserts a new document in the sprite collection with the file's name and content type.

- Get Sprites
    - Method: GET
    - Route: /sprites
    - Description: Retrieves all uploaded sprite metadata from the database.

    - Database Interaction:
        - Queries all documents from the sprite collection.
        - Converts the MongoDB ObjectId to a string for readability.


- Upload Audio File
    - Method: POST
    - Route: /upload_audio
    - Description: Uploads an audio file’s binary content and metadata to the audio collection.

    - Database Interaction:
        - Stores the actual binary content (content) and filename into the audio collection.

- Get Audio Files
    - Method: GET
    - Route: /audio
    - Description: Lists uploaded audio file metadata without returning the full binary content.

    - Database Interaction:
        - Retrieves all documents from the audio collection but removes the binary content field before returning it to save bandwidth and processing time.


- Upload Player Score
    - Method: POST
    - Route: /player_score
    - Description: Submits a player’s name and score to the score collection.

    - Database Interaction:
        - Converts a submitted JSON body into a Python dictionary.
        - Inserts it into the score collection with two fields: player_name and score.

- Get Player Scores
    - Method: GET
    - Route: /scores
    - Description: Returns all player scores stored in the database.

    - Database Interaction:
        - Fetches all documents from the score collection.
        - Converts ObjectIds to strings for easy JSON display.

---

FINAL NOTE:
imp urls:
Public Git URL	Your GitHub repo link → https://github.com/Sarahhh111/DatabaseAssignment
Public API URL	Railway deployed API → https://databaseassignment-production.up.railway.app

Thank you for reading!
-Sarah Galea