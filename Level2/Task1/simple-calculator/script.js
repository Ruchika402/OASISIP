let display = document.getElementById("display");
let buttons = document.querySelectorAll("button");
let history = document.getElementById("history");
let clearHistoryBtn = document.getElementById("clearHistory");
let currentInput = "";

clearHistoryBtn.addEventListener("click", () => {
history.innerHTML = "";
});

buttons.forEach(button => {

button.addEventListener("click", () => {

let value = button.innerText;

if(value === "C"){
currentInput = "";
display.value = "";
}

else if(value === "="){
try{
let result = eval(currentInput);

let historyItem = document.createElement("div");
historyItem.innerText = currentInput + " = " + result;

history.prepend(historyItem);

display.value = result;
currentInput = result;
}
catch{
display.value = "Error";
}
}

else{
currentInput += value;
display.value = currentInput;
}

});

});