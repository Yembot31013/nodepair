$(document).ready(function () {
  const formc = document.querySelector('.contact')
  const formBtn = document.querySelector('.contactBtn')
  const productImage = document.querySelector('.product-image')
  const checkOutVideo = document.querySelector('.checkOutVideo')
  
  checkOutVideo.addEventListener('play', (e) => {
    e.target.requestPictureInPicture();
  })
  checkOutVideo.addEventListener('contextmenu', (e) => {
    e.preventDefault()
  })
  productImage.addEventListener('play', (e) => {
    productImage.requestPictureInPicture();
  })
  productImage.addEventListener('contextmenu', (e) => {
    e.preventDefault()
  })
  formBtn.addEventListener('click', (e) => {
    e.preventDefault()
    formc.submit()
  })
    $('.product-image-thumb').on('click', function (e) {
      $('.product-image-thumb.active').removeClass('active')
      $(this).addClass('active')
      try{
        var element = document.querySelector(".product-image-thumb.active img")
        let imgSrc = element.getAttribute("src")
        var parentElement = document.querySelector(".product-content")
        parentElement.innerHTML = `<img class="product-image" src="${imgSrc}" alt="Product Image">`
      }
      catch (error) {
        var element = document.querySelector(".product-image-thumb.active video source")
        let videoSrc = element.getAttribute("src")
        var parentElement = document.querySelector(".product-content")
        parentElement.innerHTML = `<video class="product-image" style="max-height: 270px; width: 100%;">
                          <source class="h-100 w-auto" draggable="false"  src="${videoSrc}" type="video/mp4" />
                        </video>`
      }
    })
  })
  