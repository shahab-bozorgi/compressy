from PIL import Image, ImageOps

def compress_to_webp(input_path, output_path, quality=80, max_width=None):
    img = Image.open(input_path)
    img = ImageOps.exif_transpose(img)

    if max_width and img.width > max_width:
        ratio = max_width / img.width
        new_height = int(img.height * ratio)
        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
    
    img.save(output_path, 'WEBP', quality=quality, method=6) 
