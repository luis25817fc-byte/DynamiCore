from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handler(request):
    try:
        body = request.json()
        message = body.get("message")

        if not message:
            return {
                "statusCode": 400,
                "body": {"error": "message required"}
            }

        response = client.responses.create(
            model="gpt-4o-mini",
            input=message
        )

        return {
            "statusCode": 200,
            "body": {
                "success": True,
                "response": response.output_text
            }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": {"error": str(e)}
  }
