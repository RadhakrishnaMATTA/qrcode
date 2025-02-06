import qrcode
from IPython.display import Image

# Get data type from user
data_type = input("Enter data type (video, pdf, link, text): ").lower()

# Get data based on type
if data_type == "video":
    data = input("Enter YouTube video link: ")
elif data_type == "pdf":
    data = input("Enter PDF file path: ") 
elif data_type == "link":
    data = input("Enter website link: ")
else:  # Default to text if invalid type
    data_type = "text"
    data = input("Enter text data: ")

# Creating an instance of QRCode class
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=5,
)

# Adding data to the instance 'qr'
qr.add_data(data)
qr.make(fit=True)

# Generate and save the QR code image
img = qr.make_image(fill_color="black", back_color="white")
f = input("Name the QR code file: ")
img.save(f"{f}.png")

print(f"QR code for {data_type} generated and saved as {f}.png")

# Display the image
display(Image(filename=f"{f}.png"))
