from dotenv import load_dotenv
import os
from openai import OpenAI
import re
# Load environment variables
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def english_to_sql(prompt: str) -> str:
    system_prompt = "You are a Redshift SQL expert. Convert the user's question into a valid SQL query."

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-4o"
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    raw_sql = response.choices[0].message.content.strip()

    # Remove Markdown formatting if present
    cleaned_sql = re.sub(r"^```(?:sql)?\s*([\s\S]*?)\s*```$", r"\1", raw_sql.strip())

    return cleaned_sql