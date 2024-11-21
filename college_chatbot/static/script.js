function toggleChatbot() {
    const chatbotWindow = document.getElementById('chatbot-window');
    chatbotWindow.style.display = chatbotWindow.style.display === 'none' ? 'flex' : 'none';
}

function sendMessage() {
    const userInput = document.getElementById('userInput').value.trim();
    const messagesDiv = document.getElementById('messages');

    if (!userInput) return;  // Prevent sending empty messages

    // Display user's message
    messagesDiv.innerHTML += `<div>User: ${userInput}</div>`;
    messagesDiv.scrollTop = messagesDiv.scrollHeight;  // Scroll to the bottom

    // Send request to Flask server
    fetch('/get-response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Display chatbot's response
        messagesDiv.innerHTML += `<div>Chatbot: ${data.answer}</div>`;
        messagesDiv.scrollTop = messagesDiv.scrollHeight;  // Scroll to the bottom
        document.getElementById('userInput').value = ''; // Clear input
    })
    .catch(error => {
        console.error('Error:', error);
        messagesDiv.innerHTML += `<div>Chatbot: I'm sorry, there was an error.</div>`;
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    });
}

function sendOnEnter(event) {
    if (event.key === "Enter") {
        sendMessage();
        return false;  // Prevent form submission
    }
}
