class PromptBuilder:
    def __init__(self, personality_profile, memory_manager):
        self.personality = personality_profile
        self.memory = memory_manager

    def build_prompt(self, user_input):
        system_prompt = self.personality.build_system_prompt()
        memory_facts = self.memory.recall_facts()
        recent_chat = self.memory.get_recent_conversation()

        full_prompt = f"""
SYSTEM:
{system_prompt}

LONG-TERM MEMORY:
{memory_facts}

RECENT CONVERSATION:
{recent_chat}

USER:
{user_input}

ASSISTANT:
"""
        return full_prompt.strip()
