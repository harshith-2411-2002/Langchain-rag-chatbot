function sendMessage() {
    var userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    var chatBox = document.getElementById('chat-box');
    var userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user');
    userMessage.textContent = 'You: ' + userInput;
    chatBox.appendChild(userMessage);

    // Send user input to server
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/send_message');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            var botMessage = document.createElement('div');
            botMessage.classList.add('message', 'bot');
            botMessage.textContent = 'Bot: ' + response.response;
            chatBox.appendChild(botMessage);
            chatBox.scrollTop = chatBox.scrollHeight;
        } else {
            console.error('Request failed. Status:', xhr.status);
        }
    };
    xhr.send('user_input=' + encodeURIComponent(userInput));
    document.getElementById('user-input').value = '';
}
