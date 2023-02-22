import json
import pandas as pd
import random
from collections import OrderedDict
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


class PerfumeBrain:

    # This is the brain of our product. It can predict a perfume based on accords or notes provided.
    @staticmethod
    def get_recommendation(input_data):
        # Load the perfumes.json file
        with open('./json/perfumes.json', 'r') as f:
            data = json.load(f)

        # Extract the perfume names and their notes and accords
        perfumes = []
        for perfume in data['perfumes']:
            name = perfume['name']
            try:
                notes = ' '.join(
                    [note['name'].lower() for note in perfume['top_notes'] + perfume['middle_notes'] + perfume['base_notes']])
            except:
                continue
            accords = ' '.join([accord['name'].lower() for accord in perfume['accords']])
            perfumes.append((name, notes + ' ' + accords))

        # Convert the data to a Pandas dataframe
        df = pd.DataFrame(perfumes, columns=['name', 'text'])

        # Preprocess the input
        input_text = ' '.join(input_data['top_notes'] + input_data['middle_notes'] + input_data['base_notes'])
        input_text += ' ' + ' '.join([accord.lower() for accord in input_data['accords']])

        # Train a machine learning model
        vectorizer = CountVectorizer()
        x_train = vectorizer.fit_transform(df['text'])
        y_train = df['name']
        clf = MultinomialNB()
        clf.fit(x_train, y_train)

        # Use the model to predict the fragrance name
        x_input = vectorizer.transform([input_text])
        y_pred = clf.predict(x_input)
        # {
        #     "accords": ["powdery", "vanilla", "floral", "citrus", "woody", "cinnamon"],
        #     "top_notes": ["bergamot", "cinnamon"],
        #     "middle_notes": ["vanilla"],
        #     "base_notes": ["leather"]
        # }

        for perfume in data['perfumes']:
            if perfume['name'] == y_pred[0]:
                return perfume
        else:
            return {}

    @staticmethod
    def get_all_perfumes():
        with open('./json/perfumes.json') as f:
            return json.load(f)

    @staticmethod
    def get_all_notes():
        with open('./json/notes.json') as f:
            return json.load(f)

    @staticmethod
    def get_notes_by_category(note_type):
        with open('./json/notes.json') as f:
            notes = json.load(f)
            for note in notes['perfume_notes']:
                if note['name'] == note_type:
                    return note
            else:
                return {}

    @staticmethod
    def get_notes_categories():
        with open('./json/notes.json') as f:
            notes = json.load(f)

            categories = []
            for category in notes['perfume_notes']:
                categories.append(category['name'])

            return categories

    @staticmethod
    def get_random_perfume():
        # Load the perfumes.json file
        with open('./json/perfumes.json', 'r') as f:
            data = json.load(f)
        return data['perfumes'][random.randint(0, len(data['perfumes']))]