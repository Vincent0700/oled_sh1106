from oled.device import sh1106
from oled.render import canvas
from PIL import ImageFont, Image


def main():
    oled = sh1106(port=0, address=0x3C)
    font = ImageFont.truetype('./fonts/C&C Red Alert [INET].ttf', 12)
    with canvas(oled) as draw:
        # draw.text((0, 0), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', font=font, fill=255)
        logo = Image.open('examples/images/pi_logo.png')
        draw.bitmap((0, 0), logo, fill=1)


if __name__ == "__main__":
    main()
