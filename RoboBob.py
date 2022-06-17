import signal
import sys
import numexpr as ne
import platform

question_bank = [
    {
        "question": "what is your name?",
        "answer": "RoboBob"
    },
    {
        "question": "what is your age?",
        "answer": "20"
    },
]


def signal_handler(sig, frame):
    print('\nGood Bye!')
    sys.exit(0)


def handleInput(input_value):
    for question in question_bank:
        if input_value in question['question']:
            return question['answer']
    try:
        return ne.evaluate(input_value)
    except:
        pass
    return "Please enter different Question"


def askQuestion():
    input_value = input("Question> ")
    response = handleInput(input_value)
    print(f"Answer: {response}")
    askQuestion()


if __name__ == "__main__":
    if platform.system() == 'Windows':
        signal.signal(signal.SIGTERM, signal_handler)
    else:
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTSTP, signal_handler)
    print("Welcome in RoboBob!")
    askQuestion()
