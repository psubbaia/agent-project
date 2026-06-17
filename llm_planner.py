import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

PLAN_SCHEMA = {
    "type": "object",
    "properties": {
        "tasks": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 3,
            "maxItems": 6
        }
    },
    "required": ["tasks"],
    "additionalProperties": False
}


def create_plan_with_llm(goal: str) -> list[str]:
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.5"),
        input=[
            {
                "role": "system",
                "content": (
                    "You are a planning assistant. "
                    "Break the user's goal into 3 to 5 actionable tasks. "
                    "Return only structured JSON."
                )
            },
            {
                "role": "user",
                "content": f"Goal: {goal}"
            }
        ],
        text={
            "format": {
                "type": "json_schema",
                "name": "task_plan",
                "schema": PLAN_SCHEMA,
                "strict": True
            }
        }
    )

    data = json.loads(response.output_text)
    return data["tasks"]