import base64

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def generate_email_body(image1_base64, image2_base64):
    body = f'''
        <p style="color: #a6a698; font-size:13px; font-family: Arial, sans-serif;">Regards,</p>
        <br>
        <p style="color: black; font-size: 14px; font-family: Calibri, sans-serif; font-weight: bold; margin: 0; padding:0;margin-bottom: 3px">IT OPERATIONS</p>
        <p style="color: #a6a698; font-size:13px; font-family: Arial, sans-serif; margin: 0; padding:0;margin-bottom: 3px">Group Digital, Technology & Transformation</p>
        <p style="color: #a6a698; font-size: 13px; font-family: Arial, sans-serif; font-weight: bold; margin: 0; padding:0;margin-bottom: 3px">Kenanga Investment Bank Berhad</p>
        <p style="color: #a6a698; font-size: 12px; font-family: Arial, sans-serif; margin: 0; padding:0;margin-bottom: 3px">Level 6, Kenanga Tower</p>
        <p style="color: #a6a698; font-size: 12px; font-family: Arial, sans-serif;margin: 0; padding:0;margin-bottom: 4px">237, Jalan Tun Razak, 50400 Kuala Lumpur</p>
        <p style="color: #4472c4; font-size: 11px; font-family: Arial, sans-serif;margin: 0; padding:0;margin-bottom: 3px">Tel: GL +60 3 21722888 (Ext:8364 / 8365 / 8366 / 8357) </p>
        <br>
        <img src="data:image/png;base64, {image1_base64}" alt="image1"> <!-- Embed image1 -->
        <br>
        <img src="data:image/png;base64, {image2_base64}" alt="image2" > <!-- Embed image2 -->
    '''
    return body

# Images path:
image1_path = 'images/image1.png'
image2_path = 'images/image2.png'

image1_base64 = get_base64_encoded_image(image1_path)
image2_base64 = get_base64_encoded_image(image2_path)
