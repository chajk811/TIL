function doSomething(subject, callback) {
	console.log(`이제 ${subject} 과목평가 준비를 시작해볼까?`)
	callback()
}

function alterFinish(){
	console.log('며칠 안남았는데?')
}

doSomething('djnago', alterFinish)