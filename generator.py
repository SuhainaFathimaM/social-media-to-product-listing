def generate_listing(description: str, media_path: str = None) -> str:
    """
    Generates a product listing based on the description and optional media (image/video).
    """
    media_info = f"Media included: {media_path}" if media_path else "No media provided."
    
    return f"Product Listing\n\nDescription: {description}\n{media_info}"
