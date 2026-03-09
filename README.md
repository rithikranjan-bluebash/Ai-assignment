Setup Instructions
1. Clone the repository
git clone <repository-url>
cd ai-assignments
2. Create a virtual environment
python -m venv venv
source venv/bin/activate
3. Install dependencies
pip install langchain langchain-community langchain-groq
pip install sentence-transformers faiss-cpu pypdf python-dotenv
Environment Variables

Create a .env file:

GROQ_API_KEY=your_api_key_here
Running the Applications

Each assignment can be executed individually from the terminal.

Example:

python assignment4/resume_reviewer.py

or

python assignment5/hr_assistant.py
