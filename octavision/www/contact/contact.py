from __future__ import unicode_literals
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_contact_us(contact_name, phone, message, email):
    try:
        print("Creating contact...")
        contact = frappe.new_doc("Website Contact")
        contact.contact_name = contact_name
        contact.email = email
        contact.phone = phone
        contact.message = message
        contact.save()
        print("Contact saved successfully!")
        frappe.msgprint("Successfully Sent! We will contact you soon.", "Success")
    except Exception as e:
        print("Error in create_contact_us:", str(e))
        frappe.log_error("Error in create_contact_us: {}".format(str(e)))
