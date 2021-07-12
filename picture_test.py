from PIL import Image


def is_valid_image(path):
    """
    检查文件是否损坏
    """
    try:
        bValid = True
        fileObj = open(path, 'rb')  # 以二进制形式打开
        buf = fileObj.read()
        if not buf.startswith(b'\xff\xd8'):  # 是否以\xff\xd8开头
            bValid = False
        elif buf[6:10] in (b'JFIF', b'Exif'):  # “JFIF”的ASCII码
            if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):  # 是否以\xff\xd9结尾
                bValid = False
        else:
            try:
                Image.open(fileObj).verify()
            except Exception as e:
                bValid = False
                print(e)
    except Exception as e:
        return False
    return bValid


if __name__ == '__main__':
    res = is_valid_image(r'/home/wyj/PycharmProjects/0318/monitor-flask/myapi/resources/server_config_api/logo.jpg')
    print(res)
    res = is_valid_image(r'/home/wyj/图片/logo.jpg')
    print(res)
    res = is_valid_image(r'/home/wyj/图片/smile.png')
    print(res)
    res = is_valid_image(r'/home/wyj/图片/testflower.png')
    print(res)
    res = is_valid_image(r'/home/wyj/图片/2021.png')
    print(res)