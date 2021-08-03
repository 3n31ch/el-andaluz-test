import os
import re
import json

def read(filename):
	return open(filename, "r", encoding='utf-8').read()

def write(filename, text):
	if os.path.exists(filename):
		os.remove(filename)
	file = open(filename, "a", encoding='utf-8')
	file.write(text)
	file.close()

def answers():
	text = read("files/answers.txt")
	text = re.sub('"', '\\"', text) #scape "
	text = re .sub("Página (.[0-9]*)", "", text) #remove Página
	text = re .sub("\n.\n", "", text) #remove Página
	text = re .sub("\n(?! )", "", text) #remove Página
	text = re .sub("\n ", "\n", text) #remove Página
	
	write('files/processed-answers.txt', text)
	
	text = re .sub("([0-9]+)\.- ([ABCD]+)", r'"\1":"\2",', text) #remove Página
	text = re .sub(" ", "", text)
	text = re .sub("\n", "", text)
	text = text[:-1]
	text = "{"+ text +"}"
	write('files/answers.json', text)
	answers = json.loads(text)
	return answers


def clear(answers):
	text = read("files/quiz.txt")
	text = re.sub('"', '\\"', text) #scape "
	text = re .sub("Página (.[0-9]*)", "", text) #remove Página
	text = re .sub("\n.\n", "", text) #remove Página
	text = re .sub("\n(?! )", "", text) #remove Página
	text = re .sub("\n ", "\n", text) #remove Página
	text = text[1:-1]
	text = re .sub("([abcd]+)\) ", r"\n\1)", text) #remove Página
	text = re .sub("(d\).*) ([0-9]+\.-.*\na\))", r"\1\n\2", text) #remove Página
	text = re .sub("(opción )\n([abcd]\))", r"\1\2", text) #remove Página
	text = re .sub("(opciones )\n(a\))", r"\1\2", text) #remove Página
	
	write('files/processed-quiz.txt', text)
	
	lines = text.splitlines()

	questions = []
	tmp_category = None
	tmp_question = None
	tmp_answer = None
	for line in lines:
		line = line.strip()
		if bool(re.match("[0-9]+-.*", line)):
			tmp_category = re.sub("([0-9]+)-(.*)", r'{"id": "\1", "name": "\2"}', line)
			tmp_category = json.loads(tmp_category)
		if bool(re.match("[0-9]+\.-.*", line)):
			if tmp_question is not None:
				if len(tmp_question['answers']) != 4:
					print(tmp_question['id'] + "->" + str(len(tmp_question['answers'])))
				questions.append(tmp_question)
			tmp_question = re.sub("([0-9]+)\.-(.*)", r'{"id": "\1", "question": "\2", "answers": []}', line)
			tmp_question = json.loads(tmp_question)
			tmp_question["category"] = tmp_category
		if bool(re.match("[abcd]+\).*", line)):
			is_correct = 'false'
			letter = re.sub("([abcd]+)\)(.*)", r'\1', line)
			#print(tmp_question["id"])
			if answers[tmp_question["id"]].lower() == letter:
				is_correct = 'true'
			tmp_answer = re.sub("([abcd]+)\)(.*)", r'{"id": "\1", "answer": "\2", "is_correct": '+is_correct+'}', line)
			tmp_answer = json.loads(tmp_answer)
			tmp_question["answers"].append(tmp_answer)
	write('files/quiz.json', json.dumps(questions, ensure_ascii=False).encode('utf8').decode())
	
answers = answers()
clear(answers)