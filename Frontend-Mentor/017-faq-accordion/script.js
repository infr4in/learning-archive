const questions = document.querySelectorAll(".item__question");

questions.forEach( question => {
  question.addEventListener("click", e => {
    const questionContainer = e.target.parentElement;
    const questionId = questionContainer.id.slice(-1);
    const questionBtn = questionContainer.children[1];
    const answer = document.getElementById(`answer-${questionId}`);

    answer.classList.toggle("opened");
    questionBtn.classList.toggle("opened");
        
    if (answer.classList.contains("opened")) {
      answer.style.maxHeight = "150px";
    } else {
      answer.style.maxHeight = "0px";
    }

    if (questionBtn.classList.contains("opened")) {
      questionBtn.style.backgroundImage = 'url("./assets/images/icon-minus.svg")'
    } else {
      questionBtn.style.backgroundImage = 'url("./assets/images/icon-plus.svg")'
    }
  });
});