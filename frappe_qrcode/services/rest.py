import frappe
import qrcode
import base64
from io import BytesIO


@frappe.whitelist()
def generate_qr_code(box_size, border, fill_color="black", back_color="white", qrcode_data=None):
    qrCode=qrcode.QRCode(version=1,box_size=box_size,border=border)
    qrCode.add_data(qrcode_data)
    qrCode.make(fit=True)
    qr_image=qrCode.make_image(fill_color=fill_color,back_color=back_color)
    image= BytesIO()
    qr_image.save(image, format='PNG')
    image.seek(0)
    base_64_image="data:image/png;base64,"+base64.b64encode(image.getvalue()).decode('utf-8')
    return base_64_image