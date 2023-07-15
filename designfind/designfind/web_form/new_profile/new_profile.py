import frappe

def get_context(context):
	# do your magic here
	if not frappe.db.exists({"doctype": "Portfolio", "owner": frappe.session.user}):
		pass
	else:
		frappe.local.flags.redirect_location = "/board"
		raise frappe.Redirect
