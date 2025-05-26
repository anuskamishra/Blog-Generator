# 📝 LLaMA-2 Blog Generator

Generate high-quality blogs using the LLaMA-2 language model with a simple and interactive Streamlit web interface.



---

## 🚀 Project Overview

This project allows users to generate blogs dynamically by entering a topic, selecting a target audience, and choosing the desired word count. It uses **Meta's LLaMA-2** language model locally (via `CTransformers`) without relying on APIs, making it efficient, cost-effective, and private.

---

## 🧠 Features

- ✍️ Generate blog content on any topic
- 👥 Customize tone based on target audience (Researchers, Data Scientists, Common People)
- 🔢 Set custom word count limits
- 🧱 Offline LLM inference with no API keys required
- ⚡ Instant response using Streamlit UI

---

## 🛠️ Tech Stack

| Component        | Tool/Library             |
|------------------|---------------------------|
| UI Framework     | Streamlit                 |
| Language Model   | LLaMA-2 (GGML quantized)  |
| LLM Interface    | LangChain + CTransformers |
| Prompt Building  | LangChain PromptTemplate  |
| Environment      | Python + venv             |

---

---

## ⚙️ Installation & Setup

1. **Clone the repo**

```bash
git clone https://github.com/your-username/blog-generator.git
cd blog-generator

setup_instructions:
  - step: "Set up virtual environment"
    commands:
      - "python -m venv venv"
      - "source venv/bin/activate      # On Windows: venv\\Scripts\\activate"

  - step: "Install dependencies"
    commands:
      - "pip install -r requirements.txt"

  - step: "Download the LLaMA-2 Model"
    note: |
      Due to file size limits, the `.bin` model is not included in this repo.
      Download `llama-2-7b-chat.ggmlv3.q8_0.bin` from TheBloke's HuggingFace page:
      https://huggingface.co/TheBloke/Llama-2-7B-GGML

    actions:
      - "Place the downloaded file inside the `Models/` folder"

  - step: "Run the App"
    commands:
      - "streamlit run app.py"


