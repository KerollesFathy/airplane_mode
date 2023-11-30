# Copyright (c) 2023, k.fathy@axentor.co and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestFlightPassenger(FrappeTestCase):
       
	def setUp(self):
        # Create a test instance of FlightPassenger
		self.flight_passenger = frappe.get_doc({
			"doctype": "Flight Passenger",
			"first_name": "John",
			"last_name": "Doe"
		})

	def tearDown(self):
		# Delete the test document after each test
		if self.flight_passenger.get("name"):
			frappe.delete_doc("Flight Passenger", self.flight_passenger.name, force=True)

	def test_before_save_concatenates_names(self):
		# Ensure that before_save concatenates first and last names
		self.assertEqual(self.flight_passenger.full_name, None)

		# Call before_save method
		self.flight_passenger.before_save()

		# Check if the full_name is concatenated
		self.assertEqual(self.flight_passenger.full_name, "John Doe")

