# 🦜🔗 Generative AI with LangChain

<p align="center">
  <strong>From basic LLM calls to RAG, tool calling, and AI agents</strong>
</p>

<p align="center">
  A hands-on LangChain learning repository containing Python scripts, Jupyter notebooks, supporting datasets, and complete examples covering the modern LLM application stack.
</p>

---

## 📖 About This Repository

This repository is a practical learning collection built while following the **Generative AI using LangChain** curriculum by **CampusX (Nitish Singh)**.

The material progresses from direct model interaction to increasingly composable LangChain applications:

```text
LLMs → Chat Models → Embeddings → Prompts & Messages
→ Structured Output → Output Parsers → Chains
→ LCEL / Runnables → Document Loaders → Text Splitters
→ Vector Stores → Retrievers → YouTube RAG
→ Tools → Tool Binding / Tool Calling → AI Agents
```

The repository is intentionally hands-on: concepts are demonstrated through focused scripts and notebooks.

---

# 📁 Repository Structure

```text
langchain-models/
├── 1.LLMs/                         # LLM section
├── 2.ChatModels/                   # Chat model interaction
├── 3.Embedding/                    # Embeddings and similarity
├── 4.langchain-prompts/            # Prompts, messages, history, UI
├── 5.langchain-structured-output/  # TypedDict, Pydantic, JSON Schema
├── 6.langchain_output_parsers/    # String, JSON, structured, Pydantic
├── 7.langchain-chains/             # Simple, sequential, parallel, conditional
├── 8.Runnables/                    # LCEL and Runnable abstractions
├── 9.Document-loader/              # Text, CSV, PDF, directory, web
├── 10.text-splitters/              # Character, recursive, language, semantic
├── 11.Vector-store/                # Chroma vector store
├── 12.Retrivers/                   # Vector, MMR, MultiQuery, Wikipedia, compression
├── 13.Youtube_rag/                 # End-to-end YouTube RAG
├── 14.tools_langchain/             # Built-in and custom tools
├── 15.tool_binding/                # Tool binding and tool calling
├── 16.agents/                      # End-to-end agent
├── .gitignore
├── README.MD
└── requirements.txt
```

---

# 1. 🧠 LLMs

### `1.LLMs/1_llm_demo.py`

This file is currently empty. It is a placeholder for the initial LLM section, so there is no implementation to execute in this file yet.

---

# 2. 💬 Chat Models

### `2.ChatModels/2_chatmodel_openai.py`

Demonstrates LangChain's `ChatOpenAI` wrapper.

It:

- Loads environment variables.
- Reads the model from `OPENROUTER_MODEL`.
- Sets temperature to `1.5`.
- Invokes the model with a cricket prompt.
- Prints `response.content`.

```text
Environment → ChatOpenAI → invoke() → AIMessage.content
```

---

# 3. 🔢 Embeddings

## `1_embedding_openai.py`

Creates `OpenAIEmbeddings` using the `Embedding_model` environment variable, generates a 32-dimensional query embedding, and prints the vector.

## `2_embedding_openai_docs.py`

Uses `embed_documents()` to generate embeddings for multiple text documents.

## `3_document_similarity.py`

Demonstrates semantic similarity using:

- OpenAI embeddings
- `sklearn.metrics.pairwise.cosine_similarity`
- A collection of cricket documents
- A query about Jasprit Bumrah

It calculates similarity scores and selects the highest-scoring document.

```text
Documents → Document Embeddings ─┐
                                ├→ Cosine Similarity → Best Match
Query → Query Embedding ────────┘
```

This is the conceptual foundation for the vector-store and retrieval sections.

---

# 4. ✍️ LangChain Prompts

This section covers reusable prompts, chat messages, conversation history, temperature, saved prompt templates, and a Streamlit research assistant.

## `chat_prompt_template.py`

Uses `ChatPromptTemplate.from_messages()` with dynamic `field` and `topic` variables.

## `chatbot.py`

Implements a terminal chatbot using:

