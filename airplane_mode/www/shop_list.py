import frappe

def get_context(context):
    context.avaliable_shops = frappe.db.get_all(
        "Shop", filters={"status": "Available"},fields=["*"]
	)
    return context