## About

Custom Portrait is a personal AI project that explores human–AI interaction through an embodied conversational agent. The system simulates a “living portrait” that can interact with users in natural language while maintaining a consistent personality and long-term memory.

Unlike traditional chatbots, Custom Portrait focuses on personality modeling, context management, and persistent memory to create the illusion of a character that feels alive inside a portrait frame. The project is designed with a modular architecture and serves as a portfolio-grade system demonstrating applied AI engineering and system design skills.

## Project Description

Custom Portrait is a personal AI project that simulates a living portrait capable of interacting with users through natural conversation. The goal of the project is to build an AI character that can maintain a consistent personality, remember important details about the user, and respond coherently across long conversations.

The system allows a developer to define a character using simple attributes such as background, personality traits, speaking style, and a small set of behavioral rules. Each user message is processed through a prompt-building pipeline that combines the character profile with recent conversation history and stored memory before sending it to the language model.

The architecture is intentionally modular. Components such as personality handling, memory management, prompt construction, and model interaction are implemented as separate modules so that individual parts can be modified or replaced without changing the entire system.

A major focus of the project is memory. The system maintains short-term conversational context as well as long-term user-specific memory, allowing the portrait to recall facts such as the user’s name or preferences in later interactions. This helps the system behave more consistently than a stateless chatbot.

The current version supports text-based interaction and optional text-to-speech output. The design is intended to be extended later with speech input and facial animation. This project was built as a portfolio project to demonstrate applied AI system design, prompt engineering, and clean software architecture.
