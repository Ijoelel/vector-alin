from PIL import Image

def crop_png(path_image, path_result):
    # Buka gambar
    image_ori = Image.open(path_image)

    # Dapatkan objek dari mode warna (misalnya, 'RGB' atau 'RGBA')
    mode = image_ori.mode

    # Dapatkan ukuran gambar
    width, height = image_ori.size

    # Membaca warna dari tiap pixel
    pixel_colors = []
    border_x = []
    border_y = []

    pixel = 0

    for y in range(height):
        for x in range(width):
            pixel = image_ori.getpixel((x, y))

            if 255 not in pixel:
                border_x.append(x)
                border_y.append(y)

    max_x = max(border_x) + 2
    min_x = min(border_x) - 2
    max_y = max(border_y) + 2
    min_y = min(border_y) - 2

    crop_image = image_ori.crop([min_x, min_y, max_x, max_y])

    crop_image.save(path_result)

    return path_result