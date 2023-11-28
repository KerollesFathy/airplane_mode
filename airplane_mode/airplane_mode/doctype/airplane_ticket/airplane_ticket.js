// Copyright (c) 2023, k.fathy@axentor.co and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh: function(frm) {
		frm.add_custom_button("Assign Seat", () => {
			frappe.prompt([
					{"fieldname": "seat_no", "fieldtype": "Data", "label": "Seat Number", "reqd": 1}
				],
				function(values){
					frm.set_value("seat", values.seat_no);
					frm.save();
				},
				"Select Seat",
				"Assign"
			)
		} , "Actions")
	}
});
