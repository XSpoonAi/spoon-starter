## Streaming ChatBot Quick Start

# Installation

## Prerequisites

- Python 3.12 or higher
- Git
- Virtual environment (recommended)

## Quick Installation

### 1. Clone the Repository

```bash
git clone https://github.com/XSpoonAi/spoon-core.git

git clone https://github.com/XSpoonAi/spoon-toolkit.git

By the end, your project layout will look like this:

spoon/
├── spoon-core
├── spoon-starter
└── spoon-toolkit

```

### 2. Create Virtual Environment

```bash
# macOS/Linux

python -m venv spoon

source spoon/bin/activate

# Windows (PowerShell)

python -m venv spoon

.\spoon\Scripts\Activate.ps1


```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install as Package 

```bash
cd spoon-core
pip install -e .
cd spoon-toolkit
pip install -e .
```

---

### Configure an OpenRouter (or other OpenAI-compatible) API key\*\*

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

- **`Cleanup failed for ...`** – means a provider isn’t configured; remove it from `config.json` if unused.
- **`websockets.legacy` DeprecationWarning** – upstream warning, safe to ignore.
