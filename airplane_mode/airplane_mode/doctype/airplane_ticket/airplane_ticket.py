# Copyright (c) 2023, k.fathy@axentor.co and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string

class AirplaneTicket(Document):

	def before_insert(self):
		self.generate_seat_number()
		
	def before_submit(self):
		if self.status != "Boarded":
			help_info =  "<span class='text-muted'>help: change the status to Boarded to be able submit the ticket :) </span>"
			frappe.throw(f"u can't submit the ticket with status <b>{self.status}</b><hr> {help_info}")

	def validate(self):
		self.validate_unique_add_ons()
		self.calculate_total_amount()



	def validate_unique_add_ons(self):
		unique_add_ons = self.get_unique_add_ons()
		if len(unique_add_ons):
			# update idxs
			unique_add_ons = [item.update({"idx": index}) for index, item in enumerate(unique_add_ons, start=1)]
			self.update({"add_ons": unique_add_ons})

	def calculate_total_amount(self):
		total_add_ons_amount = 0.0
		for add_on in self.add_ons:
			total_add_ons_amount += add_on.amount
		self.total_amount = self.flight_price + total_add_ons_amount
	
	def get_unique_add_ons(self):
		unique_add_ons = []
		seen_items = set()

		for row in self.get("add_ons"):
			if row.get("item") not in seen_items:
				unique_add_ons.append(row)
				seen_items.add(row.get("item"))

		return unique_add_ons
	
	def generate_seat_number(self):
		random_integer = random.randint(10, 100)
		random_alphabet = random.choice(string.ascii_uppercase)
		self.seat = f"{random_integer}{random_alphabet}"




