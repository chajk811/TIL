const me = {
	name: 'ssafy', // 키가 한 단어 일 때
	'phone number': '01012341234', // 키가 여러 단어 일 때
	appelProducts: {
		ipad: '2018pro',
		iphon2: '7',
		macbook: '2019pro',
	}
}

console.log(me.name) // ssafy
console.log(me['name']) // ssafy
console.log(me['phone number']) // 키가 여러 단어인 경우 반드시 [] 접근

console.log(me.appelProducts)
console.log(me.appelProducts.ipad)

// Object Literal (객체 표현법)
var books = ['Learning JS', 'Eloquent JS']

var comics = {
	'DC': ['joker', 'aquaman'],
	'Marvel': ['captain marvel', 'avengers'],
}

var magazines = null

var bookShop = {
	books: books,
	comics: comics,
	magazines: magazines,
}

console.log(bookShop)

var bookShopTwo = {
	books,
	comics,
	magazines,
}

console.log(bookShopTwo)

///////////////////

// JSON
const jsonData = JSON.stringify({ // JSON => String
	coffee: 'Americano',
	iceCream: 'Mint Choco',
})

console.log(jsonData)
console.log(typeof jsonData)

const parseData = JSON.parse(jsonData)
console.log(parseData)
console.log(typeof parseData)
