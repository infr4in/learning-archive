const userInput = document.getElementById("text-input");
const checkerBtn = document.getElementById("check-btn");
const resultDiv = document.getElementById("result");

function checkForPalindrome(input) {
  // For later output
  const originalInput = input;

  if (input === "") {
    alert("Please input a value");
    return;
  }

  // Remove the previous result
  resultDiv.innerHTML = "";

  const lowerCaseStr = input.replace(/[^A-Za-z0-9]/gi, "''").toLowerCase();
  const reverseStr = [...lowerCaseStr].reverse().join("")

  const output = `
  <span class="accent">${originalInput}</span> 
  ${
    lowerCaseStr === reverseStr ? "is" : "is not"
  } a palindrome.
  `;

  resultDiv.innerHTML += output;

  // Show the result.
  resultDiv.classList.remove("hidden");
}

checkerBtn.addEventListener("click", () => {
  checkForPalindrome(userInput.value);
  userInput.value = "";
});

userInput.addEventListener("keydown", e => {
  if (e.key === "Enter") {
    checkForPalindrome(userInput.value);
    userInput.value = "";
  }
});