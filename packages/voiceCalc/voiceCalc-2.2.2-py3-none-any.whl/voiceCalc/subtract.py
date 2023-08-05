from VCIBD2 import takeCommand

def subtract():
    print("tell the two numbers you want to substract.")
    takeCommand.speak("tell the two numbers you want to substract.")
    print("tell the first number : ")
    takeCommand.speak("tell the first number : ")
    SF = int(takeCommand.takeCommand())
    print("tell the second number : ")
    takeCommand.speak("tell the second number : ")
    SS = int(takeCommand.takeCommand())
    D = (SF-SS)
    print(f"The diffrence is : {D}")
    takeCommand.speak(f"The diffrence is : {D}")