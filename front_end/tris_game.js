document.getElementById("btn1v1").addEventListener("click", function () {
  document.getElementById("chosePlay").style.display = "none";
  document.getElementById("insertNick").style.display = "block";
});
document
  .getElementsByClassName("back")[0]
  .addEventListener("click", function () {
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
