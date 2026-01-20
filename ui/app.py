from core.personality import PersonalityProfile
from core.memory import MemoryManager
from core.prompt_builder import PromptBuilder
from core.response_controller import ResponseController
from llm.client import LLMClient
from audio.tts import TextToSpeech

def run_app():
    print("=== AI Living Portrait System ===")

    # Create personality
    personality = PersonalityProfile(
        name="Professor Arjun",
        background="A wise former scientist who mentors young engineers.",
        traits=["calm", "logical", "encouraging"],
        speaking_style="Formal but friendly",
        rules=[
            "Never mention you are an AI",
            "Always behave as a mentor",
            "If unsure, admit and encourage thinking"
        ]
    )

    memory = MemoryManager()
    prompt_builder = PromptBuilder(personality, memory)
    response_controller = ResponseController(memory)
    llm = LLMClient()
    tts = TextToSpeech()

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye.")
            break

        prompt = prompt_builder.build_prompt(user_input)
        assistant_output = llm.generate(prompt)

        print(f"\nPortrait: {assistant_output}")

        # Update memory
        response_controller.analyze_and_update_memory(user_input, assistant_output)

        # Speak (optional)
        tts.speak(assistant_output)
