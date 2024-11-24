import os
from PIL import Image
import tensorflow as tf
from moviepy.editor import VideoFileClip
import spacy

# Load the spaCy NLP model for text processing
nlp = spacy.load("en_core_web_sm")

# Load the MobileNetV2 model for image object detection
image_model = tf.keras.applications.MobileNetV2(weights="imagenet")

def save_uploaded_file(upload_file) -> str:
    """
    Save the uploaded file to the 'static/uploads' directory.
    """
    try:
        file_directory = "static/uploads"
        os.makedirs(file_directory, exist_ok=True)  # Ensure the directory exists

        file_location = os.path.join(file_directory, upload_file.filename)

        # Save the file to the directory
        with open(file_location, "wb") as file:
            file.write(upload_file.file.read())

        return file_location
    except Exception as e:
        raise RuntimeError(f"Error saving file: {e}")
    


def process_text(text: str) -> list:
    """
    Extract product-related terms from the input text using spaCy.
    """
    try:
        doc = nlp(text)
        # Extract entities related to products or organizations
        products = [ent.text for ent in doc.ents if ent.label_ in ["PRODUCT", "ORG"]]
        return products
    except Exception as e:
        raise RuntimeError(f"Error processing text: {e}")

def process_image(image_path: str) -> list:
    """
    Detect objects in an image using the MobileNetV2 model.
    """
    try:
        img = Image.open(image_path).resize((224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
        img_array = tf.expand_dims(img_array, axis=0)

        # Predict top labels
        preds = image_model.predict(img_array)
        decoded_preds = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=5)

        # Extract the labels
        detected_objects = [label[1] for label in decoded_preds[0]]
        return detected_objects
    except Exception as e:
        raise RuntimeError(f"Error processing image: {e}")

def process_video(video_path: str) -> list:
    """
    Extract keyframes from a video and detect objects in them.
    """
    try:
        clip = VideoFileClip(video_path)
        frame_times = [5, 10, 15]  # Keyframe times (seconds)
        detected_products = []

        for t in frame_times:
            try:
                # Extract the keyframe from the video
                frame = clip.get_frame(t)

                # Directly pass the frame to process_image for object detection
                detected_products.extend(process_image(frame))  # Process directly without saving the frame to disk
            except Exception as e:
                print(f"Error processing frame at {t}s: {e}")

        clip.close()
        return list(set(detected_products))  # Remove duplicates
    except Exception as e:
        raise RuntimeError(f"Error processing video: {e}")

def combine_results(text_results: list, image_results: list, video_results: list) -> dict:
    """
    Combine results from text, image, and video processing into a unified dictionary.
    """
    result = {
        "Text Results": text_results if text_results else [],
        "Image Results": image_results if image_results else [],
        "Video Results": video_results if video_results else []
    }
    return result
