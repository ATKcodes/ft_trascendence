// Variables
let player1 = "";
let player2 = "";

function getId(id) {
  return document.getElementById(id);
}

// Move in the page
let path = ["chosePlay", "insertNick", "game"];

function moveArround(were) {
  for (let i = 0; i < path.length; i++) {
    if (path[i] === were) {
      getId(were).style.display = "block";
    } else {
      getId(path[i]).style.display = "none";
    }
  }
}

getId("btn1v1").addEventListener("click", function () {
  moveArround("insertNick");
});

getId("backChose").addEventListener("click", function () {
  var input = getId("nicknameInput");
  input.value = "";
  moveArround("chosePlay");
});

getId("nicknameInput").addEventListener("input", function () {
  var input = getId("nicknameInput");
  var button = getId("playButton");
  if (input.value.trim() === "") {
    button.disabled = true;
  } else {
    button.disabled = false;
  }
});

getId("playButton").addEventListener("click", function () {
  player1 = "Prendere da user";
  let input = getId("nicknameInput");
  player2 = input.value;
  input.value = "";
  console.log("player1: ", player1, "player2: ", player2);
  getId("nickPlayer1").textContent = player1;
  getId("nickPlayer2").textContent = player2;
  moveArround("game");
});

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
    getId("alert").style.display = "block";
    getId(
      "aler-message"
    ).textContent = `${playerWins()} wins!`;
  } else if (Array.from(cells).every((cell) => cell.textContent !== "")) {
    getId("alert").style.display = "block";
    getId("aler-message").textContent = `It's a draw!`;
    currentPlayer = "X";
  } else {
    currentPlayer = currentPlayer === "X" ? "O" : "X";
  }
  // mandare dati
  highlightPlayer();
}

function highlightPlayer() {
  getId("nickPlayer1").style.color =
    currentPlayer === "X" ? "green" : "white";
  getId("nickPlayer2").style.color =
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

// var matchData = {
// 	game: "pong",
// 	win: this.winorlose,
// 	player2: document.querySelector('.userright').textContent, // Get User2 name
// };
