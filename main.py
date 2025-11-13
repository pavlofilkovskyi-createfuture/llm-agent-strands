"""
This is a sample code to demonstrate how to create an agent using AWS Bedrock model
and integrate it with GitHub MCP Client wrapper to perform operations on GitHub repositories.

use VS Code with Jupyter extension, 
in order to run this file as a jupyter notebook in Python Interactive mode
https://code.visualstudio.com/docs/python/jupyter-support-py

make sure to install ipykernel package in your environment (included in requirements.txt)
and install recommended extensions for VS Code (see .vscode/extensions.json):
- Python (ms-python.python)
- Jupyter (ms-toolsai.jupyter)
"""

# %% import necessary modules from strands library
from strands.models import BedrockModel

# Bedrock model instance
# https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/amazon-bedrock/
bedrock_model = BedrockModel(
    model_id="openai.gpt-oss-20b-1:0",
    temperature=0.0,
    top_p=0.8,
)

# %% lets create an agent with some tools provided by strands as well as a custom tool
# https://strandsagents.com/latest/documentation/docs/api-reference/tools/
from strands_tools import calculator, current_time
from strands import tool
from strands import Agent

@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count the occurrences of a specific letter in a word.
    """
    if not isinstance(word, str) or not isinstance(letter, str):
        return 0
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")
    return word.lower().count(letter.lower())

agent = Agent(
    tools=[calculator, current_time, letter_counter],
    model = bedrock_model
)

prompt = """
I've got a few questions for you:

1. Calculate the square root of 1764
2. Tell me how many times letter 'r' occurs in "strawberry" word ?
3. What is the current time now ?
"""

agent(prompt)

# optionally we can get response returned from agent invocation and print it:
# response = agent(prompt)
# print(response)

# -------------------------------------------------------------------------

# %% instantiate GitHub MCP Client wrapper:
import os
from datetime import datetime
from strands import Agent
from wrapper import GitHubMCPClient

from dotenv import load_dotenv
load_dotenv()  # Loads from .env file

GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")
github_mcp_client = GitHubMCPClient(access_token=GITHUB_ACCESS_TOKEN) # type: ignore None

# https://strandsagents.com/latest/documentation/docs/user-guide/concepts/tools/mcp-tools
with github_mcp_client:
    agent = Agent(
        tools=github_mcp_client.list_tools_sync(),
        model = bedrock_model
    )
    
    branch_name = f"test-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    repo = "pavlofilkovskyi-createfuture/test-repo"
    
    prompt = f"""
    this repo {repo} contains files with mathematical expressions,
    find and evaluate those expressions,
    check if there are any mistakes in the expressions,
    if mistakes found:
        - fix mistakes in a new branch, named {branch_name},
        - create pull request from {branch_name} branch to main branch,
        - provide me with the link to the created pull request.
    
    technical requirements for the task:
    - always create new branch and new PR, 
    - if there is an existing branch or PR with the same content: 
        - create new branch with the branch name provided to you 
        - create new PR for changes in this new branch
    - always prefer encoding files in UTF-8, if not possible use ASCII encoding,
    - always use plain text format, no base64 or other encodings for content,
    - use only tools provided to you
    """
    
    result = agent(prompt)
    print(result)

# %%
