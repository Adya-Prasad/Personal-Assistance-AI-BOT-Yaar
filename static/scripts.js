let selectedMood = ''; // Variable to store the selected mood

function setMood(mood, event) {
    selectedMood = mood; // Set the selected mood
    // Optional: Change the button color to indicate selection
    document.querySelectorAll('.mood-button').forEach(button => {
        button.classList.remove('selected');
    });
    event.target.classList.add('selected'); // Highlight selected button
}

// Event listener for the "Send" button
document.getElementById('send-button').addEventListener('click', function() {
    const userMessage = document.getElementById('user-input').value;

    // Create a POST request to send user message and selected mood (if any)
    fetch('/get-response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `message=${encodeURIComponent(userMessage)}&mood=${encodeURIComponent(selectedMood)}`
    })
    .then(response => response.json())
    .then(data => {
        // Append the bot's response to the chat box
        const chatBox = document.getElementById('chat-box');
        chatBox.innerHTML += `<div>User: ${userMessage}</div>`;
        chatBox.innerHTML += `<div>Bot: ${data.response}</div>`;
        // Clear the input fields
        document.getElementById('user-input').value = '';
        selectedMood = ''; // Reset the selected mood
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Event listener for the "Tell me a joke" button
document.getElementById("joke-button").addEventListener("click", function() {
    fetch("/get-response", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: "message=Tell me a joke&mood=neutral", // Sending a neutral mood for the joke
    })
    .then(response => response.json())
    .then(data => {
        const chatBox = document.getElementById("chat-box");
        chatBox.innerHTML += `<div class='bot-message'>${data.response}</div>`;
    })
    .catch(error => console.error("Error:", error));
});
