def get_knowledge():
    with open("knowledge.txt", "r") as f:
        return f.read()

def retrieve_answer(query):
    data = get_knowledge()
    return data