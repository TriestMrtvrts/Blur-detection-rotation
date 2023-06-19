from PIL import Image, ImageOps

def resize(image_path, size=224):
    image = Image.open(image_path)
    if image.mode != 'RGB':
            image = image.convert('RGB')
    
    resized_image = ImageOps.pad(image, (size, size), color='black')
    
    return resized_image

#resize('./DSC_0252.JPG').show()