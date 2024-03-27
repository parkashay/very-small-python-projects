from src.generate import GenerateQrCode

if __name__ == "__main__":
    qr = GenerateQrCode()
    data = input("Enter the text or link that you want to make a QR code of: ")
    try:
        qr.generate(data)
        print("The QR code has been created and exported to '/assets' directory.")
    except Exception as err:
        print(err)
