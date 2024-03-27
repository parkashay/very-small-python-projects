import qrcode
from datetime import datetime


class GenerateQrCode:

    # initialize the qrcode class
    def __init__(self) -> None:
        self.qrcode = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

    def generate(self, data):
        # add the data that needs to be converted to the qrcode
        self.qrcode.add_data(data)
        self.qrcode.make(fit=True)

        # change the color as needed. You can also provide rgb value like 'rgb(0,0,0)'
        generated_qr_img = self.qrcode.make_image(
            fill_color="black", back_color="white"
        )

        # generate a unique name for the file
        generated_name = int(datetime.now().timestamp())

        # save the png file into the /assets directory
        generated_qr_img.save(f"assets/{generated_name}_QR_Code.png")
