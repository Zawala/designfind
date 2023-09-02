
try:
	import frappe
	import json
	from frappe import _
	import frappe.www.list
	from frappe.utils import cstr
except Exception as e:
	print(f"import Failed")
#finally:
#	print(f"import Failed")

#main method executed on page load
def get_context(context):
	#order_by='price asc',
	
	print(frappe.db.exists({"doctype": "Portfolio", "owner": frappe.session.user}))
	if not frappe.db.exists({"doctype": "Portfolio", "owner": frappe.session.user}):
		frappe.msgprint('create profile')
		frappe.local.flags.redirect_location = "/new-profile/new"
		raise frappe.Redirect
	else:
		#posts=frappe.db.get_all('Post',fields=['Title', 'Description', 'owner', 'Image', 'Route'],  as_list=True, limit=2)
		#context.posts=posts
		pass

@frappe.whitelist()
def init_load(number):
	posts=frappe.db.get_all('Post',fields=['Title', 'Description', 'owner', 'Image', 'Route'],  as_list=True, limit=9)
	return posts

		
@frappe.whitelist()
def get_posts(number):
	length=int(number)+9
	posts=frappe.db.get_all('Post',fields=['Title', 'Description', 'owner', 'Image', 'Route'],  as_list=True, start=number, page_length=length)	
	return posts
