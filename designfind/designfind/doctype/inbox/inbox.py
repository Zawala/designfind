# Copyright (c) 2023, Zawala and contributors
# For license information, please see license.txt

import frappe
import smtplib
from frappe.website.website_generator import WebsiteGenerator

class Inbox(WebsiteGenerator):
	pass





	def get_context(self, context):
		context.designer=self.user



@frappe.whitelist()
def send_mail(name):
	#code to send mail
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls() 
	server.login('your_email@gmail.com', 'your_password')
	msg = f"Hello, {frappe.session.user} wants to give you work send them an email"  
	server.sendmail('from@email.com', 'to@email.com', msg)
	server.quit()