- `SystemMessage`
- `HumanMessage`
- `AIMessage`
- Explicit conversation history
- `OPENROUTER_MODEL`
- `OPENAI_BASE_URL`
- `OPENAI_API_KEY`

The model receives the accumulated message history on each turn.

## `message_placeholder.py`

Uses `MessagesPlaceholder` to insert existing chat history into a reusable chat template. The history is loaded from `chat_history.txt`.

## `messages.py`

Demonstrates explicit system, human, and AI message objects and appends the generated AI response back to the message list.

## `prompt-generator.py`

Creates a reusable research-paper summarization `PromptTemplate` accepting:

- `paper_input`
- `style_input`
- `length_input`

It requests mathematical details and analogies where applicable and instructs the model not to guess when information is unavailable.

The template is saved to `template.json`.

## `prompt-ui.py`

A Streamlit **Research Assistant** that lets the user select a paper, explanation style, and explanation length. It loads `template.json`, composes it with the model using LCEL, and displays the result.

## `temperature.py`

A minimal temperature experiment using `ChatOpenAI` with temperature `1.5`.

## `template.json`

Serialized form of the research-paper prompt used by `prompt-ui.py`.

## `chat_history.txt`

Contains a sample refund conversation used by the message-placeholder example.

---

# 5. 🧩 Structured Output

This section demonstrates **TypedDict, Pydantic, JSON Schema, and `with_structured_output()`**.

## `typed_dict.py`

Defines a `Person` TypedDict containing `name` and `age`.

## `pydantic_demo.py`

Defines a `Student` model with:

- Name
- Optional age
- Email validation using `EmailStr`
- CGPA constrained between 0 and 10

It also demonstrates dictionary and JSON serialization.

## `json_schema.json`

Defines a simple student JSON schema with name and age, with name required.

## `with_structured_output_json.py`

Uses a JSON schema to extract structured information from a Samsung Galaxy S24 Ultra review:

- Key themes
- Summary
- Sentiment
- Pros
- Cons
- Reviewer name

## `with_structured_output_pydantic.py`

Uses a Pydantic `Review` model with fields for themes, summary, sentiment, rating, pros, cons, and reviewer.

## `with_structured_output_typed_dict.py`

Uses a TypedDict with `Annotated` field descriptions to extract structured review information.

Overall progression:

```text
TypedDict / Pydantic / JSON Schema
              ↓
model.with_structured_output(...)
              ↓
Machine-readable response
```

---

# 6. 🔄 Output Parsers

## `stroutputparser.py`

Shows the manual two-stage approach:

1. Generate a detailed report.
2. Feed the generated text into a second prompt.
3. Generate a summary.

## `stroutputparser1.py`

Converts the same idea into an LCEL chain using `StrOutputParser`:

```text
Prompt → Model → StrOutputParser
       → Prompt → Model → StrOutputParser
```

## `jsonoutputparser.py`

Uses `JsonOutputParser` and its format instructions to generate parsed JSON output.

## `structuredoutputparser.py`

Uses `ResponseSchema` and `StructuredOutputParser` to request three named facts.

## `pydanticoutputparser.py`

Uses `PydanticOutputParser` with a validated `Person` model requiring name, age greater than 18, and city.

The repository therefore demonstrates the progression from plain strings to increasingly structured output.

---

# 7. 🔗 Chains

## `simple_chain.py`

Builds:

```text
PromptTemplate → ChatOpenAI → StrOutputParser
```

and prints the chain graph.

## `sequential_chain.py`

Creates a two-stage workflow:

```text
Topic → Facts → Five-line Summary
```

## `parallel_chains.py`

Uses `RunnableParallel` to generate:

- A short note
- Five MCQs

The results are then merged into a final report.

## `conditional_chains.py`

Classifies feedback as positive or negative using Pydantic and routes it through `RunnableBranch` to different response chains.

```text
Feedback → Sentiment → Positive/Negative Branch → Reply
```

---

# 8. ⚙️ Runnables & LCEL

## `LCEL.py`

Minimal LCEL example using the pipe operator:

