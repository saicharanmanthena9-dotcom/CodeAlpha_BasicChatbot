# CodeAlpha Internship - Task 4: Basic Chatbot

def chatbot():
    print("=" * 40)
    print("       BASIC PYTHON CHATBOT")
    print("=" * 40)
    print("Bot: Hi! I'm a simple chatbot.")
    print("Bot: Say hello, ask how I am, or say bye.")
    print("Bot: Type 'bye' to end the chat.\n")

    while True:
        user_message = input("You: ").strip().lower()

        if user_message in ("hello", "hi", "hey"):
            print("Bot: Hi! Nice to meet you!")
        elif user_message in ("how are you", "how are you?"):
            print("Bot: I'm fine, thanks!")
        elif user_message in ("good", "fine", "great", "i am good", "i'm good"):
            print("Bot: That's great to hear!")
        elif user_message in ("bye", "goodbye", "exit", "quit"):
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print("Bot: Sorry, I don't understand. Try hello, how are you, or bye.")

if __name__ == "__main__":
    chatbot()
