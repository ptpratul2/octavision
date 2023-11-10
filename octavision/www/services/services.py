import frappe

def get_context(context):
    try:
        docname=frappe.form_dict.docname

        # context.services = frappe.db.sql(f"""SELECT * FROM `tabServices`;""", as_dict=True)
        context.services  = frappe.get_list("Services")
    except Exception as e:
        frappe.local.flags.redirect_location = '/404'
        raise frappe.Redirect

    return context