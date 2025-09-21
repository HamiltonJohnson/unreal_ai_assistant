# Unreal Engine AI Assistant

**Version:** 1.0  
**Author:** Hamleet  
**Category:** Scripting  
**Plugin Type:** Editor Plugin

## Overview

Unreal Engine AI Assistant is a Python-powered plugin that enables large language models (LLMs) to analyze Blueprint graphs directly inside the Unreal Editor. It extracts logic from selected Blueprints, formats it as structured JSON, and sends it to an LLM (Claude 3 Haiku via OpenRouter) for explanation, improvement suggestions, and automatic fix recommendations.

This tool is designed to help developers:
- Understand complex Blueprint logic
- Identify potential issues or inefficiencies
- Receive actionable feedback from an AI assistant
- Accelerate debugging and refactoring workflows

---

## Features

- 🔍 Extracts nodes and pin connections from Blueprint Event Graphs
- 🧠 Sends Blueprint logic to Claude 3 Haiku via OpenRouter API
- 🛠️ Receives natural language explanations and improvement suggestions
- 🧩 Supports Editor Utility Widgets and standard Blueprints
- 📦 Plug-and-play integration with Unreal’s Editor Scripting Utilities

---

## 🛠️ Installation

1. Clone or copy the plugin into your project:
2. Enable the plugin in **Edit → Plugins → Scripting → Unreal Engine AI Assistant**

3. Ensure the following plugins are enabled:
- ✅ Editor Scripting Utilities
- ✅ Python Editor Script Plugin

4. Restart the editor.

---

## 🐍 Python Setup

Make sure your Python environment is configured:

- Unreal must have Python scripting enabled
- Add the following paths to your script:
```python
sys.path.append(r"C:\UE_5.4\Engine\Plugins\Experimental\PythonScriptPlugin\Content\Python")
sys.path.append(r"C:\PROJECT_NAME\Plugins\UnrealAIAssist")

