$("#contact-form").on("submit", function () {
    frappe.call({
      method: "octavision.www.contact.contact.create_contact_us",
      args: {
        contact_name: $("#form_name").val(),
        company_name: $("#form_company_name").val(),
        phone: $("#form_phone").val(),
        business_domain: $("#form_business_domain").val(),
        no_of_employees: $("#form_no_of_employees").val(),
        message: $("#form_message").val(),
        email: $("#form_email").val(),
      },
      callback: function (r) {
        if (r.message) {
          // Success response
          console.log("Success:", r.message);
        } else if (r.exc) {
          // Error response
          console.log("Error:", r.exc);
        }
      },
    });
  });