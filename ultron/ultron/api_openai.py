import requests
import random
import html

def get_category_id(topic):
    """Fetch available categories and find the matching category ID."""
    url = "https://opentdb.com/api_category.php"
    response = requests.get(url)

    if response.status_code == 200:
        categories = response.json().get("trivia_categories", [])
        for category in categories:
            if topic.lower() in category["name"].lower():
                return category["id"]  # Return category ID if found
        print("Topic not found. Showing general questions.")
        return None
    else:
        print("Error fetching categories.")
        return None

def get_trivia_questions(topic, amount=10, difficulty="easy"):
    """Fetch trivia questions for a given topic."""
    category_id = get_category_id(topic)
    
    url = f"https://opentdb.com/api.php?amount=10&category=17&difficulty=easy&type=multiple"
    if category_id:
        url += f"&category={category_id}"  # Add category filter if available
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        questions = data.get("results", [])
        
        for idx, q in enumerate(questions, 1):
            question = html.unescape(q["question"])
            correct_answer = html.unescape(q["correct_answer"])
            incorrect_answers = [html.unescape(ans) for ans in q["incorrect_answers"]]
            
            options = incorrect_answers + [correct_answer]
            random.shuffle(options)

            print(f"\nQuestion {idx}: {question}")
            for i, option in enumerate(options):
                print(f"{chr(65+i)}. {option}")
            
            print(f"Correct Answer: {correct_answer}\n")  # Show correct answer
    else:
        print("Error fetching questions.")

# Example usage
topic = input("Enter a topic: ")
get_trivia_questions(topic)
