import frappe

from octavision.util import sendmail
#doc,recipients,msg,title,attachments=None

@frappe.whitelist
def contact(**args):
    doc =frappe.get.doc('')
    print(args)
    print("hiii")


    return args