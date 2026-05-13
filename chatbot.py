def chatbot():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["hello!","hello","hey!","hi!"]:
            print("chatbot:  Hi there!")
        elif user_input.lower() in["how are you?"]:
            print("chatbot:  I'm doing well, thanks for asking!")  
        elif user_input.lower() in ["goodbye!","goodbye","bye!","bye"]:
            print("chatbot:  Goodbye! Have a great day!")
            break
        else:
            print("chatbot:  Sorry, I didn't understand that.")    
            
chatbot()        
