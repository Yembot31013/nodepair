let locations = window.location
let wsStart = 'ws://'
let input_message;
let thread_id;
const USER_ID = $("#user_id").val();
let send_msg_form = $(".send-msg-form")

function refreshs(){
  window.location.reload()
}

function scrollToBottom(el) {
  el.scrollTop = el.scrollHeight;
}
      
if (locations.protocol === 'https') {
  wsStart = 'wss://'
}

let endpoint = wsStart + locations.host + locations.pathname

var socket = new ReconnectingWebSocket(endpoint)

socket.onopen = async (e) => {
  console.log('open', e)
  $(".send-msg-form").on("submit", (e) => {
    e.preventDefault()
    thread_id = e.currentTarget.getAttribute("form_id")
    other_user = e.currentTarget.getAttribute("other_user")
    input_message = document.getElementById(`chat-input-${thread_id}`)
    let message = input_message.value
    input_message.value = null;
    if (message){
    let data = {
      'type': "message",
      'thread': thread_id,
      'other_user': other_user,
      'message': message,
    }
    data = JSON.stringify(data)
    socket.send(data)
      document.getElementById(`form-${thread_id}`).reset;
      }
  })
  discuss_profile = document.querySelectorAll(".discuss")
  
  discuss_profile.forEach(element => {
    element.addEventListener("click", (e) => {
      var el_thread = e.currentTarget.getAttribute("id").replace("container-", "").trim()
      var discuss_count = document.getElementById(`new_${el_thread}`)
      var container_el = e.currentTarget
      if (discuss_count){
        let data = {
          'type': "read",
          'thread': el_thread,
        }
        data = JSON.stringify(data)
        socket.send(data)
        
        if (container_el) {
          container_el.classList.remove("unread")
          container_el.classList.add("read")
        }
        discuss_count.remove()
      }
      scrollToBottom(document.getElementById(`content_${el_thread}`));
    })
  });
}
socket.onmessage = async (e) => {
  console.log('message', e)
  let data = JSON.parse(e.data)
  let type = data['type']
  if (type == "status"){
    
    let status = data['status']
    let user = data['user']
    console.log("before", status, user)
    let user_el = document.getElementById(`status_${user}`)
    let contact_el = document.getElementById(`contact_${user}`)
    let contacts_el = document.getElementById(`contacts_${user}`)
    let status_el = document.getElementById(`chat_thread_${user}`)
    let chat_el = document.getElementById(`chat_status_${user}`)
    if (user_el) {
      console.log("after1", status, user)
      if (status == "online") {
        user_el.classList.remove("offline")
        user_el.classList.add("online")
      }if(status == "offline") {
        user_el.classList.remove("online")
        user_el.classList.add("offline")
      }
    }
    
    if (contacts_el) {
      console.log("after2", status, user)
      if (status == "online") {
        contacts_el.classList.remove("offline")
        contacts_el.classList.add("online")
      }if(status == "offline") {
        contacts_el.classList.remove("online")
        contacts_el.classList.add("offline")
      }
    }
    if (contact_el) {
      console.log("after3", status, user)
      if (status == "online") {
        contact_el.classList.remove("offline")
        contact_el.classList.add("online")
      }if(status == "offline") {
        contact_el.classList.remove("online")
        contact_el.classList.add("offline")
      }
    }
    if (status_el) {
      console.log("after4", status, user)
      if (status == "online") {
        status_el.classList.remove("offline")
        status_el.classList.add("online")
      }if(status == "offline") {
        status_el.classList.remove("online")
        status_el.classList.add("offline")
      }
    }
    if (chat_el) {
      console.log("after7", status, user)
      if (status == "online") {
        chat_el.textContent = "Active now"
      }if(status == "offline") {
        chat_el.textContent = "offline"
      }
    }
  }
  if (type == "message"){
    let thread = data['thread']
    let chat_t = data['chat_t']
    let other_name = data['other_name']
    let other_id = data['other_id']
    let message = data['message']
    let back_user = data['user']
    newMessage(message, chat_t, thread, back_user, other_name, other_id)
    insert_last_statement(message, thread)
    move_to_top(socket, thread, back_user)
  }
}
socket.onerror = async (e) => {
  console.log('error', e)
}
socket.onclose = async (e) => {
  console.log('close', e)
}


