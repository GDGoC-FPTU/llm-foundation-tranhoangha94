import os
import sys
from template import call_openai

prompt = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."
temperatures = [0.0, 0.5, 1.0, 1.5]

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY is not set. Set it and rerun this script.")
        sys.exit(1)

    for temp in temperatures:
        print(f"Temperature = {temp}")
        try:
            text, latency, usage = call_openai(prompt, temperature=temp)
            print(text)
            print(f"Latency: {latency:.3f}s")
            print(f"Usage: input_tokens={usage['input_tokens']}, output_tokens={usage['output_tokens']}")
        except Exception as exc:
            print(f"Error calling OpenAI for temperature={temp}: {exc}")
        print("-" * 60)
