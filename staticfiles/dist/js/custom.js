names = document.querySelector("#name");
subject = document.querySelector("#subject");
email = document.querySelector("#email");
message = document.querySelector("#message");
subscribe = document.querySelector("#subcribe");
token = document.querySelector("input[name=csrfmiddlewaretoken]");
send = document.querySelector(".send");

send.addEventListener("submit", (e)=>{
    e.preventDefault()
    name_value = names.value
    subject_value = subject.value
    email_value = email.value
    message_value = message.value
    is_subcribe = subscribe.checked
    tokens = token.value
    $.ajax({
        method: "POST",
        url: "subcribe",
        data: {
          'name': name_value,
          'subject': subject_value,
          'email': email_value,
          'message': message_value,
          'subcribe': is_subcribe,
          csrfmiddlewaretoken: tokens,
        },
        // datatype: "dataType",
        success: function (response) {
          names.value = ""
          subject.value = ""
          email.value = ""
          message.value = ""
          subscribe.checked = false

                Swal.fire(
                    response.msg,
                    response.yemi,
                    response.state
                  )
        },
        error: function (e) {
          names.value = ""
          subject.value = ""
          email.value = ""
          message.value = ""
          subscribe.checked = false
          Swal.fire(
           'Error',
            e.statusText,
            'warning'
          )
        }
      })
})