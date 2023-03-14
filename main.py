import random


class Question:
    def setup(self):
        print(
            "New question: please read the question, type your answer and press enter"
        )


class ArithmeticQuestion(Question):
    def __init__(self):
        self.num1 = random.randint(1, 100)
        self.num2 = random.randint(1, 100)
        self.operator = random.choice(["+", "-", "*"])

    def show_question(self):
        print(f"{self.num1} {self.operator} {self.num2} = ?")

    def check_answer(self, answer):
        if self.operator == "+":
            return int(answer) == self.num1 + self.num2
        elif self.operator == "-":
            return int(answer) == self.num1 - self.num2
        elif self.operator == "*":
            return int(answer) == self.num1 * self.num2
        else:
            return False


class WordQuestion(Question):
    def __init__(self):
        self.word = random.choice(["PYTHON", "JAVA", "RUBY"])
        self.missing_index = random.randint(0, len(self.word) - 1)

    def show_question(self):
        word_list = list(self.word)
        word_list[self.missing_index] = "_"
        print(" ".join(word_list))

    def check_answer(self, answer):
        return answer.upper() == self.word[self.missing_index]


def main():
    quiz = [ArithmeticQuestion() for i in range(5)] + [WordQuestion() for i in range(5)]
    random.shuffle(quiz)

    correct_answers = 0

    for question in quiz:
        question.setup()
        question.show_question()
        answer = input("")
        correct = question.check_answer(answer)
        if correct:
            correct_answers += 1
            print("** Correct, well done! **")
            input("press any key to continue")
        else:
            print("Wrong answer, try again later!")
            break

    print(f"You got {correct_answers} out of {len(quiz)} questions correct!")


if __name__ == "__main__":
    main()
