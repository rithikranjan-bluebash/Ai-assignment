import os
from groq import Groq
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def review_resume(resume, role):

    user_prompt = f"""
Resume:
{resume}

Job Role:
{role}

Evaluate the candidate.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    resume = """
    Name: John Doe
    Skills: Python, SQL, Machine Learning, Data Analysis
    Experience: Data Analyst at ABC Company for 2 years
    Education: B.Tech in Computer Science
    """

    role = "Data Scientist"

    result = review_resume(resume, role)

    print("\nAI Resume Review:\n")
    print(result)