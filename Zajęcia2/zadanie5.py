from typing import List, Iterator

class SimpleChatbot(Iterator[str]):
    def __init__(self, questions: List[str]):
        self.questions = questions
        self.index = 0

    def __iter__(self) -> "SimpleChatbot":
        return self

    def __next__(self) -> str:
        if self.index < len(self.questions):
            question = self.questions[self.index]
            self.index += 1
            return question
        else:
            raise StopIteration


bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?", "Jakie jest twoje ulubione jedzenie?"])

for question in bot:
    print(question)
    input("Odpowiedź: ") 