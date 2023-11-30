// Copyright (c) 2023, k.fathy@axentor.co and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Flight', {
	refresh: function(frm) {
		frm.set_query("member", "members", function (doc, cdt, cdn) {
			return {
				filters: [
					["Flight Passenger", "is_crew_member", "=", true] 
				]
			}
		});

		frm.set_query("gate", function (doc, cdt, cdn) {
			return {
				filters: [
					["Gate", "code", "=", frm.doc.source_airport_code] 
				]
			}
			
		});
	}
});
