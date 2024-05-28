// Variables
let player1 = "";
let player2 = "";

// Move in the page
document.getElementById("btn1v1").addEventListener("click", function () {
  document.getElementById("chosePlay").style.display = "none";
  document.getElementById("insertNick").style.display = "block";
});

document.getElementById("backChose").addEventListener("click", function () {
  var input = document.getElementById("nicknameInput");
  input.value = "";
  document.getElementById("chosePlay").style.display = "block";
  document.getElementById("insertNick").style.display = "none";
});

document.getElementById("nicknameInput").addEventListener("input", function () {
  var input = document.getElementById("nicknameInput");
  var button = document.getElementById("playButton");
  if (input.value.trim() === "") {
    button.disabled = true;
  } else {
    button.disabled = false;
  }
});

document.getElementById("playButton").addEventListener("click", function () {
  player1 = "Prendere da user";
  let input = document.getElementById("nicknameInput");
  player2 = input.value;
  input.value = "";
  console.log("player1: ", player1, "player2: ", player2);
  document.getElementById("nickPlayer1").textContent = player1;
  document.getElementById("nickPlayer2").textContent = player2;
  document.getElementById("insertNick").style.display = "none";
  document.getElementById("game").style.display = "block";
});

// Back to Main
var elements = document.getElementsByClassName("go_to_main");

for (var i = 0; i < elements.length; i++) {
  elements[i].addEventListener("click", function () {
    console.log("ciao");
  });
}

// Game
let currentPlayer = Math.random() < 0.5 ? "X" : "O";
const cells = document.querySelectorAll(".cell");

cells.forEach((cell) => {
  cell.addEventListener("click", handleClick, { once: true });
});

highlightPlayer();

function handleClick(e) {
  if (e.target.textContent !== "") return;
  e.target.textContent = currentPlayer;
  if (checkWin(currentPlayer)) {
    currentPlayer = "X";
    document.getElementById("alert").style.display = "block";
    document.getElementById(
      "aler-message"
    ).textContent = `${playerWins()} wins!`;
  } else if (Array.from(cells).every((cell) => cell.textContent !== "")) {
    document.getElementById("alert").style.display = "block";
    document.getElementById("aler-message").textContent = `It's a draw!`;
    currentPlayer = "X";
  } else {
    currentPlayer = currentPlayer === "X" ? "O" : "X";
  }
  // mandare dati
  highlightPlayer();
}

function highlightPlayer() {
  document.getElementById("nickPlayer1").style.color =
    currentPlayer === "X" ? "green" : "white";
  document.getElementById("nickPlayer2").style.color =
    currentPlayer === "O" ? "green" : "white";
}

function playerWins() {
  return currentPlayer === "X" ? player1 : player2;
}

function checkWin(player) {
  const winningCombinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  return winningCombinations.some((combination) =>
    combination.every((index) => cells[index].textContent === player)
  );
}
