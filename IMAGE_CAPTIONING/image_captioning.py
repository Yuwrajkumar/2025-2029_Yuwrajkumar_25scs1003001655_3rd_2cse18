                                                 # TASK 3 - IMAGE CAPTIONING AI
                                                    # Internship Project


from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# Load Pre-trained BLIP Model

print("Loading Image Captioning Model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("Model loaded successfully!")

# Select Image

image_path = input(
    "\nEnter the path of your image: "
).strip()


# Open Image

try:

    image = Image.open(image_path).convert("RGB")

except FileNotFoundError:

    print("Error: Image file not found.")
    exit()

except Exception as e:

    print("Error opening image:", e)
    exit()


# Process Image

print("\nAnalyzing image...")

inputs = processor(
    images=image,
    return_tensors="pt"
)


# Generate Caption

with torch.no_grad():

    output = model.generate(
        **inputs,
        max_new_tokens=50
    )

# Convert Output to Text

caption = processor.decode(
    output[0],
    skip_special_tokens=True
)

# Display Result

print("\n======================================")
print("          IMAGE CAPTION")
print("======================================")

print("Image:", image_path)
print("Caption:", caption)

print("======================================")