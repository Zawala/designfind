import frappe

def get_context(context):
	# do your magic here
	
	if frappe.session.user=='Guest':
		frappe.throw(("You need to be logged in to access this page"), frappe.PermissionError)
	
	if not frappe.db.exists({"doctype": "Portfolio", "owner": frappe.session.user}):
		pass
	else:
		frappe.local.flags.redirect_location = "/board"
		raise frappe.Redirect
