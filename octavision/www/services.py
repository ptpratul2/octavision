import frappe
def get_context(context):
    try:
        context.services = frappe.get_list("Services", fields=["name","title", "font_awesome", "sub_title","i_class_background","background"], as_dict=True)
    except Exception as e:
        frappe.local.flags.redirect_location = '/'
        raise frappe.Redirect

    return context