// ვაკონტროლებთ მარსის რობოტს - 0, 0
// UX - up x (+10)
// DX - down x (-5)
// UY - up y (+15)
// DY - down y (-10)

function roverNavigation(commands) {
  let x = 0;
  let y = 0;

  let splIttedCommands = commands.split(" ");

  for (let command of splIttedCommands) {
    if (command === "UX") {
      x += 10;
    } else if (command === "DX") {
      x -= 5;
    } else if (command === "UY") {
      y += 15;
    } else if (command === "DY") {
      y -= 5;
    }
  }
  return `(${x},${y})`;
}

console.log(roverNavigation("DX DX UY"));
