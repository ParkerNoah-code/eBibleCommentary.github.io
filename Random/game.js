document.addEventListener("DOMContentLoaded", function () {
  const gameContainer = document.getElementById("gameContainer");
  setupGameArea();

  const basket = createBasket();
  const scoreDisplay = createScore();
  let score = 0;

  document.addEventListener("mousemove", function (e) {
    moveBasket(e, basket, gameContainer);
  });

  setInterval(dropObjects, 1000);

  function setupGameArea() {
    gameContainer.style.position = "relative";
    gameContainer.style.width = "800px";
    gameContainer.style.height = "600px";
    gameContainer.style.margin = "20px auto";
    gameContainer.style.backgroundColor = "#fff";
    gameContainer.style.overflow = "hidden";
    gameContainer.style.boxShadow = "0 0 10px rgba(0,0,0,0.5)";
  }

  function createBasket() {
    const basket = document.createElement("div");
    basket.style.position = "absolute";
    basket.style.bottom = "10px";
    basket.style.left = "50%";
    basket.style.transform = "translateX(-50%)";
    basket.style.width = "100px";
    basket.style.height = "30px";
    basket.style.backgroundColor = "#8B4513";
    gameContainer.appendChild(basket);
    return basket;
  }

  function createScore() {
    const scoreDisplay = document.createElement("div");
    scoreDisplay.textContent = "Score: 0";
    scoreDisplay.style.position = "absolute";
    scoreDisplay.style.top = "10px";
    scoreDisplay.style.left = "10px";
    scoreDisplay.style.fontSize = "24px";
    scoreDisplay.style.color = "#333";
    gameContainer.appendChild(scoreDisplay);
    return scoreDisplay;
  }

  function moveBasket(e, basket, container) {
    let containerRect = container.getBoundingClientRect();
    let newLeft = e.clientX - containerRect.left - basket.offsetWidth / 2;
    newLeft = Math.max(
      0,
      Math.min(container.offsetWidth - basket.offsetWidth, newLeft)
    );
    basket.style.left = newLeft + "px";
  }

  function dropObjects() {
    let obj = document.createElement("div");
    obj.style.position = "absolute";
    obj.style.top = "0";
    obj.style.left = Math.random() * (gameContainer.offsetWidth - 20) + "px";
    obj.style.width = "20px";
    obj.style.height = "20px";
    obj.style.backgroundColor = "red";
    obj.style.borderRadius = "50%";
    gameContainer.appendChild(obj);
    moveObject(obj);
  }

  function moveObject(obj) {
    let fallInterval = setInterval(function () {
      let objTop = obj.offsetTop + 5;
      if (objTop > gameContainer.offsetHeight - basket.offsetHeight) {
        if (
          Math.abs(parseInt(basket.style.left) - obj.offsetLeft) <
          basket.offsetWidth
        ) {
          score++;
          scoreDisplay.textContent = "Score: " + score;
        }
        clearInterval(fallInterval);
        gameContainer.removeChild(obj);
      } else {
        obj.style.top = objTop + "px";
      }
    }, 50);
  }
});
