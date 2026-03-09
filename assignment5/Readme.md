# AI HR Assistant using RAG

## Overview

This project implements an **AI-powered HR Assistant** that answers employee questions by retrieving information from company HR policy documents.

The system uses a **Retrieval-Augmented Generation (RAG)** pipeline to search through HR policy documents and generate accurate responses using a Large Language Model (LLM).

Instead of manually reading long policy documents, employees can simply ask questions and receive answers instantly.

---

## Features

* Reads multiple HR policy PDF documents
* Splits documents into smaller chunks
* Generates embeddings for each chunk
* Stores embeddings in a vector database
* Retrieves relevant policy information based on user queries
* Uses an LLM to generate human-readable responses

---

## Dataset

The project uses a dataset containing HR policy documents.

```
hr_policies_dataset/

Work From Home Policy.pdf
Casual Leave Policy.pdf
Sick Leave Policy.pdf
Office Working Hours Policy.pdf
Code of Conduct Policy.pdf
```

These documents contain policies related to:

* Work from home rules
* Casual leave
* Sick leave
* Office working hours
* Employee code of conduct

---

## Technology Stack

* Python
* LangChain
* FAISS (Vector Database)
* Sentence Transformers (Embeddings)
* Groq LLM API
* PyPDF for reading PDF documents

---

## RAG Architecture

The system follows the **Retrieval-Augmented Generation pipeline**:

```
HR Policy PDFs
      ↓
Document Loader
      ↓
Text Splitter
      ↓
Embeddings Generator
      ↓
Vector Database (FAISS)
      ↓
Retriever
      ↓
Large Language Model
      ↓
Generated Answer
```

---

## Installation

Clone the repository:

```
git clone <your-repository-url>
cd hr-assistant-rag
```

Create a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install langchain langchain-community langchain-groq
pip install sentence-transformers faiss-cpu pypdf python-dotenv
```

---

## Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

Run the HR assistant from the terminal:

```
python hr_assistant.py
```

You can then ask questions such as:

```
How many casual leaves are allowed per year?
How many sick leaves are allowed each year?
What are the standard office working hours?
Who must follow the code of conduct?
```

---

## Example Output

```
Ask HR Assistant: How many casual leaves are allowed per year?

HR Assistant:
Employees are entitled to 12 casual leaves annually.
```

---

## Sample Questions

### Work From Home Policy

* How many days per week can employees work from home?
* Do employees need approval for each work-from-home day?

### Casual Leave Policy

* How many casual leaves are allowed per year?
* Can casual leave be carried forward?

### Sick Leave Policy

* How many sick leaves are allowed each year?
* When is a medical certificate required?

### Office Working Hours

* What are the standard office working hours?
* Are employees required to be available during specific hours?

### Code of Conduct

* Who must follow the Code of Conduct?
* What should employees do if they witness misconduct?

---

## Deliverables

This project includes:

* Source code for the RAG application
* Instructions to run the application
* Architecture explanation
* Example outputs demonstrating correct responses

---

## Learning Objectives

This assignment demonstrates:

* Retrieval-Augmented Generation (RAG)
* Document processing with LangChain
* Vector embeddings and similarity search
* Building AI assistants for real-world document querying

---

## Future Improvements

Possible enhancements include:

* Adding a Streamlit web interface
* Saving the FAISS vector database for faster loading
* Displaying source documents used for answers
* Improving retrieval with advanced RAG techniques

---

## Author

Rithik Ranjan
