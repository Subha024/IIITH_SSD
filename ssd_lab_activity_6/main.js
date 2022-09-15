document.addEventListener('keydown', changeToDarkMode)

// let keysPressed = {};

// document.addEventListener('keydown', (event) => {
//    keysPressed[event.key] = true;
// });

function changeToDarkMode(event) {
    if(event.ctrlKey == true && event.key == 'x') {
        if(document.body.style.backgroundColor == "white") {
            document.body.style.backgroundColor = "black";
            document.body.style.color = "white";
        } else {
            document.body.style.backgroundColor = "white";
            document.body.style.color = "black";
        }
    }
}

function dragstartHandler(evt) {
    evt.dataTransfer.setData("MyDraggedElementId", evt.target.id);
}

function dragoverHandler(evt) {
    evt.preventDefault();
}

function dropHandler(evt) {
    evt.preventDefault();

    var elementId = evt.dataTransfer.getData("MyDraggedElementId");
    evt.target.apppendChild(document.getElementById(elementId));
}