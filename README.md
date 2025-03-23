# [MCP Email Verify](https://anthropic-mcp.hashnode.dev/model-context-protocol-mcp-a-beginners-guide-to-the-future-of-ai-communication)  


A lightweight **Model Context Protocol (MCP)** server that enables your LLM to validate email addresses. This tool checks email format, domain validity, and deliverability using the AbstractAPI Email Validation API. Perfect for integrating email validation into AI applications like Claude Desktop.  

---

# What is Model Context Protocol (MCP)?
At its core, MCP is a standardized protocol designed to streamline communication between AI models and external systems. Think of it as a universal language that allows different AI agents, tools, and services to interact seamlessly.

![MCP drawio (1)](https://github.com/user-attachments/assets/567c5853-3e3c-49c5-bec2-07325f000be2)

---

## **Features**  
- **Email Verification**: Verify email addresses in real-time.  
- **MCP Integration**: Seamlessly connect with MCP-compatible LLMs.  
- **Easy Setup**: Built with Python and the MCP SDK for quick deployment.  

---

# MCP follows a client-server architecture:

![client server drawio](https://github.com/user-attachments/assets/1f7141c9-d96f-4a5d-a8ab-944b8daa81f4)

---

# Watch the Demo
Click the image below to watch a video demo of the MCP Email Verify tool in action:

[![Screenshot 2025-03-23 115525](https://github.com/user-attachments/assets/9604fef7-a4f4-4f38-81f1-883752498e1c)](https://youtu.be/myTWSKR5GvE)


---

## **Requirements**  
- **Python**: Python 3.11.0 or higher.  
- **UV**: 0.6.9 or higher.  

---
## **Setup**  

**1. Clone the Repository**  
```
git clone https://github.com/Abhi5h3k/MCP-Email-Verify.git
cd MCP-Email-Verify
```
**2. Install UV**
 
If you don’t have UV installed, you can install it using the following commands:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Verify the installation:
```
uv --version
```

**3. Set Up the Virtual Environment**

Create a virtual environment using UV:
```
uv venv
```
Activate the virtual environment:
On Windows:
```
.venv\Scripts\activate
```
**4. Install Dependencies** 
Install the required dependencies from pyproject.toml using UV:
```
uv install
```

## Running the Server
1. Set Up Environment Variables
Create a .env file in the root directory and add your [AbstractAPI](https://app.abstractapi.com/api/email-validation/tester) key:
```
ABSTRACT_API_KEY=your_api_key_here
```
2. Run the Server
Start the MCP server:
```
uv run server.py
```

## Usage

1. Register the Server with Claude Desktop
  Update the claude_desktop_config.json file to include your MCP server:
  
  ```
  {
      "mcpServers": {
          "verify_mail": {
              "command": "uv",
              "args": [
                  "--directory",
                  "C:\\ABSOLUTE\\PATH\\TO\\MCP-Email-Verify",
                  "run",
                  "server.py"
              ]
          }
      }
  }
  ```

![image](https://github.com/user-attachments/assets/72d98b2b-4b1b-41a6-9669-99aefda32867)


2. Restart Claude Desktop
  Restart Claude Desktop to detect the new tool.

3. Verify Emails
  Use prompts like:

  "I was trying to email Thanos at thanos@snap.io to ask him to bring back my favorite TV show, but I’m not sure if it’s a valid email. Can you check if it’s real or just a snap in the dark?"


## Development
Formatting and Linting
This project uses black and isort for code formatting and import sorting.

1. Install development dependencies:
   ```
    uv add black isort --dev
    ```
2. Format the code:
   ```
   black .
   ```
3. Sort imports:
  ```
    isort .
  ```


## Set up pre-commit
```bash
pre-commit install
pre-commit run --all-files
```


Available On
Smithery.ai Server: [MCP Email Verify](https://smithery.ai/server/@Abhi5h3k/mcp-email-verify)

Article: Model Context Protocol (MCP): [A Beginner's Guide to the Future of AI Communication](https://anthropic-mcp.hashnode.dev/model-context-protocol-mcp-a-beginners-guide-to-the-future-of-ai-communication)
