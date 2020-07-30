import random
import time
import pyttsx3
import speech_recognition as sr

rock = "rock"
paper = "paper"
scissors = ["scissor","scissors"]

# Stats
user_wins = 0
computer_wins = 0
tie = 0
rounds_played = 0
invalid_inputs = 0

# Text to speech conversion
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Voice recognition using microphone
def recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now!")
        speak("Speak Now!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        choice = r.recognize_google(audio)
        if choice in ["rock","paper", "scissor", "scissors","yes","no"]:
            print("You said: " + choice)
            speak("You said: " + choice)
            return choice
        else:
            return False
    except sr.UnknownValueError:
        print("Sorry! I Could not understand.")
        speak("Sorry! I Could not understand.")
        return False
    except sr.RequestError as e:
        print("Error {0}".format(e))
        speak("Error {0} occured!".format(e))
        return False


while True:
    c_choice = random.choice([rock,paper,scissors])
    print("Say Rock, Paper or Scissors ")
    speak("Say Rock, Paper or Scissors ")
    u_choice = recognition()
    if u_choice == False:
        invalid_inputs += 1
        rounds_played += 1
        continue
        
    rounds_played += 1

    if u_choice != rock and u_choice != paper and u_choice not in scissors:
        invalid_inputs += 1
    
    if u_choice == rock and c_choice == paper:
        print("Computer Wins!")
        speak("Computer Wins!")
        computer_wins += 1
    if u_choice == rock and c_choice in scissors:
        print("User Wins!")
        speak("User Wins!")
        user_wins += 1
    if u_choice == rock and c_choice == rock:
        print("Tie!")
        speak("Tie!")
        tie += 1

    if u_choice == paper and c_choice in scissors:
        print("Computer Wins!")
        speak("Computer Wins!")
        computer_wins += 1
    if u_choice == paper and c_choice == rock:
        print("User Wins!")
        speak("User Wins!")
        user_wins += 1
    if u_choice == paper and c_choice == paper:
        print("Tie!")
        speak("Tie!")
        tie += 1

    if u_choice in scissors and c_choice == rock:
        print("Computer Wins!")
        speak("Computer Wins!")
        computer_wins += 1
    if u_choice in scissors and c_choice == paper:
        print("User Wins!")
        speak("User Wins!")
        user_wins += 1
    if u_choice in scissors and c_choice in scissors:
        print("Tie!")
        speak("Tie!")
        tie += 1
    print("Rounds played: {}".format(rounds_played))
    speak("Rounds played: {}".format(rounds_played))    

    # STATS
    if rounds_played % 5 == 0:
        print("You have played {} games! ".format(rounds_played))
        speak("You have played {} games! ".format(rounds_played))
        while True:
            print("Continue playing ? Say Yes or No. ")
            speak("Continue playing ? Say Yes or No. ")
            choice = recognition()
            if choice == "no":
                print("\nFINAL STATS: ")
                print("Rounds Played: {}".format(rounds_played))
                print("Rounds Considered VALID: {}".format(rounds_played - invalid_inputs))
                print("Rounds Cancelled Due to INVALID input: {}".format(invalid_inputs))
                print("Rounds Won by USER: {}".format(user_wins))
                print("Rounds Won by COMPUTER: {}".format(computer_wins))
                print("Rounds TIE: {}".format(tie))            
                print("User's WIN% : {:.2f}% \n".format((user_wins / (rounds_played - invalid_inputs))*100))

                speak("FINAL STATS: ")
                speak("Rounds Played: {}".format(rounds_played))
                speak("Rounds Considered VALID: {}".format(rounds_played - invalid_inputs))
                speak("Rounds Cancelled Due to INVALID input: {}".format(invalid_inputs))
                speak("Rounds Won by USER: {}".format(user_wins))
                speak("Rounds Won by COMPUTER: {}".format(computer_wins))
                speak("Rounds TIE: {}".format(tie))            
                speak("User's WIN% : {:.2f}% \n".format((user_wins / (rounds_played - invalid_inputs))*100))
                break
            elif choice == "yes":
                break
            else:
                print("Enter a valid input!")
                speak("Enter a valid input!")
        if choice == "no":
            break

time.sleep(3)
            
    

    
