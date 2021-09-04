class MinionGenerator(object):
    def __init__(self, card_info):
        self._generate_card_data(
            card_info
        )
        self.card_data = self._generate_card_py()

    def _generate_card_data(self, card_info):
        self.korean_name = card_info['KoreanName']
        self.name = card_info['Name']\
            .replace('\'', '')\
            .split('[')[0]
        self.class_name = self.name\
            .replace(' ', '')\
            .replace('-', '')\
            .replace('\'', '')\
            .replace(',', '')\
            .replace('’', '')\
            .replace('the', 'The')\
            .replace(':', '')\
            .split('[')[0]
        self.tier = card_info['Tier']
        self.type = card_info['Type']
        self.text = card_info['Text']
        self.attack = card_info['Attack']
        self.health = card_info['Health']
        self.taunt = card_info['Taunt']
        self.divine_shield = card_info['DivineShield']
        self.reborn = card_info['Reborn']
        self.windfury = card_info['Windfury']
        self.frenzy = card_info['Frenzy']
        self.poison = card_info['Poison']
        self.avenge = card_info['Avenge']
        self.avenge_count = card_info['AvengeCount']
        self.death_rattle = card_info['DeathRattle']
        self.battle_cry = card_info['BattleCry']
        self.available_in_shop = card_info['AvailableInShop']

    def _generate_card_py(self):
        return f"""from ..Card import Card

class {self.class_name}(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '{self.text}'
        self.type = '{self.type}'
        self.name = '{self.korean_name}'
        self.name_eng = '{self.name}'
        self.attack = {self.attack}
        self.health = {self.health}
        self.tier = {self.tier}
        self.live = True
        self.taunt = {self.taunt}
        self.divine_shield = {self.divine_shield}
        self.windfury = {self.windfury}
        self.reborn = {self.reborn}
        self.frenzy = {self.frenzy}
        self.poison = {self.poison}
        self.avenge = {self.avenge}
        self.avenge_count = {self.avenge_count}
        self.death_rattle = {self.death_rattle}
        self.battle_cry = {self.battle_cry}
        self.available_in_shop = {self.available_in_shop}
        self.death_rattle_list = self.set_death_rattle_list()
        """

    def save_card(self):
        type_upper = self.type[0].upper() + self.type[1:]

        with open(f'./bg_simulation/card/{type_upper}/{self.class_name}.py', 'w') as f:
            f.write(self.card_data)
        with open(f'./bg_simulation/card/{type_upper}/__init__.py', 'a') as f:
            f.write(f"from .{self.class_name} import {self.class_name}\n")
