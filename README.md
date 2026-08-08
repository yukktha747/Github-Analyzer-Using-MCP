# 🚀 GitHub Profile Analyzer using Model Context Protocol (MCP)

> An AI-powered GitHub Profile Analyzer built using **FastMCP**, **Model Context Protocol (MCP)**, **OpenRouter LLMs**, **Streamlit**, and the **GitHub REST API**.

---

# 📖 Overview

GitHub Profile Analyzer is an AI-powered application that allows users to analyze any public GitHub profile using natural language.

Instead of directly calling the GitHub API, the application follows the **Model Context Protocol (MCP)** architecture.

The AI Agent first discovers the available MCP tools, asks the LLM which tool should be used, executes the selected tool through the MCP Client and MCP Server, retrieves GitHub data, and finally generates a natural language response for the user.

This project demonstrates how **LLMs**, **MCP**, and **AI Agents** can work together to build intelligent applications.

---

# 📸 Project Preview


<img width="1885" height="903" alt="Screenshot 2026-08-08 224236" src="https://github.com/user-attachments/assets/acb72906-d265-40a8-8a66-5b8f51cd971a" />

---

<img width="1697" height="711" alt="image" src="https://github.com/user-attachments/assets/104bf94a-141b-4a8f-8950-2657e3e4768f" />


---

# 🏗️ System Architecture

```text
                           USER
                             │
                             ▼
                     Streamlit UI
                             │
                             ▼
                      GitHub Agent
                             │
          ┌──────────────────┴──────────────────┐
          ▼                                     ▼
     OpenRouter LLM                        MCP Client
          │                                     │
          └──────────────────┬──────────────────┘
                             ▼
                        FastMCP Server
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
 github_profile     github_languages     analyze_profile
                             │
                             ▼
                      GitHub Service
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
          Cache Service          GitHub REST API
```

---

# 🔄 Complete Request Flow

```text
User

│

▼

Streamlit UI

│

▼

GitHubAgent.ask()

│

▼

Discover MCP Tools

│

▼

MCP Client

│

▼

FastMCP Server

│

▼

List Available Tools

│

▼

GitHubAgent

│

▼

OpenRouter LLM (1st Call)

│

▼

LLM Chooses Tool

│

▼

MCP Client

│

▼

FastMCP Server

│

▼

GitHubService

│

▼

Cache

│

No Cache?

│

▼

GitHub REST API

│

▼

Analysis Object

│

▼

MCP Client

│

▼

OpenRouter LLM (2nd Call)

│

▼

Generate Human Friendly Response

│

▼

Streamlit UI

│

▼

User
```

---

# 🎯 Features

* Analyze any public GitHub profile
* Retrieve profile information
* Fetch repository details
* Generate language statistics
* AI-powered natural language interaction
* Dynamic MCP Tool Discovery
* FastMCP Server
* OpenRouter LLM Integration
* File-based Caching
* Streamlit User Interface
* Modular Architecture

---

# 🛠️ Tech Stack

## Programming Language

* Python

---

## AI & LLM

* OpenRouter
* Google Gemini 2.5 Flash
* OpenAI SDK
* Model Context Protocol (MCP)

---

## MCP

* FastMCP
* MCP Python SDK

---

## Frameworks

* Streamlit
* Requests
* Pydantic
* python-dotenv

---

## APIs

* GitHub REST API

---

## Developer Tools

* Git
* GitHub
* Visual Studio Code
* PyCharm

---

---

# ⚙️ How the Application Works

## Step 1

The user enters a natural language query.

Example

```text
Analyze the GitHub profile of torvalds
```

---

## Step 2

The request reaches the **GitHub Agent**.

---

## Step 3

The GitHub Agent asks the **MCP Client** to discover all available tools.

The MCP Client communicates with the FastMCP Server.

The server returns tools such as:

* github_profile
* github_repositories
* github_languages
* analyze_profile

---

## Step 4

The GitHub Agent sends

* User Question
* Available Tools

to the LLM.

---

## Step 5

The LLM determines which tool should be executed.

Example

```
analyze_profile(username="torvalds")
```

---

## Step 6

The GitHub Agent instructs the MCP Client to execute the selected tool.

---

## Step 7

The MCP Client sends the request to the FastMCP Server.

---

## Step 8

The FastMCP Server invokes the corresponding Python function.

```
analyze_profile()
```

---

## Step 9

The GitHub Service checks whether the data already exists in the cache.

If cache exists

↓

Return cached data

Otherwise

↓

Call GitHub REST API

---

## Step 10

GitHub data is converted into Pydantic Models.

An Analysis object is created.

---

## Step 11

The MCP Server returns the Analysis object to the MCP Client.

---

## Step 12

The GitHub Agent sends the tool output back to the LLM.

The LLM converts structured data into a human-friendly explanation.

---

## Step 13

The final response is displayed inside Streamlit.

---

# 🔧 MCP Tools

## github_profile

Returns the public GitHub profile information.

Example

```
Get the GitHub profile of torvalds
```

---

## github_repositories

Returns all public repositories.

Example

```
Show repositories of torvalds
```

---

## github_languages

Generates programming language statistics.

Example

```
Show languages used by torvalds
```

---

## analyze_profile

Provides a complete GitHub profile analysis.

Example

```
Analyze the GitHub profile of torvalds
```

---

# 💾 Caching

The project uses a lightweight file-based cache.

Benefits include

* Faster responses
* Reduced GitHub API requests
* Lower API rate-limit usage
* Improved application performance

---

# 🔑 Environment Variables

Create a `.env` file.

```env
OPENROUTER_API_KEY=your_openrouter_api_key

GITHUB_TOKEN=your_github_token

MODEL=google/gemini-2.5-flash

CACHE_DURATION=3600

LOG_LEVEL=INFO
```

---

# 🚀 Installation

Clone the repository

```bash
git clone <repository_url>

cd github_profile
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Run Streamlit

```bash
streamlit run app.py
```

---

# 🧪 Testing

List MCP Tools

```bash
python mcp_client/test_client.py
```

Test AI Agent

```bash
python mcp_client/test_agent.py
```

---

# 💬 Example Questions

* Analyze the GitHub profile of torvalds.
* Show repositories of octocat.
* What programming languages does tensorflow use?
* Summarize the GitHub profile of microsoft.
* List repositories of yukktha747.

---

# 🚀 Future Enhancements

* Repository topic analysis
* GitHub contribution graph
* Commit history visualization
* Issue & Pull Request analysis
* PDF report generation
* Docker support
* OAuth authentication
* Persistent database cache
* Multi-user GitHub comparison

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

* Model Context Protocol (MCP)
* FastMCP Server Development
* MCP Client Development
* AI Agents
* Tool Calling / Function Calling
* OpenRouter Integration
* LLM Applications
* GitHub REST API
* Streamlit
* Pydantic Models
* File-based Caching
* Modular Software Architecture
* Prompt Engineering

---

# 📄 License

This project is created for educational and learning purposes.

Feel free to use and extend it for your own projects.
