import os

# Luego puedes cambiar esto por OpenAI real o modelo local
USE_MOCK = True


def run_ai(prompt: str, user_context: dict = None):

    if USE_MOCK:
        return {
            "response": f"[DynamiCore AI MOCK] procesé: {prompt}",
            "model": "mock-v1"
        }

    # 🔥 AQUÍ después conectas OpenAI real
    # from openai import OpenAI
    # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    #
    # completion = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "system", "content": "You are DynamiCore AI Engine"},
    #         {"role": "user", "content": prompt}
    #     ]
    # )
    #
    # return {"response": completion.choices[0].message.content}
