from VCIBD2 import takeCommand

def divide():
    print("tell the two numbers you want to divide.")
    takeCommand.speak("tell the two numbers you want to divide.")
    print("tell the first number : ")
    takeCommand.speak("tell the first number : ")
    DF = int(takeCommand.takeCommand())
    print("tell the second number : ")
    takeCommand.speak("tell the second number : ")
    DS = int(takeCommand.takeCommand())
    Q = (DF/DS)
    print(f"The quotient is : {Q}")
    takeCommand.speak(f"The quotient is : {Q}")