```python
chain = prompt1 | model | parser
```

## `runnable_sequence.py`

Explicit `RunnableSequence` implementation of prompt → model → parser.

## `runnable_parallel.py`

Uses `RunnableParallel` to generate a tweet and a LinkedIn post independently.

## `runnable_passthrough.py`

Uses `RunnablePassthrough` to preserve a generated joke while another branch generates an explanation.

## `runnable_lambda.py`

Wraps a normal Python word-counting function in `RunnableLambda` and combines the result with the generated joke using `RunnableParallel`.

## `runnable_branch.py`

Uses `RunnableBranch` to decide whether a generated report should be summarized based on its word count. Short reports pass through unchanged.

### Runnable abstractions covered

| Component | Purpose |
|---|---|
| `RunnableSequence` | Sequential execution |
| `RunnableParallel` | Independent parallel branches |
| `RunnablePassthrough` | Preserve input |
| `RunnableLambda` | Convert Python functions into Runnables |
| `RunnableBranch` | Conditional routing |
| LCEL `|` | Concise Runnable composition |

---

# 9. 📄 Document Loaders

## `text_loader.py`

Loads `cricket.txt` with `TextLoader`, then sends its content through a prompt → model → parser chain.

## `csv_loader.ipynb`

Uses `CSVLoader` to load `Social_Network_Ads.csv` and inspect the resulting documents.

## `pypdfloader.ipynb`

Uses `PyPDFLoader` on `dl-curriculum.pdf` and inspects page content and metadata.

## `directory_loader.ipynb`

Uses `DirectoryLoader` + `PyPDFLoader` to load PDFs recursively from `books/`. It compares `load()` and `lazy_load()`, including timing experiments.

## `webbase_loader.ipynb`

Uses `WebBaseLoader` to retrieve and inspect content from a web page.

### Supporting data

- `Social_Network_Ads.csv` — CSVLoader source.
- `cricket.txt` — TextLoader source.
- `dl-curriculum.pdf` — PDFLoader source.
- `books/Building Machine Learning Systems with Python - Second Edition.pdf` — DirectoryLoader source.

---

# 10. ✂️ Text Splitters

## `length_based_text_splitter.ipynb`

Introduces `CharacterTextSplitter` and demonstrates chunk size, overlap, custom separators, and PDF document splitting.

The examples use a chunk size of 100 and overlap of 20.

## `recursive_character_text_splitters.ipynb`

Uses `RecursiveCharacterTextSplitter` with hierarchical separators:

```text
\n\n → \n → space → character
```

It is applied both to raw text and PDF documents.

## `language_based_splitter.ipynb`

Uses `RecursiveCharacterTextSplitter.from_language()` with `Language.PYTHON` to split Python source code.

## `sementic_text_splitters.ipynb`

Introduces `SemanticChunker` using OpenAI embeddings. It experiments with semantic breakpoint strategies including standard deviation and percentile thresholds.

### Supporting file

`dl-curriculum (1).pdf` is used by the splitter examples.

---

# 11. 🗄️ Vector Store

## `vector_store.ipynb`

Demonstrates a persistent Chroma vector store using IPL player documents.

It covers:

- LangChain `Document`
- Metadata
- OpenAI embeddings
- Chroma persistence
- Adding documents
- Reading stored data
- Similarity search
- Similarity search with scores
- Metadata filtering
- Updating documents
- Deleting documents

```text
Documents → Embeddings → Chroma → Similarity Search
```

The repository also contains generated `my_chroma_db/` artifacts, including an HNSW index and `chroma.sqlite3`.

---

# 12. 🔍 Retrievers

## `vector_retriver.ipynb`

Creates a Chroma vector store and converts it into a retriever using `as_retriever()`. It compares retriever invocation with direct similarity search.

## `mmr_retrival.ipynb`

Introduces **Maximal Marginal Relevance (MMR)**, balancing query similarity with diversity among retrieved results. The notebook experiments with different `lambda_mult` values.

## `multiquery_retriver.ipynb`

