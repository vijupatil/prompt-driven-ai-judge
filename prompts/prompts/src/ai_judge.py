import random
VALID_MOVES = ["rock", "paper", "scissors", "bomb"]
class GameState:
   def __init__(self):
       self.round = 1
       self.user_bomb_used = False
       self.bot_bomb_used = False
state = GameState()
with open("../prompts/system_prompt.txt") as f:
   SYSTEM_PROMPT = f.read()
with open("../prompts/instruction_prompt.txt") as f:
   INSTRUCTION_TEMPLATE = f.read()
def get_bot_move():
   return random.choice(VALID_MOVES)
def build_instruction_prompt(user_text, bot_move):
   return INSTRUCTION_TEMPLATE.format(
       round_number=state.round,
       user_bomb_used=state.user_bomb_used,
       bot_bomb_used=state.bot_bomb_used,
       bot_move=bot_move,
       user_text=user_text
   )
def call_llm(system_prompt, instruction_prompt):
   """
   Replace with Gemini/OpenAI call.
   """
   print("SYSTEM PROMPT:\n", system_prompt)
   print("INSTRUCTION PROMPT:\n", instruction_prompt)
   return "{}"
def process_turn(user_text):
   bot_move = get_bot_move()
   instruction_prompt = build_instruction_prompt(user_text, bot_move)
   response = call_llm(SYSTEM_PROMPT, instruction_prompt)
   state.round += 1
if __name__ == "__main__":
   process_turn("I throw a bomb")
