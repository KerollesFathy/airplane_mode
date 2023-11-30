# Copyright (c) 2023, k.fathy@axentor.co and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
import unittest
from frappe.website.website_generator import WebsiteGenerator
from unittest.mock import MagicMock
from airplane_mode.airplane_mode.doctype.airplane_flight.airplane_flight import AirplaneFlight

class TestAirplaneFlight(FrappeTestCase):
    def setUp(self):
        # Create a test document before each test
        self.flight = frappe.get_doc({
            "doctype": "Airplane Flight",
            "status": "Scheduled",
        }).insert(ignore_permissions=True, ignore_mandatory=True)

        
    def tearDown(self):
        # Delete the test document after each test
        frappe.delete_doc("Airplane Flight", self.flight.name, force=True)

    def test_on_submit_changes_status(self):
        # Ensure that on_submit changes the status to "Completed"
        self.assertEqual(self.flight.status, "Scheduled")

        # Call on_submit method
        self.flight.on_submit()

        # Check if the status is updated
        self.assertEqual(self.flight.status, "Completed")