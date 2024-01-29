
function validateLogin(){
    message.innerHTML="";
    let valid=true;
    Array.from(document.getElementById("loginForm").getElementsByTagName("input")).map(
        item=>{
            if (item.value==""){
                message.innerHTML+=`Please fill out the ${item.name} <br>`;
                item.style.borderColor="red";
                valid=false;
            }
        })
    if (valid){
        loginForm.submit();
    }
}

function changeColorNAV(linkId) {
    var navLinks = document.getElementsByClassName("navbartext");
    for (var i = 0; i < navLinks.length; i++) {
        navLinks[i].style.backgroundColor =  "rgba(237, 237, 237, 0.749)";
    }
    var clickedLink = document.getElementById(linkId);
        if (clickedLink) {
            clickedLink.style.backgroundColor = "rgba(237, 237, 237, 0.18)";
        }
    console.log("you notttt")
} // ask tal why it is not working ? maybe the async


function DashbordAllTask() {
    let allButton = document.getElementById("tasksButtonAll");
    let myButton = document.getElementById("tasksButtonMy");
    allButton.style.borderBottom = "solid 1px white";
    myButton.style.borderBottom = "none";
    let allTask = document.getElementById("all_tasks");
    allTask.style.display = "flex";
    let myTask = document.getElementById("my_tasks");
    myTask.style.display = "none";
    let searchedTask = document.getElementById("searched_tasks");
    searchedTask.style.display = "none";

}

function DashbordMyTask() {
    let allButton = document.getElementById("tasksButtonAll");
    let myButton = document.getElementById("tasksButtonMy");
    myButton.style.borderBottom = "solid 1px white";
    allButton.style.borderBottom = "none";
    let myTask = document.getElementById("my_tasks");
    myTask.style.display = "flex";
    let allTask = document.getElementById("all_tasks");
    allTask.style.display = "none";
    let searchedTask = document.getElementById("searched_tasks");
    searchedTask.style.display = "none";
}

function DashbordSearchedTask() {
    let allButton = document.getElementById("tasksButtonAll");
    let myButton = document.getElementById("tasksButtonMy");
    myButton.style.borderBottom = "none";
    allButton.style.borderBottom = "none";
    let myTask = document.getElementById("my_tasks");
    myTask.style.display = "none";
    let allTask = document.getElementById("all_tasks");
    allTask.style.display = "none";
    let searchedTask = document.getElementById("searched_tasks");
    searchedTask.style.display = "flex";
}