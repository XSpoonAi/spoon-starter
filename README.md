## Streaming ChatBot Quick Start

# Installation

## Prerequisites

- Python 3.12 or higher
- Git
- Virtual environment (recommended)

## Quick Installation

### 1. Create Virtual Environment

```bash
# macOS/Linux

python -m venv spoon

source spoon/bin/activate

# Windows (PowerShell)

python -m venv spoon

.\spoon\Scripts\Activate.ps1


```
### 2. Clone the Repository

 Install the core SDK (and optionally the toolkits package)

```bash
pip install spoon-ai-sdk      # core framework
pip install spoon-toolkits      # extended blockchain & data toolkits
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


---

### Configure an OpenRouter or other API key（include gemini，anthropic，deepseek，openai）\*\*

Put the key into `.env`:

```
OPENROUTER_API_KEY=sk-xxxx
```

You can adjust the `llm_provider` and `model_name` in `streaming_chatbot.py`’s `ChatBot(...)`.

---

### 2. Run the Demo

```bash
python spoon-starter/streaming_chatbot.py
```

The script asks three generic topics in sequence. Each round prints:

LLM tokens stream in real time.

---

### 3. Tips

- **`Cleanup failed for ...`** – means a provider isn’t configured; safe to ignore.
- **`websockets.legacy` DeprecationWarning** – upstream warning, safe to ignore.
