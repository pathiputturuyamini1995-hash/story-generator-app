import os
from openai import OpenAI
from user_input import get_user_inputs

client = OpenAI()  # reads OPENAI_API_KEY from your environment

def generate_story(character_name: str, setting: str, theme: str) -> str:
    system_msg = (
        "You are a helpful storyteller. Write vivid, friendly stories. "
        "Keep it 250–400 words, clear paragraphs, and a sweet ending."
    )
    user_prompt = (
        f"Write a short story.\n"
        f"Main character: {character_name}\n"
        f"Setting: {setting}\n"
        f"Theme: {theme}\n"
        f"Audience: general.\n"
    )

    # Uses the latest Responses API
    resp = client.responses.create(
        model="gpt-4o-mini",
        input=[{"role": "system", "content": system_msg},
               {"role": "user", "content": user_prompt}]
    )
    return resp.output_text

if __name__ == "__main__":
    name, setting, theme = get_user_inputs()
    story = generate_story(name, setting, theme)
    print("\nGenerated Story:\n")
    print(story)