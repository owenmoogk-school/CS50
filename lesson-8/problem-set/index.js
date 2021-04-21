function multipleChoiceSubmit(obj){
	buttons = document.getElementsByClassName("failed")
	for (let i = 0; i < buttons.length; i++){
		button = buttons[i]
		button.classList.remove('failed')
	}
	buttons = document.getElementsByClassName("accepted")
	for (let i = 0; i < buttons.length; i++){
		button = buttons[i]
		button.classList.remove('accepted')
	}
	if (obj.classList.contains('correct')){

		obj.classList.add('accepted')
	}
	else{
		obj.classList.add('failed')
	}
}

function checkCountry(){
	country = document.getElementById("countryInput").value
	country = country.toLowerCase()
	document.getElementById('countryAnswerButton').classList = ''
	if (country == 'switzerland'){
		document.getElementById('countryAnswerButton').classList.add('accepted')
	}
	else{
		document.getElementById('countryAnswerButton').classList.add('failed')
	}
}