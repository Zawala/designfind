import frappe

def get_context(context):
	if frappe.session.user=='Guest':
		frappe.throw(("You need to be logged in to access this page"), frappe.PermissionError)
	