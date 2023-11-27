import frappe

def get_context(context):
    try:
        docname=frappe.form_dict.docname

        # context.services = frappe.db.sql(f"""SELECT * FROM `tabServices`;""", as_dict=True)
        # context.services = frappe.get_list("Services", fields=["title", "font_awesome", "sub_title","i_class_background","background"], limit_page_length=6)
        context.services = frappe.get_doc("Services",docname)
        # Fetch child table data from the "Service Item" table for the specified parent
        context.services_item = frappe.get_all("Services Item",
                                               filters={'parent': docname},
                                               fields=["title", "subtitle"],
                                               distinct=True)
    except Exception as e:

        frappe.msgprint('Page Not found')
        # frappe.local.flags.redirect_location = '/404'
        # raise frappe.Redirect

    return context