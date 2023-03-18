
function recommendMeta(el, video, price, title, profile, fullname, url) {
  el.append(`<div class="col-md-6 col-lg-4">
          <a href="${url}" class="btn">
              <div class="ph-item shadow-lg rounded-3">
                <div class="ph-col-12 p-0 h-100">
                  <div class="ph-picture ok">
                    <video style="width: 100%; height: 120px;" controls>
                      <source class="h-100 w-100" draggable="false"  src="${video}" type="video/mp4" />
                    </video>
                  </div>
                  <div class="edit ph-row h-auto">
                    <div class="ph-col-4 empty"></div>
                    <p class="col-8 text-lead fs-6 text-end my-2">Starting At <span class="fw-bold text-primary">US$${price}</span></p>
                    <strong class="col-12 cus">${title}</strong>
                  </div>
                </div>
                <div class="edit ph-col-2 mt-auto">
                  <div class="edit ph-avatar d-flex">
                    <img src="${profile}" alt="" title="${fullname}" class="w-100">
                  </div>
                </div>
                <div class="my-auto col-md-9 col-lg-8 mb-auto">
                  <div class="ph-row py-2">
                    <strong class="ph-col-12 text-lead">${fullname}</strong>
                    <strong class="ph-col-12 text-primary mb-1">Top Rated Seller</strong>
                    <div class="ph-col-8 big"></div>
                  </div>
                </div>
              </div>
              </a>
            </div>`)
}


function processData(data, el, el_meta_doc) {
  el_meta_doc.innerHTML = ""
  data.map(data => {
    let video = data.video
    let price = data.get_start_price
    let title = data.title
    let profile = data.get_profile_Picture
    let fullname = data.get_full_Name
    let urls = data.get_url
    recommendMeta(el, video, price, title, profile, fullname, urls)
  })
}

var profile = $("#profile")
query = profile.val()

// var endpoint1 = "http://127.0.0.1:8000/profileAll"
var endpoint2 = `productMeta/`
var endpoint3 = `productProject/`

var all = $("#productAll")
let el_all_doc = document.querySelector("#productAll")

var meta = $("#productMeta")
let el_meta_doc = document.querySelector("#productMeta")

var project = $("#productProject")
let el_project_doc = document.querySelector("#productProject")


if (el_all_doc){
  get_meta(endpoint2, all, el_all_doc)
  get_meta(endpoint3, all, el_all_doc)
}
if (el_meta_doc){
  get_meta(endpoint2, meta, el_meta_doc)
}
if (el_project_doc ){
  get_meta(endpoint3, project, el_project_doc)
}
  

function get_meta(endpoint, rec_meta, el_meta_doc){
  fetch(endpoint)
    .then(
      (res) => res.json()
  )
    .then(
      (response) => { 
      processData(response, rec_meta, el_meta_doc)
      })
    .catch(err => console.log("error", err))
}