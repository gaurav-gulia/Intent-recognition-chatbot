import streamlit as st
from main1 import response
from tensorflow.keras.models import load_model

model = load_model('model.h5')

# Define colors for each intent
intent_colors = {
    "Greeting": "green",
    "GreetingResponse": "lightblue",
    "CourtesyGreeting": "orange",
    "CourtesyGreetingResponse": "violet",
    "CurrentHumanQuery": "red",
    "NameQuery": "maroon",
    "RealNameQuery": "darkred",
    "TimeQuery": "tomato",
    "Thanks": "coral",
    "NotTalking2U": "brown",
    "UnderstandQuery": "firebrick",
    "Shutup": "crimson",
    "Swearing": "salmon",
    "GoodBye": "teal",
    "CourtesyGoodBye": "turquoise",
    "WhoAmI": "navy",
    "Clever": "indigo",
    "Gossip": "gold",
    "Jokes": "yellow",
    "PodBayDoor": "lime",
    "PodBayDoorResponse": "olive",
    "SelfAware": "cyan",
}

# Streamlit UI
st.title("Intent Recognition Bot")

st.write("Interact with the bot by typing your message below. Type 'quit' to end the conversation.")

# Initialize session state for conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Container for chat history
chat_container = st.container()

# Display the conversation history
with chat_container:
    for entry in st.session_state.conversation:
        speaker = entry[0]
        message = entry[1]
        if speaker == "user":
            st.markdown(f"""<div style="font-size:20px"><strong>You: </strong>{message}</div>""", unsafe_allow_html=True)
        else:
            intent_text = entry[2]
            color = intent_colors.get(intent_text, "gray")
            st.markdown(f"""
                <div style="font-size:20px" ><strong>Bot:</strong> <span >{message}</span>
                    <div style="background-color: {color}; color: white; padding: 5px; border-radius: 5px; display: inline-block; margin-left: 10px;">
                        {intent_text}
                    </div>
                </div>
            """, unsafe_allow_html=True)

# User input form at the bottom
st.write('<hr>', unsafe_allow_html=True)  # Horizontal line separator
with st.form(key='user_input_form', clear_on_submit=True):
    user_message = st.text_input("You:")
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_message:
    if user_message.lower() == "quit":
        st.write("Conversation ended.")
    else:
        # Get intent and response
        user_message = user_message.lower()
        bot_response, intent = response(user_message, model)

        # Append user message and bot response to the conversation history
        st.session_state.conversation.append(("user", user_message))
        st.session_state.conversation.append(("bot", bot_response, intent))

    # Rerun the script to update the conversation
    st.experimental_rerun()
