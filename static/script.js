async function sendMessage() {
  let input = document.getElementById("user-input");
  let chatBox = document.getElementById("chat-box");
  let userText = input.value.trim();
  if (userText === "") return;

  // Add user message with avatar
  chatBox.innerHTML += `
    <div class='message user-msg'>
      <span>${userText}</span>
      <img src='/static/user.png' alt='User'>
    </div>
  `;
  input.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;

  // Add bot typing indicator
  let typingDiv = document.createElement("div");
  typingDiv.classList.add("message", "bot-msg", "typing");
  typingDiv.innerHTML = `<img src='/static/bot.png' alt='Bot'><span class='dot'></span><span class='dot'></span><span class='dot'></span>`;
  chatBox.appendChild(typingDiv);
  chatBox.scrollTop = chatBox.scrollHeight;

  // Fetch bot response
  const response = await fetch("/get", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ message: userText })
  });

  const data = await response.json();

  // Remove typing indicator
  typingDiv.remove();

  // Add bot response with avatar
  chatBox.innerHTML += `
    <div class='message bot-msg'>
      <img src='/static/bot.png' alt='Bot'>
      <span>${data.reply}</span>
    </div>
  `;
  chatBox.scrollTop = chatBox.scrollHeight;
}
