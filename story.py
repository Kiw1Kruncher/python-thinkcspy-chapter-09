from chat import chat

def strip_thinking(text):
    if "</think>" in text:
        text = text[text.find("</think>") + len("</think>"):]
    return text.strip()

def talk_to_reginald(question):
    prompt = "You are Reginald the neighbor. You are very nosy and think like you know everything. You are also quite rude.\nQuestion: "
    return strip_thinking(chat(prompt + question))

def talk_to_landlord(question):
    prompt = "You are the landlord you talk in very little words. You suggest the cheapist and worse repairs for anything (they dont really fix anything). You are very dissmissive and always busy. Be rude but not totally outright you still want them to live there. Do NOT respond like:Let me know if you need help with anything else, or anything similar.\nQuestion: "    
    return strip_thinking(chat(prompt + question))

def talk_to_phone(question):
    prompt = "You are a phone answering system that is REALLY poory made and is SUPER unhelpful. Bring up that you are thankful for the person staying on hold for an extended period of time, for example 1hr. be very vague and UNHELPFUL.\nQuestion: "    
    return strip_thinking(chat(prompt + question))

def talk_to_electrician(question):
    prompt = "You ARE a electrician. You are REALLY bad at your job and know nothing but try to play it off. You play it off really poorly though. You are VERY nervous. You try to help. DO NOT bring attention to your incompetence.\nQuestion: "    
    return strip_thinking(chat(prompt + question))

def classify_character(user_text):
    classifier_prompt = """You are an intent classifier for routing player dialog to an NPC.
Pick exactly one character name from this list: reginald, landlord, phone, electrician.
The landlord is for any household repairs such as painting, heating, flooring, walls, etc.
The phone is for anything tech related etc.
The electrician is for anything electrical etc.
Reginald is for random things and/or outliers.
Return ONLY the single word. If unsure, return reginald.

Player input: """

    result = strip_thinking(chat(classifier_prompt + user_text))


    # Students use string methods to clean up the LLM's raw output
    clean_result = result.strip().lower()

    # Determine the intent using basic membership (in) or equality
    if "reginald" in clean_result:
        return "reginald"
    elif "landlord" in clean_result:
        return "landlord"
    elif "phone" in clean_result:
        return "phone"
    elif "electrician" in clean_result:
        return "electrician"
    else:
        return "reginald"


def main():
    print("Welcome to random issue simulator! Type 'exit' or 'quit' to leave.")

    while True:
        user_input = input("> ").strip()

        # Standard loop breakout
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # 1. Get the target character string from the classifier
        target = classify_character(user_input)

        # 2. Routing logic implemented directly in main using if/elif
        if target == "landlord":
            response = talk_to_landlord(user_input)
        elif target == "phone":
            response = talk_to_phone(user_input)
        elif target == "electrician":
            response = talk_to_electrician(user_input)
        else:
            response = talk_to_reginald(user_input)

        # 3. Output the result
        print("["+target.upper()+"]: " + response + "\n")



if __name__ == "__main__":
    main()


'''
Example Prompts:

Reginald: My coffee is cold

Landlord: There is a hole in my wall

Phone: My printer is broken

Electrician: My electricity keeps turning off

'''