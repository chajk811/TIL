// function sleep_3s(){
// 	setTimeout(()=> console.log('wake up'), 3000)
// }

// console.log('Start sleeping')
// sleep_3s()
// console.log('End of program')

// function first() {
// 	console.log('first')	
// }

// function second() {
// 	console.log('second')	
// }

// function third() {
// 	console.log('third')	
// }

// first()
// setTimeout(second, 1000)
// third()


// console.log('hi')
// setTimeout(function ssafy(){
// 	console.log('ssafy')
// }, 100)
// console.log('bye')

function printHellow() {
	console.log('hello from baz')	
}

function  baz() {
	setTimeout(printHellow, 3000)
}

function bar() {
	baz()
}

function foo() {
	bar()
}

foo()