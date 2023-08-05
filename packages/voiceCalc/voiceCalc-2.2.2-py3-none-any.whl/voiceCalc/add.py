from VCIBD2 import takeCommand


def add():
    print("tell the two numbers you want to add.")
    takeCommand.speak("tell the two numbers you want to add.")
    print("tell the first number : ")
    takeCommand.speak("tell the first number : ")
    AF = int(takeCommand.takeCommand())
    print("tell the second number : ")
    takeCommand.speak("tell the second number : ")
    AS = int(takeCommand.takeCommand())
    S = (AF+AS)
    print(f"The sum is : {S}")
    takeCommand.speak(f"The sum is : {S}")