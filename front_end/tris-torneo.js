function getId(id) {
  return document.getElementById(id);
}

getId("User1").value = "Get from User";
let player1 = getId("User1").value;
let player2 = "";
let player3 = "";
let player4 = "";

// parte torneo
let firstMatch = getId("firstMatch");
let secondMatch = getId("secondMatch");
let finalMatch = getId("final");

let players = [player1, player2, player3, player4];
let match1 = [];
let match2 = [];
let final = [];

// all button
let playButton = getId("playButton");
let playMatch = getId("playMatch");
let nextMatch = getId("nextMatch");
let playAgain = getId("playAgain");
let goToMain = getId("go-to-main");

// Move in the page
let path = ["insertNick", "tournament", "game"];

function moveArround(where) {
  for (let i = 0; i < path.length; i++) {
    if (path[i] === where) {
      getId(where).style.display = "block";
    } else {
      getId(path[i]).style.display = "none";
    }
  }
}

// parte inserisci input
let input = getId("User2");
let input2 = getId("User3");
let input3 = getId("User4");
let button = getId("playButton");
button.disabled = true;
input.addEventListener("input", checkInputs);
input2.addEventListener("input", checkInputs);
input3.addEventListener("input", checkInputs);

function checkInputs() {
  if (
    input.value.trim() !== "" &&
    input2.value.trim() !== "" &&
    input3.value.trim() !== ""
  ) {
    button.disabled = false;
  } else {
    button.disabled = true;
  }
}

playButton.addEventListener("click", function () {
  player2 = input.value;
  player3 = input2.value;
  player4 = input3.value;
  input.value = "";
  input2.value = "";
  input3.value = "";

  players = [player1, player2, player3, player4];

  console.log(
    "player1: ",
    player1,
    "player2: ",
    player2,
    "player3: ",
    player3,
    "player4: ",
    player4
  );
  createMatch();

  moveArround("tournament");
});

// parte torneo
function createMatch() {
  let playersCopy = [...players];
  match1 = [];
  match2 = [];

  for (let i = 0; i < 4; i++) {
    let random = Math.floor(Math.random() * playersCopy.length);
    let player = playersCopy[random];
    playersCopy.splice(random, 1);
    if (i < 2) {
      match1.push(player);
    } else {
      match2.push(player);
    }
  }
  firstMatch.textContent = `${match1[0]} vs ${match1[1]}`;
  firstMatch.style.color = "green";
  secondMatch.textContent = `${match2[0]} vs ${match2[1]}`;
  console.log("match1: ", match1, "match2: ", match2);
}

let currentGame = 1;
playMatch.addEventListener("click", function () {
  resetMatchVariable();
  moveArround("game");
});

// game
let currentPlayer = Math.random() < 0.5 ? "X" : "O";
const cells = document.querySelectorAll(".cell");

function resetMatchVariable() {
  currentPlayer = Math.random() < 0.5 ? "X" : "O";
  cells.forEach((cell) => {
    cell.textContent = "";
    cell.addEventListener("click", handleClick, { once: true });
  });
  getId("alert").style.display = "none";
  nickPlayerText();
  getId("nextMatch").style.display = "none";
  getId("playAgain").style.display = "none";
  getId("go-to-main").style.display = "none";
  highlightPlayer();
}

function handleClick(e) {
  if (e.target.textContent !== "") return;
  e.target.textContent = currentPlayer;
  if (checkWin(currentPlayer)) {
    getId("alert").style.display = "block";
    getId("aler-message").textContent = `${playerWins()} wins!`;
    if (currentGame === 1) {
      currentGame++;
      nextMatch.style.display = "block";
      nextMatch.addEventListener("click", handleNextMatch);
    } else if (currentGame === 2) {
      currentGame++;
      nextMatch.style.display = "block";
      nextMatch.removeEventListener("click", handleNextMatch);
      nextMatch.addEventListener("click", handleFinalMatch);
    } else {
      getId("go-to-main").style.display = "block";
    }
  } else if (Array.from(cells).every((cell) => cell.textContent !== "")) {
    getId("alert").style.display = "block";
    getId("aler-message").textContent = `It's a draw!`;
    playAgain.style.display = "block";
    playAgain.addEventListener("click", function () {
      resetMatchVariable();
    });
  } else {
    currentPlayer = currentPlayer === "X" ? "O" : "X";
  }
  highlightPlayer();
}

function handleNextMatch() {
  final[0] = playerWins();
  finalMatch.textContent = `${final[0]} vs ???`;
  firstMatch.style.color = "white";
  secondMatch.style.color = "green";
  resetMatchVariable();
  moveArround("tournament");
}

function handleFinalMatch() {
  secondMatch.style.color = "white";
  finalMatch.style.color = "green";
  final[1] = playerWins();
  finalMatch.textContent = `${final[0]} vs ${final[1]}`;
  resetMatchVariable();
  moveArround("tournament");
}

// utils
function highlightPlayer() {
  getId("nickPlayer1").style.color = currentPlayer === "X" ? "green" : "white";
  getId("nickPlayer2").style.color = currentPlayer === "O" ? "green" : "white";
}

function playerWins() {
  return currentPlayer === "X"
    ? getId("nickPlayer1").textContent
    : getId("nickPlayer2").textContent;
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

function nickPlayerText() {
  if (currentGame === 1) {
    getId("nickPlayer1").textContent = match1[0];
    getId("nickPlayer2").textContent = match1[1];
  } else if (currentGame === 2) {
    getId("nickPlayer1").textContent = match2[0];
    getId("nickPlayer2").textContent = match2[1];
  } else {
    getId("nickPlayer1").textContent = final[0];
    getId("nickPlayer2").textContent = final[1];
  }
}
