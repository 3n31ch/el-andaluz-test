new Vue({
	el: '#app',
	data: {
		numberOfQuestions: 20,
		quiz: quiz,
		mode: 'LIST',
		questions: [],
		page: 1,
		pageSize: 100
	},
	mounted() {
		this.changeMode()
	},
	methods: {
		loadQuestions() {
			const checkboxs  = document.querySelectorAll('input[type="radio"]')
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
			
		},
		changeMode() {
			this.questions = []
			if(this.mode === 'LIST') {
				this.loadList(1)
			}
		},
		loadList(page) {
			const checkboxs  = document.querySelectorAll('input[type="radio"]')
			checkboxs.forEach(checkbox => {
				checkbox.checked = false
			})
			this.questions = []
			this.page = page
			for (let index = (this.page - 1) * this.pageSize; index < this.page * this.pageSize && index < this.quiz.length; index++) {
				this.questions.push(this.quiz[index])
			}

		}
	}
});
