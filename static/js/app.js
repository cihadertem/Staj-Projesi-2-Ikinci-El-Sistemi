const roomName=JSON.parse(document.getElementById("room-name").textContent)
const user=JSON.parse(document.getElementById("user").textContent)
const conversation=document.getElementById("conversation")

const sendButton=document.getElementById("send")
const inputField=document.getElementById("comment")


const chatSocket= new WebSocket("ws://"+window.location.host+"/ws/chat/"+roomName+"/")



document.getElementById("hiddeninput").addEventListener('change',handleFileSelect,false)

function handleFileSelect(){
  var file=document.getElementById('hiddeninput').files[0];
  getBase64(file)
}

function getBase64(file){
  var reader= new FileReader()
  reader.readAsDataURL(file)

  reader.onload=function(){
    chatSocket.send(JSON.stringify({
      "what_is_it":"image",
      "message":reader.result
    }))
  }
}

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data)
    const message_type=data.what_is_it
    if(message_type==="text"){
        var message=data.message
    }else if(message_type==="image"){
        var message=`<img width="300" height="300" src="${data.message}">`
    }
    if (user === data.user){
    var message =`<div class="row message-body">
    <div class="col-sm-12 message-main-sender">
      <div class="sender">
        <div class="message-text">
          ${message}
        </div>
        <span class="message-time pull-right">
            ${data.created_date}
        </span>
      </div>
    </div>
  </div>`
}else{
   var message =`<div class="row message-body">
    <div class="col-sm-12 message-main-receiver">
      <div class="receiver">
        <div class="message-text">
          ${message}
        </div>
        <span class="message-time pull-right">
            ${data.created_date}
        </span>
      </div>
    </div>
  </div>`
}
    conversation.innerHTML+= message
};

chatSocket.onclose=function(e){
    console.error("Socket beklenmedik bir şekilde kapandı.")
}

inputField.focus()
inputField.onkeyup=function (e){
    if(e.keyCode===13){
        sendButton.click()
    }
}
sendButton.onclick= function (e) {
    const message=inputField.value
    chatSocket.send(JSON.stringify({
        "what_is_it":"text",
        'message': message
    }))
    inputField.value=" "
    
}
