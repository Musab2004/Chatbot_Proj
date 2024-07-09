# Chatbot Project with Function Calling

## Overview

This project implements a chatbot using Streamlit and OpenAI's GPT-3.5-turbo model. The chatbot supports natural language interactions and integrates several functionalities including weather checking via API, Google search, and JSON creation for video generation from text inputs.

## Features

- **Natural Language Processing**: Uses OpenAI's GPT-3.5-turbo model for conversational responses.
- **API Integrations**:
  - Current weather checking via WeatherAPI.
  - Google search API integration for fetching relevant information.
  - API for generating JSON descriptions for video creation based on text inputs.
- **Session Management**: Tracks conversation history and manages user sessions using Streamlit's session state.

## Setup

To run the chatbot locally, follow these steps:

1. Clone the repository and navigate to the project directory.

```bash
  git clone git@github.com:Musab2004/Chatbot_Proj.git
  cd Chatbot-Proj
  pip install -r requirements.txt
  streamlit run app.py
```

## Usage

- Enter your queries in the chat input.
- The chatbot responds with natural language replies and performs requested tasks like weather checks, Google searches, and video JSON generation.
