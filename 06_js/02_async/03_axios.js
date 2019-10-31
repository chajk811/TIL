const axios = require('axios')

axios.get('http://jsonplaceholder.typicode.com/posts')
	.then(response =>	{
		console.log(response)
	})
	.catch(err => {
		console.log(err)
	})