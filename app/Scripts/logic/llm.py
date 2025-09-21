from Scripts.logic.blueprints import generate_prompt_from_selected_blueprint
import requests


def call_claude(prompt):
    # Log the prompt being sent to Claude
    print("Sending prompt to Claude:\n", prompt)

    # Set up request headers for OpenRouter API
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",  # Replace with your actual key or load from env
        "Content-Type": "application/json"
    }

    # Construct the payload for Claude 3 Haiku model
    data = {
        "model": "anthropic/claude-3-haiku",
        "messages": [{"role": "user", "content": prompt}]
    }

    # Send the request to OpenRouter and log the raw response
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    print("Claude response:\n", response.text)

    # Extract and return the assistant's reply from the response JSON
    return response.json()["choices"][0]["message"]["content"]


def run_llm_analysis(custom_prompt=None):
    # Generate a base prompt from the currently selected Blueprint in the Unreal Editor
    base_prompt = generate_prompt_from_selected_blueprint()
    if not base_prompt:
        return "No valid Blueprints found."

    # If the user provided an additional prompt, append it to the base prompt
    if custom_prompt:
        base_prompt += f"\n\nUser prompt:\n{custom_prompt}"

    # Try sending the prompt to Claude and return the response
    try:
        response_text = call_claude(base_prompt)
    except Exception as e:
        # Handle any errors during the API call
        response_text = f"Error calling Claude: {str(e)}"

    return response_text
