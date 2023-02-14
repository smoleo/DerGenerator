
let div=document.getElementById("NameList");

addEventListeners();
addToDisplay();

function addEventListeners(){
    console.log("addEventListeners");
    $('#generate').on('click', () => {
        console.log("generate");
        addToDisplay([1,2,3,4,5,6])
     });
     $('#add').on('click', () => {
       eel.addToWords(document.getElementById('part1').value,document.getElementById('part2').value,document.getElementById('part3').value)
       document.getElementById('part1').value=""
       document.getElementById('part2').value=""
       document.getElementById('part3').value=""
     });
}

async function addToDisplay(list){
    div.innerHTML = "";
    eel.generateNames()((names)=>{
        names.forEach((element)=>{
            div.innerHTML += "<p  class=\"block mb-2 text-base font-medium text-gray-900 dark:text-white\">"+element+"</p>";
        })
    })

}