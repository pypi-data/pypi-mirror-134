import unittest
from .main import JSONTrek
from string import ascii_uppercase as ABCs


class TrekTest(unittest.TestCase):
    def setUp(self):
        self.trek = JSONTrek()

    def test_user_profile(self):
        self.assertRaises(TypeError, self.trek.user_profile, '')
        self.assertRaises(TypeError, self.trek.user_profile, 123)
        self.assertRaises(TypeError, self.trek.user_profile, {})
        self.assertRaises(ValueError, self.trek.user_profile, [])
        self.assertRaises(TypeError, self.trek.user_profile, None)
        self.assertRaises(TypeError, self.trek.user_profile, (1,))

        self.assertRaises(ValueError, self.trek.user_profile,
                          ['username', 'email', 'test123'])

        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "occupation",
            "address",
        ]
        profile = self.trek.user_profile(fields)
        self.assertRegex(profile['username'], r'\w+\d+')
        self.assertRegex(
            profile['email'], r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        self.assertRegex(profile['first_name'], r'\w+')
        self.assertRegex(profile['last_name'], r'\w+')
        self.assertRegex(profile['occupation'], r'\w+')

        self.assertEqual(fields, list(profile.keys()))

    def test_address(self):
        for i in range(10000):
            address = self.trek.address()
            self.assertRegex(address['street'],
                             r'\d+[ ](?:[A-Za-z0-9.-]+[ ][\S]+)[\w. ]*')

            self.assertRegex(address['city'], r'\w')
            self.assertRegex(address['city'], r"[A-Za-z-' ]+")
            self.assertRegex(address['state'], r"\w{2}")
            self.assertRegex(address['country'], r"[A-Za-z-' ]+")
            self.assertRegex(address['zipcode'], r"\w{5}-\w{4}")

        self.assertEqual(['street', 'city', 'state', 'country',
                         'zipcode'], list(address.keys()))

    def test_ipsum(self):
        #
        self.assertRaises(ValueError, self.trek.ipsum, lang=1)
        self.assertRaises(ValueError, self.trek.ipsum, lang=None)
        self.assertRaises(ValueError, self.trek.ipsum, lang=[])
        self.assertRaises(ValueError, self.trek.ipsum, lang={})
        self.assertRaises(ValueError, self.trek.ipsum, lang='abc')
        self.assertRaises(ValueError, self.trek.ipsum, n=0)
        self.assertRaises(TypeError, self.trek.ipsum, n=None)
        self.assertRaises(TypeError, self.trek.ipsum, n={})
        self.assertRaises(TypeError, self.trek.ipsum, n=[])

        # check human ipsum
        to_include = ['astronomical_objects', 'species',
                      'trek_nouns', 'trek_nouns', 'trek_nouns', 'trek_nouns']

        all_human_words = []

        # gather all words into the list
        for key in to_include:

            # if the value is a list, add all its items to the words list
            if isinstance(self.trek.all_words.get(key), list):
                all_human_words.extend(self.trek.all_words.get(key))

            # if the value is a dict, add the lists at each letter
            else:
                # loop through alphabet and use each
                # as a key to add the list at that key
                for letter in ABCs:
                    all_human_words.extend(self.trek.all_words[key][letter])

        # join all the words into a giant string
        all_human_words = ' '.join(sorted(all_human_words))

        human_ipsum = self.trek.ipsum()
        for punc in ['!', '?', '.']:
            human_ipsum = human_ipsum.replace(punc, '')

        # check if all the words in the ipsum are in the klingon word bank
        for word in human_ipsum.split(' '):
            self.assertIn(word.lower(), all_human_words.lower())

        # check if all the words in the ipsum are in the klingon word bank
        all_klingon_words = ' '.join(sorted(self.trek.klingon_words))

        klingon_ipsum = self.trek.ipsum(lang='klingon')
        for punc in ['!', '?', '.']:
            klingon_ipsum = klingon_ipsum.replace(punc, '')

        for word in klingon_ipsum.split(' '):
            self.assertIn(word.lower(), all_klingon_words.lower())

    def test_username(self):
        for i in range(10000):
            username = self.trek.username()
            self.assertRegex(username, r"[A-Z]+[a-z]+[\d]*")

    def test_get_name(self):
        self.assertRaises(TypeError, self.trek.get_name, 123)

        self.assertRaises(ValueError, self.trek.get_name, 'abc')