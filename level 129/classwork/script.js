const emojis = [
    "😀",
    "😎",
    "🚀",
    "🌈",
    "🍕",
    "🐶",
    "🐱",
    "🌲",
    "🔥",
    "⚽",
    "💡",
    "🎉",
    "🤔",
    "👍",
    "😭",
    "💻",
    "🎨",
    "🧠",
    "😍",
    "😂"
  ];
  let button = document.getElementById("btn")
  
  const randomIndex = Math.floor(Math.random() * emojis.length)

  button.onclick("click",function(e){
    console.log(emojis[randomIndex])
  })