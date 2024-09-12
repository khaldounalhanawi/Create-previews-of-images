from PIL import Image

imagefile = r"C:\Users\Khaldoun\Desktop\delete\240902_Leipzig-Probstheida_Kam04_HIGH.jpg"

def resizeimage(imagefile):
    im = Image.open(imagefile)
    aspect = im.size[0] / im.size[1]

    width = 1000
    height = int(width / aspect)  # Cast to int since resize expects integer dimensions
    
    # Resize the image
    resized_im = im.resize((width, height))
    
    # save the resized image
    resized_im.save(imagefile)
    
    print('image resized')

resizeimage(imagefile)
