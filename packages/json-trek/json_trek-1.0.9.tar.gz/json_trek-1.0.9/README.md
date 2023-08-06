# JSON Trek
## Star-Trek-flavored JSON data

Generate fake JSON user data and lorem ipsum with a Star Trek theme.

[![CI](https://github.com/perennialAutodidact/json_trek/actions/workflows/ci.yml/badge.svg)](https://github.com/perennialAutodidact/json_trek/actions/workflows/ci.yml)
## Fake User Data

JSON Trek can generate user information for the following categories:

- Username
- Email address
- First name
- Last name
- Address
  - Street
  - City
  - State
  - Country
  - Zip code
- Occupation

## Install

`$ pip install json-trek`

## Usage

```python
>>> from json_trek import JSONTrek

>>> trek = JSONTrek()
```

## Methods
## user_profile(fields: list)

If called without a list of fields, `user_profile` will generate values for all fields.

### Username fields
- username
- email
- first_name
- last_name
- occupation
- address

```python
>>> trek.user_profile() # generate a user profile with all fields

# the output here is formatted for readability
{
  "username": "CyberneticImplant8",
  "email": "SporeDrive48@sector68.fed",
  "first_name": "Mirab",
  "last_name": "Zshaar",
  "occupation": "Xenoanthropologist",
  "address": {
    "street": "665 N. Bomar Hwy.",
    "city": "Nyria III",
    "state": "RT",
    "country": "Tessen III",
    "zipcode": "43974-3953"
  }
}
```


```python
>>> trek.user_profile([ 'username', 'email' ]) # or, pass a list of the desired user profile fields

# the output here is formatted for readability
{
  "username": "FluxIsolator81",
  "email": "IsodyneRelay17@sector21.trk"
}

```

## username()
Generate a username consisting of two words and a number.

```python
>>> trek.username()
"OrbitalTether35"
```

## email()
Generate an email address. This is the same as the output from username ending with @sector0-100 and ending with .com, .trk, .edu, .fed, or .net

```python
>>> trek.email()
"IconianCombadge48@sector63.net"
```
## get_name(first_or_last: str = 'both')
Generate a first and last name together or each individually.

```python
>>> trek.name()
"K'Kath Lor"

>>> trek.name('first')
"Ilia"

>>> trek.name('last')
"Xerius"
```
## occupation()
Generate an occupation.

```python
>>> trek.occupation('first')
"Chief Medical Officer"
```
## address()
Generate an address with values for street, city, state, country and zipcode.

```python
>>> trek.address()

# the output here is formatted for readability
{
  "street": "75 Aldean St.",
  "city": "Risa",
  "state": "CR",
  "country": "Ganalda IV",
  "zipcode": "73691-9986"
}
```

## ipsum(n: int = 30, lang: str = 'human')

Args:
- `n` - minimum number of words to generate (some words come as pairs so the final string might be more than `n` words.)
- `lang` - language in which to generate lorem ipsum text
  - `'human'` (default)
  - `'klingon'`

```python
>>> trek.ipsum() # generate 30 human words
"Matter synthesizer? Holosuite hovercar runabout kantare? Kelva ithenite nuubari sensor mundahla taresia narva verdanis combadge ardana lothra leyron argosian. Burke? Xindus varro? Eridanus. Xelatian lyssarian hovercar? Cepheus nakan kurlan valakis shuttlecraft!"

>>> trek.ipsum(10, 'klingon') # generate 10 klingon words
"Cha. Jatlh jajvam duj nenchoh pov jaghmeyjaj? Chack toj posmoh!"
```

Thanks to [STAPI](http://stapi.co/) for providing a lot of the data used in this project.
