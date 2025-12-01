success = True  # to control the game so we can retry in some cases
username = ""


def ask_yes_no_answer(question: str) -> str:
    while True:
        ans = input(question).strip().lower()
        if ans in ["y", "yes", "yep", "ok", "yeah", "yea", "sure", "yup", "yess", "yepp", "yup", "yeahh"]:
            return "yes"
        if ans in ["n", "no", "nope", "nah", "nooo", "nop", "nopeee"]:
            return "no"
        print("❗ Please write yes or no!")
