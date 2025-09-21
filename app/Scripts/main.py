import sys

# Add plugin and PythonScriptPlugin paths
sys.path.append(r"C:\UE_5.4\Engine\Plugins\Experimental\PythonScriptPlugin\Content\Python")
sys.path.append(r"C:\PROJECT_NAME\Plugins\UnrealAIAssist")
from UnrealAIAssist.Scripts.logic.llm import run_llm_analysis


def run(prompt: str):
    print(f"Prompt received: {prompt}")
    return run_llm_analysis(prompt)

# Optional CLI entry point
if __name__ == "__main__":
    # Example usage: python main.py "Explain this Blueprint"
    if len(sys.argv) > 1:
        input_prompt = " ".join(sys.argv[1:])
        result = run(input_prompt)
        print("LLM Response:\n", result)
    else:
        print("Usage: python main.py <prompt>")