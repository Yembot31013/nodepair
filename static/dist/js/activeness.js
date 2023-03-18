let locations = window.location
let wsStart = 'ws://'

if (locations.protocol === 'https') {
  wsStart = 'wss://'
}

let endpoint = wsStart + locations.host + "/activeMsg/"

var socket = new ReconnectingWebSocket(endpoint)

socket.onopen = async (e) => {
  console.log('open', e)
}
socket.onmessage = async (e) => {
  console.log('message', e)
}
socket.onerror = async (e) => {
  console.log('error', e)
}
socket.onclose = async (e) => {
  console.log('close', e)
}
function addCount() {
  var count = document.querySelector(".msgCount")
  if (count) {
    let value = parseInt(count.textContent.replace("+", "")) + 1
    if (value > 10) {
      count.textContent = "+10"
    }
    else {
      count.textContent = value
    }
  } else {
    $(".dropMsg").append(`<span class="badge bg-warning msg">1</span>`)
  }
}