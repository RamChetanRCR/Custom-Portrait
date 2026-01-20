class PersonalityProfile:
    def __init__(self, name, background, traits, rules, speaking_style):
        self.name = name
        self.background = background
        self.traits = traits
        self.rules = rules
        self.speaking_style = speaking_style

    def build_system_prompt(self):
        traits_text = ", ".join(self.traits)
        rules_text = "\n".join(f"- {r}" for r in self.rules)

        prompt = f"""
You are a living portrait named {self.name}.

Background:
{self.background}

Personality Traits:
{traits_text}

Speaking Style:
{self.speaking_style}

Rules:
{rules_text}

Always stay in character. Never mention you are an AI.
"""
        return prompt.strip()
