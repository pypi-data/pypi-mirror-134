from VCIBD2 import takeCommand

def multiply():
    print("tell the two numbers you want to multiply.")
    takeCommand.speak("tell the two numbers you want to multiply.")
    print("tell the first number : ")
    takeCommand.speak("tell the first number : ")
    MF = int(takeCommand.takeCommand())
    print("tell the second number : ")
    takeCommand.speak("tell the second number : ")
    MS = int(takeCommand.takeCommand())
    P = (MF*MS)
    print(f"The product is : {P}")
    takeCommand.speak(f"The product is : {P}")