function newMessage(message, timestamp, thread, back_user, other_name, other_id) {
  if ($.trim(message) === '') {
    return false;
  }

  let message_element;
  if (USER_ID != back_user){
  message_element = `<div class="message">
												<img class="avatar-md" src="/static/dist/img/avatars/avatar-female-5.jpg" data-toggle="tooltip" data-placement="top" title="Keith" alt="avatar">
												<div class="text-main">
													<div class="text-group">
														<div class="text">
															<p>${message}</p>
														</div>
													</div>
												</div>
											</div>`
  }else{
  message_element = `<div class="message me">
												<div class="text-main">
													<div class="text-group me">
														<div class="text me">
															<p>${message}</p>
														</div>
													</div>
												</div>
											</div>`
    }
  let message_body = $(`#msg-card-body-${thread}`)

  if (!message_body) {
    create_new_thread(thread, other_name, other_id)
    message_body = $(`#msg-card-body-${thread}`)
  }

  message_body.append(message_element)
  message_body.animate({
    scrollTop: $(document).height()
  }, 100)
}

function insert_last_statement(msg, id) {
  if ($.trim(msg) === '') {
    return false;
  }
  $(`#last-${id}`).text(msg)
}

function create_new_thread(id, other_name, other_id) {
  $("#chats").append(`<a href="#list-${id}" class="filterDiscussions discuss all unread single" id="container-${id} data-toggle="list" role="tab">
												<img class="avatar-md" src="/static/dist/img/avatars/avatar-male-1.jpg" data-toggle="tooltip" data-placement="top" title="${other_name}" alt="avatar">
												<div class="status">
													<i class="material-icons online">fiber_manual_record</i>
												</div>
                        <div id="unread_${id}">
                          <div class="new bg-pink" id="new_${id}">
                            <span id="count_${id}">1</span>
                          </div>
                        </div>
												<div class="data">
													<h5>${other_name}</h5>
													<span>Sun</span>
													<p id="last-${id}"></p>
												</div>
											</a>`)
  
  $("#").append(`<div class="babble tab-pane fade" id="list-${id}" role="tabpanel" aria-labelledby="list-chat-list">
							<div class="chat" id="chat1">
								<div class="top">
									<div class="container">
										<div class="col-md-12">
											<div class="inside">
												<a href="#"><img class="avatar-md" src="/static/dist/img/avatars/avatar-female-5.jpg" data-toggle="tooltip" data-placement="top" title="${other_name}" alt="avatar"></a>
												<div class="status">
													<i class="material-icons online">fiber_manual_record</i>
												</div>
												<div class="data">
													<h5><a href="#">${other_name}</a></h5>
													<span>Active now</span>
												</div>
											</div>
										</div>
									</div>
								</div>
								<div class="content" id="content">
									<div class="container">
										<div class="col-md-12 msg-card-body" id="msg-card-body-${id}">
											
										</div>
									</div>
								</div>
								<div class="container">
									<div class="col-md-12">
										<div class="bottom">
											<form class="position-relative w-100 send-msg-form" id="form-${id}" form_id="${id}" other_user="${other_id}">
												<textarea class="form-control" placeholder="Start typing for reply..." rows="1" id="chat-input-${id}"></textarea>
												<button class="btn emoticons"><i class="material-icons">insert_emoticon</i></button>
												<button type="submit" class="btn send"><i class="material-icons">send</i></button>
											</form>
											<label>
												<input type="file">
												<span class="btn attach d-sm-block d-none"><i class="material-icons">attach_file</i></span>
											</label> 
										</div>
									</div>
								</div>
							</div>
						</div>`)
}

async function move_to_top(sockets, thread, back_user) {
  var cur = document.getElementById(`container-${thread}`)
  if (USER_ID != back_user) {
    if (document.querySelector(`.active.show#container-${thread}`)) {
      cur.classList.remove("unread")
      cur.classList.add("read")
    } else {
      cur.classList.remove("unread")
      cur.classList.add("read")
    }
  }
  var parent = cur.parentNode
  var first = parent.firstChild

  parent.insertBefore(cur, first)
  if (document.querySelector(`.active.show#container-${thread}`)) {
        let data = {
          'type': "read",
          'thread': thread,
        }
        data = JSON.stringify(data)
        await sockets.send(data)
  }
  if (!document.querySelector(`.active.show#container-${thread}`)) {
    var count = document.getElementById(`count_${thread}`)
    var unread = document.getElementById(`unread_${thread}`)
    if (USER_ID != back_user) { 
      if (count) {
        
        let value = parseInt(count.textContent.replace("+", "")) + 1
        if (value > 10) {
          count.textContent = "+10"
        }
        else {
          count.textContent = value
        }
      } else {
        unread.innerHTML = `<div class="new bg-yellow" id="new_${thread}"><span id="count_${thread}">1</span></div>`
      }
    }
  }
}
