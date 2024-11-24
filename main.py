from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import shutil
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from fastapi import Request
from .utils import save_uploaded_file, process_text, process_image, process_video, combine_results
from .generator import generate_listing

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
# Load the pre-trained model (MobileNetV2)
model = MobileNetV2(weights="imagenet")

# Ensure a folder exists to save the uploaded and processed images
UPLOAD_DIR = Path("static/uploads")
PROCESSED_DIR = Path("static/processed")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Root endpoint - serve a simple message or HTML page
@app.get("/")
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), text: str = None):
    try:
        # Handle file upload
        if file:
            file_location = save_uploaded_file(file)
            file_extension = file.filename.split('.')[-1].lower()

            # Process the file (Image or Video)
            if file_extension in ['jpg', 'jpeg', 'png']:
                detected_objects = process_image(file_location)
                media_type = "image"
            elif file_extension in ['mp4', 'mov', 'avi']:
                detected_objects = process_video(file_location)
                media_type = "video"
            else:
                return JSONResponse(status_code=400, content={"error": "Invalid file type"})

            # Generate listing based on detected objects
            media_path = f"/static/processed/{file.filename}"
        else:
            detected_objects = []
            media_type = None
            media_path = None

        # Process the description text if provided
        text_results = process_text(text) if text else []

        # Combine results
        combined_results = combine_results(text_results, detected_objects, [])

        # Generate the final product listing
        product_listing = generate_listing(description=text, media_path=media_path)

        # Return the results
        return JSONResponse(content={
            "product_listing": product_listing,
            "processed_file_url": media_path,
            "combined_results": combined_results
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/static/{file_name}")
async def get_processed_file(file_name: str):
    file_location = PROCESSED_DIR / file_name
    if file_location.exists():
        return FileResponse(file_location)
    else:
        return JSONResponse(status_code=404, content={"error": "File not found"})
