new Vue({
	el: '#app',
	data: {
		numberOfQuestions: 20,
		quiz: quiz,
		questions: []
	},
	methods: {
		loadQuestions() {
			const checkboxs  = document.querySelectorAll('input[type="radio"]')
			console.log(checkboxs)
			checkboxs.forEach(checkbox => {
				checkbox.checked = false
			})
			this.questions = []
			if(this.numberOfQuestions > 100) this.numberOfQuestions = 100
			if(this.numberOfQuestions < 1) this.numberOfQuestions = 1
			const randomIds = []
			for (let index = 0; index < this.numberOfQuestions; index++) {
				while(true) {
					const randomId = Math.floor(Math.random() * this.quiz.length-1)
					if(!randomIds.includes(randomId)) {
						this.questions.push(quiz[randomId])
						randomIds.push(randomId)
						break;
					}
				}
			}
			
		}
	}
});
