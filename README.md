# Medical Query Assistant

A Python-based Medical Query Assistant that leverages LangChain, Pinecone, Streamlit, and Google Generative AI to provide accurate and responsive medical information from the Gale Encyclopedia of Medicine.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Setup and Installation](#setup-and-installation)
4. [Usage](#usage)
   - [Ingesting Medical Data](#ingesting-medical-data)
   - [Running the Application](#running-the-application)
5. [Project Structure](#project-structure)
6. [Environment Variables](#environment-variables)
7. [Dependencies](#dependencies)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgments](#acknowledgments)

## Introduction

The Medical Query Assistant is a tool designed to assist with querying medical information using natural language. It processes medical documents, indexes them with Pinecone, and provides a user-friendly interface powered by Streamlit for querying this data. The assistant supports both text and voice input, and responds with both text and audio output.

## Features

- **Natural Language Processing:** Supports querying medical data in natural language.
- **Voice and Text Input:** Users can input queries via text or voice.
- **Audio Response:** Converts responses to audio using Google Text-to-Speech.
- **Streamlit Interface:** A simple and interactive web interface.
- **Pinecone Vector Store:** Efficient document indexing and retrieval.
- **Google Generative AI Integration:** Utilizes Google's latest generative AI for natural language understanding.

## Setup and Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- Pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AKomplished-bug/Medical-chatbot-.git
   cd Medical-chatbot-

2. Create a virtual environment and activate it:
   
   '''bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required Python packages:

   '''bash
   pip install -r requirements.txt

4. Set up your environment variables by creating a .env file:

   '''bash
   cp sample.env .env



