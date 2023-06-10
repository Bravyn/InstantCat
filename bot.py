import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create and train the chatbot
chatbot = ChatBot('My Chatbot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')  # Train the chatbot on English corpus

# Streamlit App
def main():
    st.title("Chatbot MVP")

    # Chatbot interaction
    user_input = st.text_input("You:", key='user_input')
    if st.button("Send"):
        bot_response = chatbot.get_response(user_input)
        st.text_area("Chatbot:", value=str(bot_response), height=200, key='bot_response')

if __name__ == '__main__':
    main()
