# USECASE NAME : IMAGE RESOLUTION TO 300*300 DPI
# DESCRIPTION : This usecase is to convert an image resolution from its original dpi to  300dpi.
# PRECONDITION : IMAGE FORMAT SHOULD BE TIFF FORMAT
# INPUT FILE : SAMPLE.TIFF
# EXPECTED OUTPUT FILE : OUTPUT_TIFF.TIFF
# DATE : 07-MARCH-2024
#  AUTHOR: DEEPAK JAKKUL



from PIL import Image



# image path for input file considering it is of tiff format
image_path = r'DEEPAK OCR\DEEPAK OCR\sample.tiff'


#desired dpi we want
desired_dpi = (300, 300)

# Function for getting image dpi Info
def get_image_dpi(image_path):
    try:
        with Image.open(image_path) as img:
            dpi = img.info.get('dpi')
            if dpi:
                return dpi
            else:
                return None
    except Exception as e:
        return f"Error: {e}"



# Function for changing image dpi to the required dpi we waant
def change_image_dpi(image_path, desired_dpi=(300, 300), output_path=None):
# def change_image_dpi(image_path, desired_dpi=(300, 300), output_path=None):
    try:
        with Image.open(image_path) as img:

            current_dpi = img.info.get('dpi')
            
            # comparing the input image dpi with the desired dpi 300*300 dpi
            if current_dpi != desired_dpi:
                img.info['dpi'] = desired_dpi

                # Convert to RGB if the image is in RGBA mode
                if img.mode == 'RGBA':
                    img = img.convert('RGB')

                if output_path:
                    img.save(output_path, dpi=desired_dpi)
                    return f"Image DPI changed to {desired_dpi}. Saved to {output_path}"
                else:
                    return f"Image DPI changed to {desired_dpi}. Changes not saved (output_path not provided)."
            else:
                return f"Image already has the desired DPI ({desired_dpi}). No changes made."
    except Exception as e:
        return f"Error: {e}"


#function calling for getting image dpi
current_dpi = get_image_dpi(image_path)
print(f"Current DPI: {current_dpi}")

#printing the result of  function call of change image dpi
result = change_image_dpi(image_path, desired_dpi, output_path='output_tiff.tiff')
print(result)