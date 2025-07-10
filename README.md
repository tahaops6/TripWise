# TripWise 🧳✨

**TripWise** is an Agentic AI-powered travel planning assistant that intelligently builds travel itineraries and suggestions based on user preferences, prompt interactions, and real-time data. This project combines a Streamlit user interface with a FastAPI backend and a modular, agent-based architecture for high flexibility and scalability.

---

## 🚀 Features

- 🤖 Agentic AI-driven travel recommendation system  
- 🌐 REST API built with FastAPI  
- 💬 Prompt-based planning using LLMs  
- 📊 Streamlit-based interactive UI  
- 🧱 Modular, extensible code structure  
- 📁 Built-in logging, error handling, and configuration modules  

---

## 🧠 Under the Hood: How It Works

TripWise is built using a modern, modular architecture designed for flexibility, scalability, and fast iteration. Here's a breakdown of how the main components work together:

---

### ⚙️ System Overview

TripWise operates in a modular pipeline across three main layers:

1. **Frontend (Streamlit)**
   - Accepts user queries (e.g. "Plan a trip to Tokyo for 4 days").
   - Sends a POST request to the backend API.

2. **Backend (FastAPI)**
   - Receives the request and routes it to the AI Agent.
   - Validates input and handles exceptions/logging.

3. **Agentic AI Core**
   - Builds a prompt based on user input using stored templates.
   - Sends the prompt to OpenAI’s LLM.
   - Parses and formats the response into a travel plan.

4. **LLM (OpenAI / GPT-4)**
   - Processes the prompt and returns an intelligent travel itinerary.

5. **Response**
   - The travel plan is sent back through the FastAPI layer to Streamlit.
   - Displayed beautifully in the frontend.

---

### 🔧 Key Technologies

#### FastAPI
- Acts as the backend server and API provider.
- Accepts POST requests with user input (via `/query` endpoint).
- Handles routing, validation, and returns structured responses to the frontend.
- Exposes an interactive OpenAPI (Swagger) UI at `/docs`.

#### Streamlit
- Provides the interactive web UI for users to submit travel queries.
- Communicates with the FastAPI backend using `requests.post()` to trigger trip generation.
- Displays AI-generated itineraries in a user-friendly format.

#### Agentic AI Core (`agent/`)
- Contains modular agents that construct dynamic prompts and handle response formatting.
- Acts as the decision-making layer for integrating user context, preferences, and tool output.

#### LLM Prompt Engine (`prompt_library/`)
- Houses reusable and editable prompt templates for interacting with OpenAI or other LLMs.
- Can be extended to support different planning styles, languages, or tones.

#### OpenAI API
- Powers the natural language processing layer using LLMs like GPT-4 to build itineraries, suggest places, and generate narratives.
- Prompts are built dynamically using user queries and predefined templates.

#### Utilities (`utils/`, `tools/`, `logger/`, `exception/`)
- Provide helpers for logging, error catching, environment variable loading, and modular tool functions.

#### `.env` Configuration
- Manages secrets and API keys securely using `python-dotenv`.
- Centralized config system ensures safe, scalable, and deployable environments.

---

### 🔄 Data Flow Example

1. **User submits a query** via the Streamlit interface.  
2. Streamlit sends the query to the **FastAPI** backend (`/query` endpoint).  
3. FastAPI passes the input to an **agent** that dynamically builds an LLM prompt.  
4. The **OpenAI API** is called with the generated prompt.  
5. The agent formats the LLM response into a human-readable itinerary.  
6. The response is sent back to Streamlit and displayed in the UI.

---

## 🛠️ Tech Stack

- Python 3.10+  
- Streamlit (UI)  
- FastAPI (API)  
- OpenAI / LLM-based Prompts  
- dotenv (.env management)  
- Logging & exception handling utilities  

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/TripWise.git
cd TripWise
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory with the following:

```env
OPENAI_API_KEY=your_openai_key
OTHER_API_KEYS=optional_other_keys
```

---

## ▶️ Running the Application

### 🖥️ Streamlit Frontend

To launch the interactive UI:

```bash
streamlit run streamlit_app.py
```

### 🧠 FastAPI Backend

To start the API server:

```bash
uvicorn main:app --reload --port 8000
```

## 📂 Project Structure

```
TripWise/
│
├── agent/              # Core agent logic for trip planning
├── config/             # Configuration management
├── exception/          # Custom exception handlers
├── logger/             # Logging setup
├── notebook/           # Exploratory notebooks (if any)
├── prompt_library/     # Stored AI prompt templates
├── tools/              # Data processing tools
├── utils/              # Utility functions
├── main.py             # FastAPI app entrypoint
├── streamlit_app.py    # Streamlit UI app entrypoint
├── requirements.txt    # Python dependencies
├── setup.py            # Packaging script
├── .env                # Environment variables (excluded from git)
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, submit pull requests, or open issues to propose new features or fixes.

---

## 🌐 Contact

Have questions or want to collaborate? Please open an issue or reach out via GitHub.
