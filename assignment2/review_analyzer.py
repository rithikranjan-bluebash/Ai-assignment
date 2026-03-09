import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

# 1️⃣ Define Pydantic Schema
class ReviewAnalysisResponse(BaseModel):
    summary: str = Field(
        description="A brief summary of the customer review with maximum 3 lines"
    )
    positives: list = Field(
        description="List of positives mentioned by the customer - max 3 points"
    )
    negatives: list = Field(
        description="List of negatives mentioned by the customer - max 3 points"
    )
    sentiment: str = Field(
        description="One word sentiment: positive, negative, or neutral"
    )


# 2️⃣ Create Output Parser
parser = PydanticOutputParser(pydantic_object=ReviewAnalysisResponse)

# 3️⃣ Prompt Template
prompt = PromptTemplate(
    template="""
Analyze the following customer review.

{format_instructions}

Review:
{review}
""",
    input_variables=["review"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# 4️⃣ Initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# 5️⃣ Get User Input
review = input("Enter customer review:\n")

# 6️⃣ Format Prompt
formatted_prompt = prompt.format(review=review)

# 7️⃣ Get LLM Response
response = llm.invoke(formatted_prompt)

# 8️⃣ Parse Structured Output
parsed_output = parser.parse(response.content)

print("\nStructured Review Analysis:\n")
print(parsed_output.model_dump_json(indent=2))