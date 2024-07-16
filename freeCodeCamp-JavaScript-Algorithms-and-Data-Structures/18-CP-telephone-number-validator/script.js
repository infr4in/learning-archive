const userInput = document.getElementById("user-input");
const checkBtn = document.getElementById("validator-check-btn");
const clearBtn = document.getElementById("validator-clear-btn");
const output = document.getElementById("output");

const checkValidNumber = input => {
  if (input === "") {
    alert("Please provide a phone number");
    return;
  }

  const countryCode = "^(1\\s?)?";
  const areaCode = "(\\([0-9]{3}\\)|[0-9]{3})";
  const spacesDashes = "[\\s\\-]?";
  const phoneNumber = "[0-9]{3}[\\s\\-]?[0-9]{4}$";
  const phoneRegex = new RegExp(
    `${countryCode}${areaCode}${spacesDashes}${phoneNumber}`
  );

  const pTag = document.createElement("p");
  if (phoneRegex.test(input)) {
    pTag.style.color = "lightgreen";
    pTag.innerText = `Valid US number: ${input}`;
  } else {
    pTag.style.color = "lightcoral";
    pTag.textContent = `Invalid US number: ${input}`;
  }

  output.appendChild(pTag);
}

checkBtn.addEventListener("click", () => {
  checkValidNumber(userInput.value);
  userInput.value = "";
  output.classList.remove("hidden");
});

userInput.addEventListener("keydown", e => {
  if (e.key === "Enter") {
    checkValidNumber(userInput.value);
    userInput.value = "";
    output.classList.remove("hidden");
  }
});

clearBtn.addEventListener("click", () => {
  output.textContent = "";
  output.classList.add("hidden")
});