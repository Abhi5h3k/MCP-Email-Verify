import os
from typing import Any

import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables from .env file
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("verify_email")


# Constants
ABSTRACT_API_KEY = os.getenv("ABSTRACT_API_KEY", "your_api_key_here")
ABSTRACT_API_URL = "https://emailvalidation.abstractapi.com/v1/"


@mcp.tool()
async def verify_email(email: str) -> dict[str, Any]:
    """
    Validates an email address using an external email validation API.

    This function checks the validity, deliverability, and other attributes of an email address.
    It returns a detailed dictionary containing information about the email's format, domain,
    and SMTP server.

    Args:
        email (str): The email address to validate.

    Returns:
        dict[str, Any]: A dictionary containing detailed validation results. The dictionary
        includes the following keys:
            - "email" (str): The email address being validated.
            - "autocorrect" (str): Suggested autocorrection if the email is invalid or malformed.
            - "deliverability" (str): The deliverability status of the email (e.g., "DELIVERABLE").
            - "quality_score" (str): A score representing the quality of the email address.
            - "is_valid_format" (dict): Whether the email is in a valid format.
                - "value" (bool): True if the format is valid, False otherwise.
                - "text" (str): A textual representation of the format validity (e.g., "TRUE").
            - "is_free_email" (dict): Whether the email is from a free email provider.
                - "value" (bool): True if the email is from a free provider, False otherwise.
                - "text" (str): A textual representation (e.g., "TRUE").
            - "is_disposable_email" (dict): Whether the email is from a disposable email service.
                - "value" (bool): True if the email is disposable, False otherwise.
                - "text" (str): A textual representation (e.g., "FALSE").
            - "is_role_email" (dict): Whether the email is a role-based email (e.g., "admin@domain.com").
                - "value" (bool): True if the email is role-based, False otherwise.
                - "text" (str): A textual representation (e.g., "FALSE").
            - "is_catchall_email" (dict): Whether the domain uses a catch-all email address.
                - "value" (bool): True if the domain is catch-all, False otherwise.
                - "text" (str): A textual representation (e.g., "FALSE").
            - "is_mx_found" (dict): Whether MX records are found for the email domain.
                - "value" (bool): True if MX records are found, False otherwise.
                - "text" (str): A textual representation (e.g., "TRUE").
            - "is_smtp_valid" (dict): Whether the SMTP server for the email domain is valid.
                - "value" (bool): True if the SMTP server is valid, False otherwise.
                - "text" (str): A textual representation (e.g., "TRUE").

    Example:
        >>> await verify_email("thanos@snap.io")
        {
            "email": "thanos@snap.io",
            "autocorrect": "",
            "deliverability": "UNDELIVERABLE",
            "quality_score": "0.00",
            "is_valid_format": {
                "value": true,
                "text": "TRUE"
            },
            "is_free_email": {
                "value": false,
                "text": "FALSE"
            },
            "is_disposable_email": {
                "value": false,
                "text": "FALSE"
            },
            "is_role_email": {
                "value": false,
                "text": "FALSE"
            },
            "is_catchall_email": {
                "value": false,
                "text": "FALSE"
            },
            "is_mx_found": {
                "value": false,
                "text": "FALSE"
            },
            "is_smtp_valid": {
                "value": false,
                "text": "FALSE"
            }
        }
    Raises:
        ValueError: If the API key is not found in the environment variables.
        requests.exceptions.HTTPError: If the API request fails (e.g., 4xx or 5xx error).
        Exception: For any other unexpected errors.
    """
    # Check if the API key is available
    if not ABSTRACT_API_KEY:
        raise ValueError("API key not found in environment variables.")

    # Construct the API URL
    api_url = f"{ABSTRACT_API_URL}?api_key={ABSTRACT_API_KEY}&email={email}"

    try:
        # Make the API request
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        # Parse the JSON response
        result = response.json()

        # Return the validation results
        return result

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (e.g., 4xx, 5xx)
        raise requests.exceptions.HTTPError(f"HTTP error occurred: {http_err}")
    except Exception as err:
        # Handle any other errors
        raise Exception(f"An error occurred: {err}")


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
