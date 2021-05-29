import os
from PIL import Image


def main():
    # 读取图片
    im = Image.open('aa.jpg')

    # 宽高各除 3，获取裁剪后的单张图片大小
    width = im.size[0] // 3
    height = im.size[1] // 3

    # 裁剪图片的左上角坐标
    start_x = 0
    start_y = 0

    # 用于给图片命名
    im_name = 1

    # 循环裁剪图片
    for i in range(3):
        for j in range(3):
            # 裁剪图片并保存
            crop = im.crop((start_x, start_y, start_x + width, start_y + height))
            # 判断文件夹是否存在
            if not os.path.exists('imgs'):
                os.mkdir('imgs')
            crop.save('imgs/' + str(im_name) + '.jpg')

            # 将左上角坐标的 x 轴向右移动
            start_x += width
            im_name += 1

        # 当第一行裁剪完后 x 继续从 0 开始裁剪
        start_x = 0
        # 裁剪第二行
        start_y += height


if __name__ == '__main__':
    main()
