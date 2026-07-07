# Generative AI using LangChain 🦜🔗

This repository contains hands-on code implementations and Jupyter Notebooks built while following the **Generative AI using LangChain** playlist by CampusX (Nitish Singh).

It serves as a comprehensive guide and personal reference for building LLM-powered applications, progressing from basic API calls to modern LangChain architectures using LCEL, RAG, and AI Agents.

## 🚀 Key Topics Covered

The repository is structured methodically, covering the following core concepts:

1. **Foundations & Models**
   - Working with standard LLMs vs. ChatModels.
   - Managing System, Human, and AI messages.
   - Generating text embeddings.

2. **Prompts & Structured Outputs**
   - Dynamic inputs using `PromptTemplate` and `ChatPromptTemplate`.
   - Forcing predictable LLM responses using `with_structured_output` (Pydantic, TypedDict, JSON Schemas).
   - Implementing output parsers.

3. **Chains & LangChain Expression Language (LCEL)**
   - Building traditional chains.
   - Moving to modern LCEL syntax with `RunnableSequence`, `RunnableParallel`, `RunnablePassthrough`, and `RunnableLambda`.

4. **Retrieval-Augmented Generation (RAG)**
   - **Document Loaders:** Ingesting PDFs, CSVs, and web data.
   - **Text Splitters:** Chunking text using `RecursiveCharacterTextSplitter` and related strategies.
   - **Vector Stores:** Indexing and storing embeddings.
   - **Retrievers:** Implementing retrieval techniques on top of vector stores.
   - **Project:** **YouTube RAG Chatbot** (`13.Youtube_rag`) — chatting with a video's transcript.

5. **Tools & AI Agents**
   - Binding native Python functions and external APIs as tools to models.
   - Building autonomous AI agents capable of reasoning and executing tasks sequentially.

## 📁 Repository Structure

\`\`\`text
📦 langchain-models
 ┣ 📂 1.LLMs                          # Basic LLM invocation
 ┣ 📂 2.ChatModels                    # Chat model interfaces & message types
 ┣ 📂 3.Embedding                     # Text embeddings
 ┣ 📂 4.langchain-prompts             # Prompt templates
 ┣ 📂 5.langchain-structured-output   # Structured outputs (Pydantic, TypedDict, JSON Schema)
 ┣ 📂 6.langchain_output_parsers      # Output parsers
 ┣ 📂 7.langchain-chains              # Traditional chains
 ┣ 📂 8.Runnables                     # LCEL: RunnableSequence, RunnableParallel, etc.
 ┣ 📂 9.Document-loader                # Document loaders
 ┣ 📂 10.text-splitters               # Text splitting strategies
 ┣ 📂 11.Vector-store                 # Vector store indexing
 ┣ 📂 12.Retrievers                   # Retrieval techniques
 ┣ 📂 13.Youtube_rag                  # End-to-end YouTube RAG project
 ┣ 📂 14.tools_langchain              # Defining tools
 ┣ 📂 15.tool_binding                 # Binding tools to models
 ┣ 📂 16.agents                       # Agent construction & execution
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
\`\`\`

## 🛠️ Setup & Installation

To run the notebooks and Python scripts locally, you will need Python 3.9+ and API keys for whichever model provider a given notebook uses.

**1. Clone the repository**

\`\`\`bash
git clone https://github.com/Rajendra-Pd-Joshi/langchain-models.git
cd langchain-models
\`\`\`

**2. Create a virtual environment**

\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
\`\`\`

**3. Install dependencies**

\`\`\`bash
pip install -r requirements.txt
\`\`\`

**4. Set up environment variables**

Create a \`.env\` file in the root directory and add your API keys:

\`\`\`env
OPENAI_API_KEY=your_openai_api_key_here
# add other provider keys as needed
\`\`\`

## 💡 How to Use

- **Beginners:** Start with \`1.LLMs\`, \`2.ChatModels\`, and \`4.langchain-prompts\` to understand how to interact with LLMs using LangChain wrappers.
- **Intermediate:** Dive into \`8.Runnables\` to master LangChain Expression Language (LCEL) and the \`|\` pipe syntax.
- **Advanced:** Explore \`11.Vector-store\`, \`12.Retrievers\`, \`13.Youtube_rag\`, and \`16.agents\` to see how retrieval systems and autonomous agents are built.

It's recommended to go through the modules in numerical order (1 → 16), since later modules assume familiarity with concepts from earlier ones — especially Runnables (8) before Agents (16).

## 🙏 Acknowledgments

Credit for the curriculum and instructional flow goes to **Nitish Singh (CampusX)**. Check out the [CampusX YouTube channel](https://www.youtube.com/@campusx-official) for in-depth AI and Data Science tutorials.

## 📄 License

No license specified yet — treat as personal/educational reference material unless a license is added.