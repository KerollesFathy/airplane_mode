# Copyright (c) 2023, k.fathy@axentor.co and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Contract(Document):
	def validate(self):
		if frappe.db.get_value("Shop", self.shop, "status") == "Occupied":
			frappe.throw(f"Shop <b>{self.shop}</b> is not Avaliable for renting now")