Uses `MultiQueryRetriever` so an LLM can generate multiple interpretations of a query before retrieval. It compares standard vector retrieval with multi-query retrieval.

## `wikipedia_retriver.ipynb`

Uses `WikipediaRetriever` to retrieve multiple Wikipedia documents for a natural-language query.

## `conceptual_compression_retriver.ipynb`

Builds a FAISS retriever and wraps it in `ContextualCompressionRetriever` with an LLM-based `LLMChainExtractor`.

```text
Query → Base Retriever → Relevant Documents → LLM Compressor → Focused Context
```

---

# 13. 🎥 YouTube RAG

## `rag_youtube.ipynb`

A complete RAG application over a YouTube transcript.

### Pipeline

```text
YouTube Video
     ↓
YouTube Transcript API
     ↓
Recursive Character Splitter
     ↓
OpenAI Embeddings
     ↓
FAISS
     ↓
Retriever
     ↓
Retrieved Context
     ↓
Grounded Prompt
     ↓
ChatOpenAI
     ↓
Answer
```

The notebook explicitly handles transcript exceptions, uses `text-embedding-3-small`, retrieves the top two chunks, and instructs the LLM to answer only from the supplied transcript context.

---

# 14. 🛠️ Tools

## `built_in_tools.ipynb`

Demonstrates built-in LangChain tools:

- DuckDuckGo Search
- Shell Tool

## `custom_tools.ipynb`

Demonstrates three custom-tool approaches:

1. `@tool` decorator
2. `StructuredTool` with a Pydantic schema
3. `BaseTool` subclass

The multiplication example is used to inspect tool names, descriptions, arguments, and generated schemas.

## `toolkit.ipynb`

Groups custom `add` and `multiply` tools into a `MathToolKit` class.

---

# 15. 🔧 Tool Binding & Tool Calling

## `tool_calling.ipynb`

Demonstrates the complete manual tool-calling loop:

```text
User → LLM with Bound Tool → Tool Call → Tool Execution → Tool Result → LLM → Final Answer
```

It uses a multiplication tool and `llm.bind_tools()`.

## `currecncy_conversion_tool.ipynb`

Builds a two-tool currency conversion workflow:

- Fetch conversion rate from an external API.
- Convert an amount using that rate.

The notebook then addresses an important issue: the model may attempt to supply an exchange rate itself. It introduces `InjectedToolArg` so the conversion rate can instead be supplied by the application after the external API call.

---

# 16. 🤖 AI Agents

## `endtoend_agent.ipynb`

The final notebook combines model interaction and tools into an agent.

It:

1. Creates a DuckDuckGo search tool.
2. Creates `ChatOpenAI`.
3. Uses LangChain's `create_agent`.
4. Supplies the search tool.
5. Sends a natural-language question.
6. Lets the agent decide how to use the tool.
7. Reads the final response.

The notebook describes the agent loop as:

```text
Thought → Action → Observation
       ↖───────────────↙
             ↓
        Final Answer
```

---

# 🔄 Complete Learning Architecture

```text
                         GENERATIVE AI
                              │
                              ▼
                           LLMs
                              │
                              ▼
                        Chat Models
                              │
                              ▼
                         Embeddings
                              │
                              ▼
                    Prompts & Messages
                              │
                              ▼
                     Structured Output
                              │
                              ▼
                       Output Parsers
                              │
                              ▼
                           Chains
                              │
                              ▼
                       LCEL / Runnables
                              │
                              ▼
                     Document Processing
                              │
                 ┌────────────┼────────────┐
                 ▼            ▼            ▼
              Loaders      Splitters   Vector Store
                                             │
                                             ▼
                                         Retrievers
                                             │
                                             ▼
                                            RAG
                                             │
                                             ▼
                                           Tools
                                             │
                                             ▼
                                       Tool Calling
                                             │
                                             ▼
                                           Agents
                                             │
                                             ▼
                                        Agentic AI
```

---

# 🧰 Technologies Used

