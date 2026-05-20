import os
import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Create output directory

os.makedirs("output", exist_ok=True)

print("\n=== QR Code Generator ===\n")

# User input

data = input("Enter URL or text: ").strip()

if not data:
print("Error: Input cannot be empty.")
exit()

# Custom filename

filename = input("Enter filename (without extension): ").strip()

if not filename:
filename = "generated_qr"

# Create QR object

qr = qrcode.QRCode(
version=1,
error_correction=ERROR_CORRECT_H,
box_size=10,
border=4,
)

# Add data

qr.add_data(data)
qr.make(fit=True)

# Create image

img = qr.make_image(
fill_color="black",
back_color="white"
)

# Save image

filepath = f"output/{filename}.png"
img.save(filepath)

print(f"\nQR code successfully saved to:")
print(filepath)

