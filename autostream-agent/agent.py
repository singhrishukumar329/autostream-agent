def run_agent(user_input):
    user_input = user_input.lower()

    if "price" in user_input:
        return "Our pricing starts at ₹999"
    
    elif "buy" in user_input:
        return "Please share your name and contact details"
    
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    
    else:
        return "Sorry, I didn’t understand that. Please ask about pricing or buying."