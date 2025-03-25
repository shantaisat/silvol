from dotenv import load_dotenv
import os
import cloudinary
import cloudinary.api

# Load environment variables from .env file
load_dotenv()  # This will load the .env file from the root directory

# Configure Cloudinary using the CLOUDINARY_URL from .env
cloudinary.config(
    cloudinary_url=os.getenv("CLOUDINARY_URL")  # Use the full CLOUDINARY_URL directly
)

try:
    # Test the connection
    response = cloudinary.api.ping()
    print("Cloudinary Connection Successful:", response)

    # List all uploaded resources
    resources = cloudinary.api.resources()
    print("Uploaded Resources:", resources)

except Exception as e:
    print("Cloudinary Connection Failed:", e)
    print("CLOUDINARY_URL:", os.getenv("CLOUDINARY_URL"))