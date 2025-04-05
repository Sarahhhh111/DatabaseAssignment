~ Game Assets API – Database Essentials Assignment

This project is a RESTful API created using FastAPI and Python. It is designed to manage multimedia game assets such as sprites, audio files, and player scores. It connects to a MongoDB Atlas cloud database.

---

~ Technologies Used

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic
- Motor (MongoDB async driver)
- Python-dotenv
- MongoDB Atlas
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

