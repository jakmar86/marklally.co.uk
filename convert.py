from PIL import Image

# Open the WebP image
image = Image.open('0_2.webp')

# Convert it to RGB format
image = image.convert('RGB')

# Save as a JPG
image.save('0_2.jpg', 'jpeg')