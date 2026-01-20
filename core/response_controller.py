class ResponseController:
    def __init__(self, memory_manager):
        self.memory = memory_manager

    def analyze_and_update_memory(self, user_input, assistant_output):
        text = user_input.lower()

        # Simple rule-based memory extraction
        if "my name is" in text:
            name = text.split("my name is")[-1].strip()
            self.memory.store_fact("user_name", name)

        if "i am a" in text:
            role = text.split("i am a")[-1].strip()
            self.memory.store_fact("user_role", role)

        # Add to short-term memory
        self.memory.add_interaction(user_input, assistant_output)
