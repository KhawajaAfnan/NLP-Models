
# from tokenizers import Tokenizer, models,  pre_tokenizers

# import pandas as pd

# tokenizer = Tokenizer(models.BPE())

# tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()


# data = pd.read_csv('nlpass1/Sentiment Dataset Urdu.csv')

# texts = data['Text'].tolist()
# tokenizer.train_from_iterator(texts)

# tokenizer.save('urdu_bpe_tokenizer.json')

# tokenizer = Tokenizer.from_file('urdu_bpe_tokenizer.json')

# encoded = tokenizer.encode("لڑکا کتاب پڑھتا ہے")
# print(encoded.tokens)  



import pandas as pd

data = pd.read_csv('nlpass1/Sentiment Dataset Urdu.csv', encoding='utf-8')

texts = data['Text'].tolist()

def create_word_dict(texts):
    word_set = set()
    for text in texts:
        words = text.split() 
        word_set.update(words)
    return word_set

urdu_word_dict = create_word_dict(texts)

def max_match_segmentation(sentence, word_dict):
    words = []
    while sentence:
        for i in range(len(sentence), 0, -1):
            word = sentence[:i]
            if word in word_dict:
                words.append(word)
                sentence = sentence[i:]  
                break
        else:
            words.append(sentence[0])
            sentence = sentence[1:]
    return words

# Example sentence from the dataset
sample_sentence = "یہ ایک مثال ہے"

# Perform MaxMatch segmentation
segmented_sentence = max_match_segmentation(sample_sentence, urdu_word_dict)

# Display the segmented sentence
print(f"Original Sentence: {sample_sentence}")
print(f"Segmented Sentence: {' | '.join(segmented_sentence)}")
