from oled.device import sh1106
from oled.render import canvas
from PIL import ImageFont, Image
import qrcode


def main():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=3,
    )
    qr.add_data('http://vincentstudio.info')
    qr.make(fit=True)
    img = qr.make_image()
    img.save('./images/code.png')

    oled = sh1106(port=0, address=0x3C)
    font = ImageFont.truetype('./fonts/C&C Red Alert [INET].ttf', 12)
    with canvas(oled) as draw:
        logo = Image.open('images/code.png')
        draw.bitmap((0, 1), logo, fill=1)
        draw.text((75, 20), 'Vincent', font=font, fill=1)
        draw.text((90, 32 ), 'Studio', font=font, fill=1)


if __name__ == "__main__":
    main()