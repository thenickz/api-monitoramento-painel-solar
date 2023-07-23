from fastapi import FastAPI
from routes import root, solar_painel, arduino_lora_receptor


app = FastAPI()
app.include_router(root.router)
app.include_router(solar_painel.router)
app.include_router(arduino_lora_receptor.router)
