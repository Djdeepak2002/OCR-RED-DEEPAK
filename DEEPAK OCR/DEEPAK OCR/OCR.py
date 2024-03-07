# # from PIL import Image
# # # import stat
# # import os

# # image = Image.open('sample.tiff')

# # width, height = image.size
# # new_size = (width//2, height//2)
# # resized_image = image.resize(new_size)

# # # image = Image.open('myimage.jpg')
# # # new_image = image.resize((300, 300))
# # # new_image.save('myimage_500.jpg')

# # new_image.save('./Output_folder/compressed_tifffile.tiff', optimize=True, quality=100)

# # original_size = os.path.getsize('sample.tiff')
# # compressed_size = os.path.getsize('compressed_tiff_file.tiff')

# # print("Original Size: ", original_size)
# # print("Compressed Size: ", compressed_size)


# # # file_stats = os.stat('sample.tiff')
# # # print(file_stats)
# # # file_stats = os.stat('compressed_tifffile.tiff')

# from PIL import Image
# import os

# image = Image.open('sample.tiff')
# print(image.info['dpi'])

# # width, height = image.size
# # new_size = (width//2, height//2)
# # resized_image = image.resize(new_size)

# # resized_image.save('./Output_folder/compressed_tifffile.tiff', optimize=True, quality=100)

# # original_size = os.path.getsize('sample.tiff')
# # compressed_size = os.path.getsize('./Output_folder/compressed_tifffile.tiff')

# # print("Original Size: ", original_size)
# # print("Compressed Size: ", compressed_size)


from PIL import Image

def get_image_dpi(image_path):
    try:
        with Image.open(image_path) as img:
            dpi = img.info.get('dpi')
            if dpi:
                return dpi
            else:
                return "DPI information not available for this image."
    except Exception as e:
        return f"Error: {e}"

image_path = r'DEEPAK OCR\sample.tiff'
dpi_info = get_image_dpi(image_path)

print(f"DPI Information: {dpi_info}")