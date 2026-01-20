## About

Custom Portrait is a personal AI project that explores human–AI interaction through an embodied conversational agent. The system simulates a “living portrait” that can interact with users in natural language while maintaining a consistent personality and long-term memory.

Unlike traditional chatbots, Custom Portrait focuses on personality modeling, context management, and persistent memory to create the illusion of a character that feels alive inside a portrait frame. The project is designed with a modular architecture and serves as a portfolio-grade system demonstrating applied AI engineering and system design skills.

## Project Description

Custom Portrait is an interactive AI system that enables real-time, personality-driven conversational interaction with a virtual portrait. The system allows developers to define a custom character profile consisting of background, personality traits, speaking style, and behavioral rules. All user interactions are processed through a structured prompt-building pipeline that injects personality constraints, short-term conversational context, and long-term memory into each model call.

The architecture is designed in a modular manner, separating the personality engine, memory manager, prompt builder, response controller, and LLM interface into independent components. This design allows easy replacement of language models, memory strategies, and user interfaces without affecting the core logic.

A key focus of Custom Portrait is persistent memory. The system maintains both short-term conversational memory and long-term user-specific memory, enabling the portrait to recall important facts such as user identity and preferences across interactions. This significantly improves coherence and realism compared to stateless chatbots.

The current implementation supports text-based interaction and text-to-speech output, with a clear extension path toward multimodal interaction including speech input and facial animation. The project emphasizes clean system design, reproducibility, and extensibility, making it suitable as a portfolio project for AI and software engineering roles.
