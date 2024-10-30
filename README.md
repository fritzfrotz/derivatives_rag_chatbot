
Derivatives Chatbot

Welcome to the Derivatives Chatbot project! This interactive chatbot, built with Streamlit, LangChain, and OpenAI, provides answers to market finance questions, specifically focusing on derivatives. The bot retrieves relevant content from a document-based knowledge base, processes user questions, and generates concise responses. This README will guide you through the setup, usage, and structure of the project.

Project Overview
The chatbot leverages LangChain’s document retrieval and large language model (LLM) functionalities to answer derivatives-related questions. It includes features for:

Document processing and text chunking
Vector storage and retrieval
Conversation history management
User feedback collection
The chatbot interface is designed with Streamlit, featuring a user-friendly UI and customizable chat bubble design for better readability.

Project Structure
The project consists of two main files:

app2.py: The main Streamlit application that handles the UI, manages conversation history, and interfaces with the backend functions.
functions1.py: Contains core functions for document loading, text chunking, vector storage, retrieval, prompt formatting, and user feedback saving.
Features
Dynamic Chat Interface: Displays user and bot messages with themed chat bubbles.
Document Processing: Converts Word documents to LangChain-compatible format, with text chunking to optimize retrieval.
Vector Store with Chroma: Stores document embeddings for fast, context-relevant retrieval.
Conversation History Management: Stores and displays conversation history for user reference.
Feedback Collection: Collects and stores user feedback at the end of each session.
Setup
Prerequisites
Python 3.8 or higher
Pip (Python package installer)
Environment file for secure API key storage
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/derivatives_chatbot.git
cd derivatives_chatbot
Create and Activate a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
Install the Required Packages:

bash
Copy code
pip install -r requirements.txt
Create a .env File:

Place your API keys in a .env file in the root directory. An example .env:

plaintext
Copy code
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your_langchain_api_key
OPENAI_API_KEY=your_openai_api_key
Load Data Files:

Add your .docx files containing Q&A content related to market finance and derivatives to the ./data/ directory.

Usage
Start the Streamlit Application:

Run the following command in the terminal:

bash
Copy code
streamlit run app2.py
Interacting with the Chatbot:

Enter your questions in the chat input at the bottom of the page.
View responses from the bot, along with sources if available.
End the session by providing feedback through the sidebar.
Feedback and Conversation Logs:

Feedback and conversation logs are saved in the ./data/ directory by default.
Adjust the directory path as necessary in functions1.py.
Future Improvements
Enhanced Error Handling: Add more try-except blocks for file I/O and API calls to improve reliability.
Modularized Functions: Refactor complex functions in app2.py and functions1.py for readability and ease of testing.
Optimized Chat Rendering: Implement optimized chat rendering to handle longer conversations more efficiently.
Environment Variable Verification: Add checks to ensure required environment variables are loaded properly.
Unit Tests: Add tests for core functions in functions1.py to ensure code reliability and maintainability.
Move Conversation History to Database: Implement a more persistent storage solution for conversation history, using a database.
Contributing
Contributions are welcome! Please fork the repository, make your changes in a new branch, and submit a pull request with a detailed description of the changes.

License
This project is licensed under the MIT License.

