# Prompt-Driven AI Judge (Rock Paper Scissors Plus)
## Objective
This project implements a prompt-driven AI Judge for a Rock–Paper–Scissors Plus game.
The focus is on prompt design, instruction clarity, edge-case handling, and explainability.
## Game Rules
- Valid moves: rock, paper, scissors, bomb
- Bomb can be used only once per player
- Bomb beats everything
- Bomb vs bomb results in a draw
- Unclear or invalid moves waste the turn
## Architecture
- Intent Understanding: handled by LLM
- Game Logic: enforced through prompt rules
- Response Generation: structured JSON
- State: minimal Python (round, bomb usage)
## Folder Structure
- prompts/ → system and instruction prompts
- src/ → minimal glue code
- examples/ → sample outputs
## Failure Cases Handled
- Ambiguous input → UNCLEAR
- Invalid moves → INVALID
- Repeated bomb usage → INVALID
- Synonyms mapped only if intent is clear
## Future Improvements
- Add confidence score
- Multi-round summary
- Adversarial prompt testing
- Clarifying question support
## How to Run
```bash
python src/ai_judge.py
