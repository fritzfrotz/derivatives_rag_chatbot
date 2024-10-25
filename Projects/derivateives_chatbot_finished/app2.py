import streamlit as st
import time
from functions1 import retrieve_and_generate_answer, save_feedback, save_conversation

st.title("🤖 The Derivatives Chatbot")

# Initialize session state for the conversation
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'feedback_given' not in st.session_state:
    st.session_state['feedback_given'] = False
if 'feedback_text' not in st.session_state:
    st.session_state['feedback_text'] = ""

# Function to display the chat bubbles (themed for bot and user messages)
def display_chat():
    for message in st.session_state['history']:
        if message["type"] == "user":
            st.markdown(f"""
                <div class='message-row'>
                    <div class='icon'>
                        <img src='https://img.icons8.com/color/48/000000/user-male-circle--v1.png' width='40' />
                    </div>
                    <div class='message user-message'>
                        {message['content']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class='message-row'>
                    <div class='icon'>
                        <img src='https://img.icons8.com/color/48/000000/robot-2.png' width='40' />
                    </div>
                    <div class='message bot-message'>
                        {message['content']}
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Inject CSS for better chat styling and to position the input at the bottom
st.markdown("""
    <style>
    .message-row {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    .icon {
        flex-shrink: 0;
        margin-right: 10px;
    }
    .message {
        padding: 10px;
        border-radius: 10px;
        max-width: 80%;
    }
    .user-message {
        background-color: #daf7dc;
        text-align: left;
        animation: fadeIn 0.5s;
    }
    .bot-message {
        background-color: #f0f0f5;
        text-align: left;
        animation: fadeIn 0.5s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .fixed-input {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: white;
        padding: 10px;
        z-index: 999;
        border-top: 2px solid #ccc;
    }
    .separator {
        margin: 20px 0;
        border-top: 2px solid #ccc;
    }
    </style>
    """, unsafe_allow_html=True)

# Create a container to hold the input box, and make it fixed at the bottom
input_container = st.empty()

# Input for the user's question inside the container
with input_container.container():
    query = st.text_input("Ask a question to the chatbot", key="input_text", label_visibility="collapsed", placeholder="Type your message here...")

    # Button to send the query to the backend
    send_button = st.button("Send")

if send_button and query:
    # Save user message to the conversation history
    st.session_state['history'].append({"type": "user", "content": query})

    # Show the loading spinner while processing the backend response
    with st.spinner("🤖 Bot is thinking..."):
        try:
            # Call the function to retrieve and generate the answer
            answer, sources = retrieve_and_generate_answer(query)

            # Save bot response to the conversation history
            st.session_state['history'].append({"type": "bot", "content": answer})

            # Display only the new user message and bot response (not the entire history again)
            #display_chat()

            st.write(answer)

            # Save the conversation (optional)
            save_conversation(query, answer, "./data/")  # Update this path if necessary

            # Display the sources inside an expander if available
            if sources:
                with st.expander("Show sources"):
                    for source in sources:
                        st.write(f"- {source}")

        except Exception as e:
            st.error(f"An error occurred: {e}")

# Add a horizontal line with a title to separate the chat history from the input section
st.markdown("""
    <div style='text-align: center; margin-top: 20px; margin-bottom: 20px;'>
        <h3 style='display: inline-block; padding: 0 10px; background-color: white;'>
            Chat History
        </h3>
        <hr style='border: 1px solid #ccc; margin-top: -10px;'/>
    </div>
""", unsafe_allow_html=True)

# Display the chat history
display_chat()

# Sidebar for Feedback
with st.sidebar:
    st.subheader("End Session and Provide Feedback")

    # Ask for feedback (show feedback input only if the session is not ended yet)
    if not st.session_state['feedback_given']:
        st.session_state['feedback_text'] = st.text_area("Please provide your feedback:", value=st.session_state['feedback_text'])

        # Submit feedback button
        if st.button("Submit Feedback", key="feedback_button"):
            if st.session_state['feedback_text']:
                # Simulate feedback sending animation
                with st.spinner("Submitting your feedback..."):
                    time.sleep(1.5)

                try:
                    # Call the function to save feedback
                    save_feedback(st.session_state['feedback_text'], "Overall Session Feedback", "./data/", "Overall Feedback")  # Update this path if necessary
                    st.session_state['feedback_given'] = True
                    st.success("Thank you for your feedback!")
                except Exception as e:
                    st.error(f"Failed to save feedback: {e}")
            else:
                st.warning("Please enter some feedback before submitting.")
    else:
        st.info("Feedback has already been submitted. Thank you!")
