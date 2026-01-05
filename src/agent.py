import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Correct env variable name
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


class WaterIntakeAgent:
    DAILY_GOAL_ML = 2500  # standard daily intake

    def __init__(self):
        self.history = []

    def _hydration_status(self, intake: int) -> str:
        if intake < 1000:
            return "Low hydration"
        elif intake < 2000:
            return "Moderate hydration"
        else:
            return "Well hydrated"

    def analyze_intake(self, intake: int) -> str:
        status = self._hydration_status(intake)
        remaining = max(self.DAILY_GOAL_ML - intake, 0)

        prompt = f"""
        You are a hydration assistant.

        User water intake today: {intake} ml
        Hydration status: {status}
        Remaining water to reach daily goal: {remaining} ml

        Give a short, friendly recommendation in 2–3 sentences.
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Groq model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )

        feedback = response.choices[0].message.content.strip()

        self.history.append({
            "intake": intake,
            "status": status,
            "remaining": remaining,
            "feedback": feedback
        })

        return (
            f"Hydration Status: {status}\n"
            f"Consumed: {intake} ml\n"
            f"Remaining to reach daily goal: {remaining} ml\n\n"
            f"AI Recommendation:\n{feedback}"
        )


if __name__ == "__main__":
    agent = WaterIntakeAgent()
    intake = 1500
    result = agent.analyze_intake(intake)
    print(result)
