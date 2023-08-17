function closeTodoCreateModal(){
	var modal = document.getElementById("add_todo_modal");
	if(modal.style.display!="none"){
		modal.style.display = "none";
	}else{
		console.log("close else");
	}
}

function openTodoCreateModal(){
	var modal = document.getElementById("add_todo_modal");
	if(modal.style.display == "none" || modal.style.display==""){
		modal.style.display = "block";
	}else{
		console.log("open else");
	}
}