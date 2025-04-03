#import nltk
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK resources (if needed)
nltk.download('punkt')
nltk.download('stopwords')

# Function to process user input and generate responses
def chatbot_response(user_input):
    # Tokenize the input
    tokens = word_tokenize(user_input.lower())

    # Remove common stop words (like "the", "is", etc.)
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Simple keyword-based responses
    if "hello" in filtered_tokens or "hi" in filtered_tokens:
        return "Hello! How can I assist you today?"
    elif "name" in filtered_tokens:
        return "I'm your friendly chatbot! What's your name?"
    elif "how" in filtered_tokens and "you" in filtered_tokens:
        return "I'm just a chatbot, but I'm here to help!"
    elif "bye" in filtered_tokens or "exit" in filtered_tokens:
        return "Goodbye! Have a wonderful day!"
    else:
        return "I'm not sure how to respond to that, but I'm learning!"

# Main function to run the chatbot
def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()


