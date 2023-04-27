import frappe
import qrcode
import base64
from io import BytesIO


def generate_qr_code(**kwargs):
    qrCode=qrcode.QRCode(version=1,box_size=kwargs['box_size'],border=kwargs['border'])
    qrCode.add_data(kwargs['qrcode_data'])
    qrCode.make(fit=True)
    qr_image=qrCode.make_image(fill_color=kwargs['fill_color'],back_color=kwargs['back_color'])
    image= BytesIO()
    qr_image.save(image, format='PNG')
    image.seek(0)
    base_64_image="data:image/png;base64,"+base64.b64encode(image.getvalue()).decode('utf-8')
    return base_64_image