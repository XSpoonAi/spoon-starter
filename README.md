## Streaming ChatBot Quick Start

# Installation

## Prerequisites

- Python 3.11 or higher
- Git
- Virtual environment (recommended)

## Quick Installation

### 1. Clone the Repository

```bash
git clone https://github.com/XSpoonAi/spoon-core.git
cd spoon-core
git clone https://github.com/XSpoonAi/spoon-toolkit.git
cd spoon-toolkit
```

### 2. Create Virtual Environment

```bash
# macOS/Linux
python3 -m venv spoon-env
source spoon-env/bin/activate

# Windows (PowerShell)
python -m venv spoon-env
.\spoon-env\Scripts\Activate.ps1
```

> 💡 On newer Apple Silicon Macs the `python` shim may not point to Python 3.
> Use `python3` for all commands unless you have explicitly configured `python`
> to target Python 3.10 or later.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install as Package (Optional)

```bash
pip install -e .
```
---
### Configure an OpenRouter (or other OpenAI-compatible) API key**  
   Put the key into `.env`:
   ```
   OPENROUTER_API_KEY=sk-xxxx
   ```
   You can adjust the `llm_provider` and `model_name` in `streaming_agent.py`’s `ChatBot(...)`.

---

### 2. Run the Demo
```bash
python spoon-starter/starter/streaming_chatbot.py
```
The script asks three generic topics in sequence. Each round prints:

- ` Streaming ChatBot response...` – LLM tokens stream in real time.

---


### 3. Tips
- **`Cleanup failed for ...`** – means a provider isn’t configured; remove it from `config.json` if unused.
- **`websockets.legacy` DeprecationWarning** – upstream warning, safe to ignore.