| Category | Technologies |
|---|---|
| Language | Python |
| LLM framework | LangChain |
| Model integration | LangChain OpenAI / ChatOpenAI |
| Model routing | OpenRouter configuration in examples |
| Embeddings | OpenAI Embeddings |
| Structured data | TypedDict, Pydantic, JSON Schema |
| Parsers | String, JSON, Structured, Pydantic |
| Composition | LCEL, RunnableSequence, RunnableParallel, RunnableLambda, RunnableBranch |
| Document loaders | TextLoader, CSVLoader, PyPDFLoader, DirectoryLoader, WebBaseLoader |
| Text splitting | Character, Recursive Character, Language-based, Semantic |
| Vector stores | Chroma, FAISS |
| Retrieval | Vector, MMR, MultiQuery, Wikipedia, Contextual Compression |
| RAG | YouTube transcript RAG |
| Tools | DuckDuckGo, Shell, custom tools, toolkits |
| Agents | LangChain `create_agent` |
| UI | Streamlit |
| Environment | python-dotenv |
| Validation | Pydantic |
| Notebook environment | Jupyter |

---

# 🛠️ Setup

## 1. Clone

```bash
git clone https://github.com/Rajendra-Pd-Joshi/langchain-models.git
cd langchain-models
```

## 2. Virtual environment

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

The current requirements file pins versions for LangChain, LangGraph, OpenAI, ChromaDB, Pydantic, Streamlit, Jupyter, scikit-learn, YouTube Transcript API, Wikipedia, DuckDuckGo Search, and related packages.

## 4. Configure environment variables

Examples in the repository use variables including:

```env
OPENAI_API_KEY=your_api_key
OPENROUTER_MODEL=your_model
OPENAI_BASE_URL=your_base_url
Embedding_model=your_embedding_model
EMBEDDING_MODEL=your_embedding_model
OPENAI_MODEL=your_model
```

The exact variables required depend on the example.

> Never commit API keys or other secrets. The repository's `.gitignore` excludes `.env`.

---

# ▶️ Running the Material

For notebooks:

```bash
jupyter notebook
```

For Python examples:

```bash
python path/to/example.py
```

For the Streamlit research assistant:

```bash
streamlit run 4.langchain-prompts/prompt-ui.py
```

---

# 📚 Recommended Learning Order

Follow the numerical progression:

```text
01. LLMs
02. Chat Models
03. Embeddings
04. Prompts
05. Structured Output
06. Output Parsers
07. Chains
08. Runnables / LCEL
09. Document Loaders
10. Text Splitters
11. Vector Stores
12. Retrievers
13. YouTube RAG
14. Tools
15. Tool Binding
16. Agents
```

Later sections build directly on earlier concepts, particularly the progression from embeddings → vector stores → retrievers → RAG and from tools → tool calling → agents.

---

# 📦 Current Dependencies

The repository currently pins:

```text
chromadb==1.5.9
duckduckgo_search==8.1.1
jupyter==1.1.1
langchain==1.3.11
langchain-chroma==1.1.0
langchain-community==0.4.2
langchain-core==1.4.8
langchain-experimental==0.4.2
langchain-openai==1.3.3
langgraph==1.2.8
openai==2.32.0
pandas==3.0.2
pydantic==2.13.3
python-dotenv==1.2.2
scikit-learn==1.8.0
streamlit==1.57.0
wikipedia==1.4.0
youtube-transcript-api==1.2.4
```

---

# 🔐 Repository Notes

- `.env`, `myenv/`, Python cache directories, and compiled Python files are ignored.
- The repository contains generated Chroma database artifacts under `11.Vector-store/my_chroma_db/`.
- Several examples depend on external APIs and therefore require valid credentials and network access.
- The existing repository does not specify a license; it is best treated as an educational/personal reference unless a license is added.

---

## 🙏 Acknowledgment

The existing repository identifies the curriculum and instructional flow as based on the **Generative AI using LangChain** playlist by **Nitish Singh (CampusX)**.

---

**Happy Learning and Building with LangChain! 🦜🔗🚀**
