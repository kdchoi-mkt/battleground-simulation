from ..Card import Card
import random


class Leapfrogger(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "죽음의 메아리: 아군 야수에게 +2/+2와 이 죽음의 메아리를 부여합니다."
        self.type = "Beast"
        self.name = "폴짝개구리 "
        self.name_eng = "Leapfrogger"
        self.attack = 3
        self.health = 3
        self.tier = 2
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = False
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = True
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def _add_death_rattle(self, mine, opponent):
        beast_card = [
            card for card in mine.get_live_card_list() if card.get_type() == "Beast"
        ]
        if len(beast_card) > 0:
            beast = random.choice(beast_card)
            beast.gain_health(2)
            beast.gain_attack(2)
            if len(beast.death_rattle_list) < 500:
                beast.death_rattle_list.append(self._add_death_rattle)

    def set_death_rattle_list(self) -> list:
        return [self._add_death_rattle]
