const avatarBtn = document.querySelector(".avatar-btn")
const avatarPic = document.querySelector(".avatar-pic")
const formClass = document.querySelector(".formClass")
const firstName = document.querySelector("#firstName")
const email = document.querySelector("#email")
const locations = document.querySelector("#location")

formClass.addEventListener("submit", (e) => {
  e.preventDefault();
  if (firstName.value == "") {
    Swal.fire(
        'Error',
        "full name can't be left empty",
        'info'
    )
    return false;
  }
  if (email.value == "") {
    Swal.fire(
        'Error',
        "email can't be empty",
        'info'
    )
    return false;
  }
  if (locations.value == "") {
    Swal.fire(
        'Error',
        "location must be provided, (example: Lagos, Nigeria)",
        'info'
    )
    return false;
  }
  if (locations.value == "None") {
    Swal.fire(
        'Error',
        "Invalid, location can't be none, (example: Lagos, Nigeria)",
        'info'
    )
    return false;
  }
  formClass.submit()
  formClass.reset()
})
avatarBtn.addEventListener("click", () => {
  avatarPic.click
})
avatarPic.addEventListener("change", function () {
		let folder = this.files[0];
		if (folder.type == "image/png" | folder.type == "image/jpeg") {
		let fileReader = new FileReader();
		fileReader.onload = ()=>{
		  let fileURL = fileReader.result;
		  send_file(fileURL)
		};
		fileReader.readAsDataURL(folder);
  }
})
let credent_el = document.getElementsByName("csrfmiddlewaretoken")
let credent = credent_el.value

async function send_file(fileURL) {
  
  fetch("update_pics", {method: "post", body:JSON.stringify({"profile_pic": fileURL})})
    .then(
      (res) => res.json()
  )
    .then(
      (response) => { 
      processData(response, fileURL)
      })
    .catch(err =>
      Swal.fire(
        'Error',
        'info'
      )
    )
}
function processData(response, fileURL) {
  let pict1 = document.querySelector(".nav-avatar")
  pict1.src = fileURL
  let pict2 = document.querySelector(".up-avatar")
  pict2.src = fileURL
  let pict3 = document.querySelector(".display-avatar")
  pict3.src = fileURL
  Swal.fire(
    'Success',
    response.response,
    'success'
  )
}