from ..card import Beast, Demon, Dragon, Elemental, Mech, Murloc, Neutral, Pirate, Quilboar, All

TYPE_LIST = {
    'Quilboar',
    'Beast',
    'Demon',
    'Murloc',
    'Dragon',
    'Elemental',
    'Pirate',
    'Mech',
}

TYPE_MATCHER = {
    'Quilboar': Quilboar,
    'Beast': Beast,
    'Demon': Demon,
    'Murloc': Murloc,
    'Dragon': Dragon,
    'Elemental': Elemental,
    'Pirate': Pirate,
    'Mech': Mech,
    'Neutral': Neutral,
    'All': All
}

TIER_REROLL_MAX = {
    1: 3,
    2: 3,
    3: 4,
    4: 4,
    5: 5,
    6: 6
}

TIER_COIN = {
    1: 5,
    2: 7,
    3: 8,
    4: 9,
    5: 10,
    6: 0
}
