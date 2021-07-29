# Create your classes here

class Student(object):
    """A student."""

    def __init__(self, first_name, last_name, address):

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """A question in an exam along with its correct answer."""

    def __init__(self, question, correct_answer):

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):

        user_response = input(self.question)
        if user_response == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    """An exam including its name and the questions within it."""

    def __init__(self, name):

        self.name = name
        self.questions = []

    def add_question(self, question):

        self.questions.append(question)
