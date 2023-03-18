
var formField = document.querySelector("#queryForm")
formField.addEventListener("submit", (e) => {
  e.preventDefault()
  let query = document.querySelector("#searchBar").value
  e.reset
  window.location = `/query/${query}/`
})

function recommendMeta(el, video, price, title, profile, fullname, url) {
  el.append(`<div class="col-md-6 col-lg-4">
        <a href="${url}" class="btn">
          <div class="ph-item shadow-lg rounded-3">
            <div class="ph-col-12 p-0 h-100">
              <div class="ph-picture ok">
                <video style="width: 324px; height: 120px;" controls controlsList="nodownload" onPlay="handlePlay(this)" onContextmenu="handleContext()">
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

function handlePlay(e) {
  e.requestPictureInPicture();
}
function handleContext(e) {
  e.preventDefault();
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


var endpoint1 = "fetchMeta"
var endpoint2 = "fetchProject"
var endpoint3 = "fetchRateMeta"
var endpoint4 = "fetchRateProject"

var rec_meta = $("#rec_meta")
let el_meta_doc = document.querySelector("#rec_meta")

var rec_project = $("#rec_project")
let el_rec_project_doc = document.querySelector("#rec_project")

var rate_meta = $("#rate_meta")
let el_rate_meta_doc = document.querySelector("#rate_meta")

var rate_project = $("#rate_project")
let el_rate_project_doc = document.querySelector("#rate_project")

if (el_meta_doc){
  get_meta(endpoint1, rec_meta, el_meta_doc)
}
if (el_rec_project_doc){
  get_meta(endpoint2, rec_project, el_rec_project_doc)
}
if (el_rate_meta_doc){
  get_meta(endpoint3, rate_meta, el_rate_meta_doc)
}
if (el_rate_project_doc){
  get_meta(endpoint4, rate_project, el_rate_project_doc)
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