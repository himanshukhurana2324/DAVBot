import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')
def read_conversation_pairs_from_csv(file_path):
    conversation_pairs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 2:  # Skip rows with invalid format
                continue
            question = row[0]
            answer = row[1]
            conversation_pairs.append((question, answer))
    return conversation_pairs

def preprocess_conversation_pairs(conversation_pairs):
    preprocessed_conversation_pairs = []
    stop_words = set(stopwords.words('english'))
    for question, answer in conversation_pairs:
        question_tokens = word_tokenize(question.lower())
        answer_tokens = word_tokenize(answer.lower())
        question_tokens = [word for word in question_tokens if word not in stop_words]
        answer_tokens = [word for word in answer_tokens if word not in stop_words]
        preprocessed_conversation_pairs.append((question_tokens, answer_tokens))
    return preprocessed_conversation_pairs

def match_question(tokens, conversations):
    for token in tokens:
        if token in conversations:
            # Return only the answer tokens
            answer = conversations[token][0][1]
            answer = [word.replace('\\n', '\n') for word in answer]
            return answer # Assuming the first matching conversation pair
    return None

def output(user_input):
    conversation_pairs = read_conversation_pairs_from_csv('home/chatbotD.csv')
    preprocessed_conversation_pairs = preprocess_conversation_pairs(conversation_pairs)
    
    conversations = {}
    for question_tokens, answer_tokens in preprocessed_conversation_pairs:
        for token in question_tokens:
            if token not in conversations:
                conversations[token] = []
            conversations[token].append((question_tokens, answer_tokens))
    
    tokens = word_tokenize(user_input.lower())
    filtered = [token for token in tokens if token not in stopwords.words('english')]
    answer = match_question(filtered, conversations)
    if answer:
        return( ' '.join(answer))    
    else:
        return "You can visit website or college so you get more clarity"