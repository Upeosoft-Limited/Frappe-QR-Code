// Copyright (c) 2023, Upeosoft Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('QR Code Settings', {
	validate: function(frm) {
		frappe.call({
			method: 'frappe_qrcode.services.rest.generate_qr_code',
			args: {
				"box_size":frm.doc.box_size,
				"border":frm.doc.border,
				"fill_color":frm.doc.fill_color,
				"back_color":frm.doc.back_color
				},
			callback:function (r) {
				let succes_message=r.message
				console.log(succes_message)
			}
		});
	}
});
