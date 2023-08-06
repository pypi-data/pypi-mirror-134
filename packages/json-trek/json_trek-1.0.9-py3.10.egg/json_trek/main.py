import json
from pathlib import Path
from string import ascii_uppercase as ABCs
from random import choice as random_choice, random, randint

# default user profile fields
VALID_FIELDS = [
    "username",
    "email",
    "first_name",
    "last_name",
    "occupation",
    "address",
]

class JSONTrek:
    """
    Star-Trek-themed fake data and lorem ipsum generator for testing and prototyping.

    from JSONTrek import JSONTrek

    trek = JSONTrek()
    """

    def __init__(self):
        filepath = Path(__file__).parent / 'json'
        self.all_words = {}
        # loop through all the json files and add the words from each to the all_words dict
        for filename in filepath.iterdir():
            stem = filename.stem # *.json
            filename = str(filename.resolve())
            with open(filename, 'r') as json_file:
                self.all_words[stem] = json.load(json_file)


        self.names = self.all_words.get('names')
        self.animals = self.all_words.get('animals')
        self.astro_objs = self.all_words.get('astronomical_objects')
        self.klingon_words = self.all_words.get('klingon_words')
        self.names = self.all_words.get('names')
        self.occupations = self.all_words.get('occupations')
        self.species = self.all_words.get('species')
        self.trek_nouns = self.all_words.get('trek_nouns')

    def user_profile(self, fields: list = VALID_FIELDS, valid_fields=VALID_FIELDS) -> dict:
        """Generates random values for each of the given fields in the fields list
        Returns a dictionary of fields and their values"""
        profile = {}

        if not isinstance(fields, list):
            raise TypeError('fields must be a list of strings')
        elif fields == []:
            raise ValueError('fields cannot be blank')

        for field in fields:
            if field not in valid_fields:
                raise ValueError(f'invalid profile field name: {field}')
            if field == "username":
                profile["username"] = self.username()
            elif field == "email":
                profile['email'] = self.email()
            elif field == 'first_name':
                profile['first_name'] = self.get_name('first')
            elif field == 'last_name':
                profile['last_name'] = self.get_name('last')
            elif field == 'occupation':
                profile['occupation'] = self.occupation()
            elif field == 'address':
                profile['address'] = self.address()
        return profile

    def username(self) -> str:
        """Return an adjective and a noun in camelCase, representing a username"""
        species = self.species.get(random_choice(ABCs))

        noun = random_choice(self.trek_nouns).title().split(' ')

        username = ''.join(noun)
        if len(noun) == 1:
            username = random_choice(species).title() + username

        return username + str(int(random() * 100))

    def email(self) -> str:
        """Return a fake email address

        e.g. ElaysianSalmon25@sector92.edu"""
        suffixes = ['com', 'trk', 'edu', 'fed', 'net']
        return f'{self.username()}@sector{randint(1, 100)}.{random_choice(suffixes)}'

    def get_name(self, which_name: str = 'both') -> str:
        """Choose a random letter and then choose a random first or last name
        from the list of names using the random letter as a key"""

        if type(which_name) is not str:
            raise TypeError("'which_name' must be a string")

        if which_name.lower() not in ['first', 'last', 'both']:
            raise ValueError(
                "'which_name' must be either 'first', 'last' or 'both'")

        if which_name == 'both':
            letter_first = random_choice(ABCs)
            letter_last = random_choice(ABCs)
            first = random_choice(self.names['first'][letter_first])
            last = random_choice(self.names['last'][letter_last])
            name = first + ' ' + last
        else:
            letter = random_choice(ABCs)
            name = random_choice(self.names[which_name][letter])

        return name

    def occupation(self) -> str:
        return random_choice(self.occupations[random_choice(ABCs)])

    def address(self) -> str:
        cardinals = ['N.', 'N.E.', 'E.', 'S.E.', 'S.', 'S.W.', 'W.', 'N.W.']
        street_types = ['Ave.', 'St.', 'Ln.', 'Ct.', 'Blvd.', 'Way', 'Hwy.']

        address = {
            'street': '',
            'city': random_choice(self.astro_objs[random_choice(ABCs)]),
            'state': random_choice(ABCs) + random_choice(ABCs),
            'country': random_choice(self.astro_objs[random_choice(ABCs)]),
            'zipcode': f'{randint(12345, 99999)}-{randint(1000, 9999)}'
        }

        address['street'] += str(randint(1, 999)) + ' '

        if random() > .7:
            address['street'] += random_choice(cardinals) + ' '

        address['street'] += random_choice(self.all_words['species']
                                           [random_choice(ABCs)]) + ' '
        address['street'] += random_choice(street_types)

        return address

    def ipsum(self, n: int = 30, lang: str = "human") -> str:
        """Return a string of n words from specified language (lang)"""

        if type(n) is not int:
            raise TypeError("'n' must be an integer")

        if n == 0:
            raise ValueError("'n' cannot be zero")

        elif lang not in ['human', 'klingon'] or type(lang) is not str:
            raise ValueError("'lang' must be either 'human' or 'klingon'")

        if lang == 'klingon':
            words = self.all_words['klingon_words']

        elif lang == "human":
            # the trek_nouns list is significantly shorter
            # than the others, so it's added 12 times. lol
            to_include = ['astronomical_objects', 'species',
                          'trek_nouns', 'trek_nouns', 'trek_nouns',
                          'trek_nouns', 'trek_nouns', 'trek_nouns',
                          'trek_nouns', 'trek_nouns', 'trek_nouns',
                          'trek_nouns', 'trek_nouns', 'trek_nouns', ]

            words = []

            for key in to_include:

                # if the value is a list, add all its items to the words list
                if isinstance(self.all_words.get(key), list):
                    words.extend(self.all_words.get(key))

                # if the value is a dict, add the lists at each letter
                else:
                    # loop through alphabet and use each
                    # as a key to add the list at that key
                    for letter in ABCs:
                        words.extend(self.all_words[key][letter])

            # print(sorted(words))
        text = ""
        for i in range(n):

            # the first word should be titleized
            if i == 0:
                text += random_choice(words)
                text = text.capitalize()
            else:
                # random number between 0 and 1
                chance = random()
                punc_added = False
                # add punctuation based on a random chance
                if chance < 0.1:
                    text += ". "
                    punc_added = True
                elif chance < 0.2:
                    text += "? "
                    punc_added = True
                elif chance < 0.3:
                    text += "! "
                    punc_added = True
                else:
                    text += " "

                word = ''
                while not word.isalpha():
                    word = random_choice(words)

                # if punctuation was added,
                # capitalize the next word
                if punc_added:
                    text += word.capitalize()
                else:
                    text += word.lower()

                # The final character should be !
                if i == n - 1:
                    text += "!"
                # else:
                #     if punc_added:
                #         text += ' '

        return text


if __name__ == '__main__':
    trek = JSONTrek()
    print(trek.ipsum(lang='klingon'))
    print(trek.user_profile())
