import os
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Load environment variables
load_dotenv()

# Set embedding model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Setup Groq LLM
Settings.llm = Groq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# Load documents
documents = SimpleDirectoryReader("policies").load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Query engine
query_engine = index.as_query_engine()

print("HR Assistant Ready! (type 'exit' to quit)\n")

try:
    while True:
        question = input("Ask HR: ").strip()

        if question.lower() in ["exit", "quit", "bye"]:
            print("Goodbye.")
            break

        response = query_engine.query(question)
        print("Answer:", response, "\n")

except KeyboardInterrupt:
    print("\nGoodbye.")