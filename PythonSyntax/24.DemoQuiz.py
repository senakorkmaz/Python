class Question():
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self,answer):
        return self.answer == answer

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for p in question.choices:
            print(f'-{p}')
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score +=1
        self.questionIndex +=1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
            
    def showScore(self):
        print('score:',self.score,'/',len(self.questions))
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex +1
        if questionNumber > totalQuestion:
            print('Quiz bitti')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(50,'-'))

questionText1 ='En iyi programlama dili hangisidir ?'
questionText2 ='En populer programlama dili hangisidir ?'
answerList = ['C#','python','javascript','java']
q1 = Question(questionText1,answerList,'python')
q2 = Question(questionText2,answerList,'python')
questions = [q1,q2]

quiz = Quiz(questions)
quiz.loadQuestion()