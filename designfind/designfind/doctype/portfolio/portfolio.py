# Copyright (c) 2023, Zawala and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Portfolio(WebsiteGenerator):
	def before_save(self):
		if not frappe.db.exists({"doctype": "Portfolio", "username": self.username}):
			self.route=f'portfolio/{self.username}'
			self.is_published=True
			user = frappe.get_doc({
				"doctype":"User",
				"first_name":self.username,
				})
			user = frappe.get_doc('User', frappe.session.user)
			user.user_image=self.profile_picture
			user.save(
			ignore_permissions=True, # ignore write permissions during insert
		)
			self.create_inbox(self.username)

	def create_inbox(self, username):
		doc = frappe.new_doc('Inbox')
		doc.is_published=True
		doc.user=self.username
		doc.route=f'inbox/{username}'
		doc.insert(
			ignore_permissions=True, # ignore write permissions during insert
		)




	def get_context(self, context):
		if frappe.session.user=='Guest':
			frappe.throw(("You need to be logged in to access this page"), frappe.PermissionError)
	
		person=frappe.db.get_value('Portfolio',{'owner': frappe.session.user},['bio', 'username'], as_dict=True)
		posts=frappe.db.get_list('Post', filters={'owner':  frappe.session.user},fields=['title', 'route', 'creation'],)
		context.posts=posts
		context.person=person
