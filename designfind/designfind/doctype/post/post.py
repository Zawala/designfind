# Copyright (c) 2023, Zawala and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Post(WebsiteGenerator):
	def before_save(self):
		title=self.title
		title=title.lower()
		title=title.replace(" ", "_")
		self.route=title

	def get_context(self, context):
		context.post = frappe.db.get_value(
            "Post", self.name, ["name", "description", "owner", "title"], as_dict=True
        )
		print(context.post)
		
