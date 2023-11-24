from __future__ import unicode_literals
import frappe
from frappe import _


@frappe.whitelist(allow_guest=True)
def create_contact_us(contact_name, phone, query_type, message, email):
	contact = frappe.new_doc("Website Contact")
	contact.contact_name = contact_name	
	contact.email = email
	contact.phone = phone
	contact.message = message
	contact.query_type = query_type
	contact.save()
	