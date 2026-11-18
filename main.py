from chat import chat

def strip_thinking(text):
    if "</think>" in text:
        text = text[text.find("</think>") + len("</think>"):]
    return text.strip()

def talk_to_villager(question):
    prompt = "You are a village farmer. Respond with one single variation of 'Good day.'\nQuestion: "
    return strip_thinking(chat(prompt + question))

def talk_to_guard(question):
    prompt = "You are a cautious town guard. Keep answers short and mention safety.\nQuestion: "    
    return strip_thinking(chat(prompt + question))

def talk_to_wizard(question):
    prompt = "You are a wise and old wizard. Be very open to help people and offer wizardly advice while being very vague and mystic.\nQuestion: "    
    return strip_thinking(chat(prompt + question))

def talk_to_merchant(question):
    prompt = "You are a greedy and exploitative merchant. You are to be sneaky and try to swindle people, never give anything for free.\nQuestion: "    
    return strip_thinking(chat(prompt + question))

def classify_character(user_text):
    classifier_prompt = """You are an intent classifier for routing player dialog to an NPC.
Pick exactly one character name from this list: villager, guard, wizard, merchant.
Return ONLY the single word. If unsure, return villager.

Player input: """

    result = strip_thinking(chat(classifier_prompt + user_text))


    # Students use string methods to clean up the LLM's raw output
    clean_result = result.strip().lower()

    # Determine the intent using basic membership (in) or equality
    if "villager" in clean_result:
        return "villager"
    elif "guard" in clean_result:
        return "guard"
    elif "wizard" in clean_result:
        return "wizard"
    elif "merchant" in clean_result:
        return "merchant"
    else:
        return "villager"


def main():
    print("Welcome to the AI Village! Type 'exit' or 'quit' to leave.")

    while True:
        user_input = input("> ").strip()

        # Standard loop breakout
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # 1. Get the target character string from the classifier
        target = classify_character(user_input)

        # 2. Routing logic implemented directly in main using if/elif
        if target == "guard":
            response = talk_to_guard(user_input)
        elif target == "wizard":
            response = talk_to_wizard(user_input)
        elif target == "merchant":
            response = talk_to_merchant(user_input)
        else:
            response = talk_to_villager(user_input)

        # 3. Output the result
        print("["+target.upper()+"]: " + response + "\n")



if __name__ == "__main__":
    main()