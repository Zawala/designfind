# Copyright (c) 2023, Zawala and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Post(WebsiteGenerator):
	def before_save(self):
		title=self.title
		title=title.lower()
		title=title.replace(" ", "_")
		self.route=f'portfolio/{title}'
		self.is_published=True

	def get_context(self, context):
		context.post = frappe.db.get_value("Post", self.name, ["name", "description", "owner", "title"], as_dict=True)
		bio=frappe.db.get_value('Portfolio',{'owner': frappe.session.user},['bio', 'username'], as_dict=True)
		context.person=bio
		print(bio)
		
