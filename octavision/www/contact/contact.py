from __future__ import unicode_literals
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_contact_us(contact_name, company_name, phone, business_domain, no_of_employees, message, email):
	contact = frappe.new_doc("Website Contact")
	contact.contact_name = contact_name
	contact.company_name = company_name
	contact.email = email
	contact.phone = phone
	contact.message = message
	contact.business_domain = business_domain
	contact.no_of_employees = no_of_employees
	contact.save()
	