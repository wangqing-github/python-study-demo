from PIL import Image, ImageDraw, ImageFont
# 解决读取图片报错
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os


# 获取文字
def gen_text_img(text, font_size, font_path=None):
    '''
    输入：
    text：照片墙的样式文字
    font_size：字体的大小
    font_path：字体
    返回：
    文字图像
    '''
    font = ImageFont.truetype(font_path, font_size)
    (width, length) = font.getsize(text)
    text_img = Image.new('RGBA', (width, length))
    draw = ImageDraw.Draw(text_img)
    # 从左上角开始绘制
    draw.text((0, 0), text, fill=(0, 0, 0), font=font)
    return text_img


def trans_alpha(img, pixel):
    '''
    R：红
    G：绿
    B：蓝
    A：透明
    '''
    _, _, _, alpha = img.split()
    alpha = alpha.point(lambda i: pixel[-1] * 10)
    img.putalpha(alpha)
    return img


def picture_wall_mask(text_img, edge_len, pic_dir):
    '''
    输入：
    text_img：文字图像
    edge_len：照片边长（用于扩大像素）
    pic_dir：路径
    '''
    # 像素扩大
    new_img = Image.new(
        'RGBA', (text_img.size[0] * edge_len, text_img.size[1] * edge_len))
    file_list = os.listdir(pic_dir)
    img_index = 0
    for x in range(0, text_img.size[0]):
        for y in range(0, text_img.size[1]):
            pixel = text_img.getpixel((x, y))
            file_name = file_list[img_index % len(file_list)]
            try:
                # 导入图片
                img = Image.open(os.path.join(pic_dir, file_name)).convert(
                    'RGBA')
                img = img.resize((edge_len, edge_len))
                img = trans_alpha(img, pixel)
                # 进行替换
                new_img.paste(img,
                              (x * edge_len, y * edge_len))
                img_index += 1
            except Exception as e:
                print(f"文件打开失败：{file_name} + {e}")
    return new_img


def main(text='我全都要',
         font_size=20,
         edge_len=60,
         pic_dir="./wall",
         out_dir="./out",
         font_path='buzz_cloud_font.ttf'):
    '''
    生成照片墙
    :param text: 照片墙字符样式
    :param font_size: 字体大小
    :param edge_len: sub picture's egde length
    '''
    if len(text) >= 1:
        text_ = ' '.join(text)
        print(f"generate text wall for '{text_}' with picture path:{pic_dir}")
        text_img = gen_text_img(text_, font_size, font_path)
        img_ascii = picture_wall_mask(text_img, edge_len, pic_dir)
        img_ascii.save(out_dir + os.path.sep + ''.join(text) + '.png')


if __name__ == '__main__':
    main()



