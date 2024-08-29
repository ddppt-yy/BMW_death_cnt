import base64

# 读取 .ico 文件并转换为 Base64
def ico_to_base64(ico_path, txt_path):
    with open(ico_path, 'rb') as ico_file:
        ico_data = ico_file.read()
        base64_data = base64.b64encode(ico_data).decode('utf-8')
    
    # 将 Base64 数据写入 .txt 文件
    with open(txt_path, 'w') as txt_file:
        txt_file.write(base64_data)

if __name__ == "__main__":
    ico_to_base64('icon.ico', 'ico_base64.txt')
    ico_to_base64('icon.png', 'png_base64.txt')
    ico_to_base64('icon.jpg', 'jpg_base64.txt')
    ico_to_base64('template.png', 'tmp_base64.txt')
