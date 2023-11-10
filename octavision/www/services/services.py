import frappe

def get_context(context):
    try:
        docname=frappe.form_dict.docname

        # context.services = frappe.db.sql(f"""SELECT * FROM `tabServices`;""", as_dict=True)
        # context.services = frappe.get_list("Services", fields=["title", "font_awesome", "sub_title","i_class_background","background"], limit_page_length=6)
        context.services = frappe.get_doc("Services",docname)
    except Exception as e:

        frappe.msgprint('Page Not found')
        # frappe.local.flags.redirect_location = '/404'
        # raise frappe.Redirect

    return context