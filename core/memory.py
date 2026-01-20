class MemoryManager:
    def __init__(self, max_short_term=10):
        self.short_term = []   # list of (user, assistant)
        self.long_term = {}   # key-value memory
        self.max_short_term = max_short_term

    def add_interaction(self, user_text, assistant_text):
        self.short_term.append((user_text, assistant_text))
        if len(self.short_term) > self.max_short_term:
            self.short_term.pop(0)

    def get_recent_conversation(self):
        text = ""
        for u, a in self.short_term:
            text += f"User: {u}\nAssistant: {a}\n"
        return text.strip()

    def store_fact(self, key, value):
        self.long_term[key] = value

    def recall_facts(self):
        if not self.long_term:
            return "None"
        return "\n".join(f"{k}: {v}" for k, v in self.long_term.items())
