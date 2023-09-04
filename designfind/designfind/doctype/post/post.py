# Copyright (c) 2023, Zawala and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Post(WebsiteGenerator):
	def before_save(self):
		title=self.title
		title=title.lower()
		title=title.replace(" ", "_")
		self.route=f'post/{title}'
		self.is_published=True

	def get_context(self, context):
		if frappe.session.user=='Guest':
			frappe.throw(("You need to be logged in to access this page"), frappe.PermissionError)
		context.show_sidebar=True

		context.post = frappe.db.get_value("Post", self.name, ["name", "description", "owner", "title"], as_dict=True)
		bio=frappe.db.get_value('Portfolio',{'owner': frappe.session.user},['bio', 'username'], as_dict=True)
		if context.post['owner']== frappe.session.user:
			context.is_owner=True
		context.person=bio
		context.csrf_token = frappe.local.session.data.csrf_token


@frappe.whitelist()
def delete_post(name):
	print(name)