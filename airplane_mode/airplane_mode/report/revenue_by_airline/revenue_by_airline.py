# Copyright (c) 2023, k.fathy@axentor.co and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import cint


def execute(filters=None):
	columns, data = get_columns(filters), get_data(filters)
	total_revenue = sum([x.get("revenue") for x in data])
	report_summary = [
	{"label":"Total Revenue","value": total_revenue,"indicator":"Green"},
	]
	chart = get_chart(data)
	return columns, data, None, chart, report_summary

def get_data(filters=None):
	q = """
		SELECT
   			airli.name AS "airline",
    		COALESCE(SUM(subquery.total_amount), 0) AS "revenue"
		FROM
    		tabAirline airli
		LEFT JOIN (
			SELECT
				airli.name AS airline,
				COALESCE(SUM(ticket.total_amount), 0) AS total_amount
			FROM
				tabAirline airli
			LEFT JOIN tabAirplane airpla ON airli.name = airpla.airline
			LEFT JOIN `tabAirplane Flight` flight ON flight.airplane = airpla.name
			LEFT JOIN `tabAirplane Ticket` ticket ON flight.name = ticket.flight
			GROUP BY airli.name
		) AS subquery ON airli.name = subquery.airline
		GROUP BY airli.name;
	"""
	return frappe.db.sql(q, as_dict=True)


def get_columns(filters=None):
	return [
		{
			"label": "Airline",
			"fieldname": "airline",
			"fieldtype": "Link",
			"options": "Airline",
			"width": 200
		},
		{
			"label": "Revenue",
			"fieldname": "revenue",
			"fieldtype": "Currency",
			"width": 200
		}
	]

def get_chart(data=None):
	chart = {
		"data":{
			"labels":[ x.get("airline") for x in data],
			"datasets":[{"values":[ x.get("revenue") for x in data]}]
			},
		"type":"donut"
		}
	return chart
