import frappe
from frappe.utils import now_datetime, get_first_day, get_last_day, getdate, add_months
from datetime import timedelta

def send_rent_due_reminder():
    
    if not frappe.db.get_single_value("Airport Shop Settings", "enable_rent_reminder"):
        return
    
    # Get the current date and time
    current_datetime = now_datetime()

    # Get tenants with rent due in the current month
    tenants_due = frappe.get_all(
        "Contract",
        filters={
            "docstatus": 1,  # Approved contracts
            "date_of_expiry": (">=", current_datetime),
        },
        fields=["name", "tenant", "shop", "date_of_expiry", "rent_amount"],
    )
    email_template = frappe.db.get_single_value("Airport Shop Settings", "email_template")
    template = frappe.get_doc("Email Template", email_template)
    # Send email reminders to tenants
    for tenant_due in tenants_due:
        doc =  frappe.get_doc("Contract", tenant_due.get("name"))
        subject = frappe.render_template(template.subject, {"doc": doc})
        message = frappe.render_template(template.response, {"doc": doc})
        send_email_reminder(tenant_due, subject, message)

def send_email_reminder(tenant_due, subject, message):
    tenant_name = tenant_due.get("tenant")
    
    # Get the tenant's email address
    tenant_contact = frappe.db.get_value("Tenant", tenant_name, "contact")
    tenant_email = frappe.db.get_value("Contact", tenant_contact, "email_id")

    # Send the email
    if tenant_email:
    	frappe.sendmail(
			recipients=tenant_email,
            sender="notifications@example.com",
			subject=subject,
			message=message,
		)

