

const buttonA = document.querySelector("#SendMessageBtn");
const input = document.querySelector("#UserInput");


buttonA.onclick = () => {
  alert(input.value);
  createJSON();
};

function createJSON() {
  const dict_values = {"ChatGPT":input.value};
  console.log(dict_values);
  const str = JSON.stringify(dict_values);
  console.log(str);
  $.ajax({
    url:"/test",
    type:"POST",
    contentType:"application/json",
    data: str
  });
}
