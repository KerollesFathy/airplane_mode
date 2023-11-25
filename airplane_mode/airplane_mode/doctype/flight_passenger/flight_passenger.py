# Copyright (c) 2023, k.fathy@axentor.co and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FlightPassenger(Document):
	def before_save(self):
		self.full_name = self.first_name + " " +  self.last_name
	
	def validate(self):
		if not self.last_name:
			frappe.throw("Please set last name")
