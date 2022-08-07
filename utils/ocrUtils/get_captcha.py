import pytesseract
import base64

from PIL import Image
from common.config import PathConfig

cache_path = PathConfig.cache_path


def get_captcha(code_url):
    """
    将base64码生成图片验证码并识别
    """
    code = code_url.split(',')[-1]
    imgdata = base64.b64decode(code)
    with open(cache_path+'captcha.png', 'wb') as f:
        f.write(imgdata)
    code_img = Image.open(cache_path+'captcha.png')
    code_txt = pytesseract.image_to_string(code_img, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

    return code_txt[:6]


if __name__ == '__main__':
    a = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAAAgCAIAAABrSUp5AAABG0lEQVR42u2ZwRICIQxD+/8/rQePzrJpkrI4hivGdh5ZWqBeGfCoIAiswPpRWAWMwPp7WIUNkBqBdR2OW4kJiQQL+aUCy7V+t7xACQ/LRVaREEZWEivclldTio8Wf/WZamUFJkZLUFhEANwX3ZpAELmK0pKU0VaLWUIyB4tOrJTmQCxzHCzC77Ow6rnB1dxTYNlz2gNrvZlykk2wJro5l38bhbtbmxWUlkPSxMfugTXqO6TVIhLgoiCS6trK3gcY+yxvlPs+i/Cqi9T5ksJtJcLi6hdx3AG3OSIx3hfTB+mh0vm9DORBWtlolZsT1y0FEaUlqdbWLt6xEb3CUZI8WOR1Z6Z9DazAyme42VyB5b5sExvRM99fA2v3eAMDu1r3TGgstQAAAABJRU5ErkJggg=='
    codes = get_captcha(a)
    print(codes)