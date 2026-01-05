let inp = document.getElementById('input1');
let btn = document.getElementById("btn1");
let messages = document.getElementById("message_area");

btn.addEventListener("click", () => {
    const paragraph = document.createElement("p");
    paragraph.textContent = inp.value;
    paragraph.id = 'user'
    
    messages.appendChild(paragraph);

    const botText = document.createElement("p");
    botText.textContent = "hello how are you";
    botText.id = 'bot'

    setTimeout(() => {
        messages.appendChild(botText);
    }, 5000);
});

// მუშაობს