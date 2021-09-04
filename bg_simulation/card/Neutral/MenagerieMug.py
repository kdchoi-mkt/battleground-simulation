from ..Card import Card
import random


class MenagerieMug(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "전투의 함성: 종족이 서로 다른 무작위 아군 하수인 셋에게 +1/+1을 부여합니다."
        self.type = "Neutral"
        self.name = "박물관 컵"
        self.name_eng = "Menagerie Mug"
        self.attack = 2
        self.health = 2
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
        self.death_rattle = False
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def trigger_before_battle_cry(self, mine, index):
        card_list = [card for card in mine.get_card_list()]
        random.shuffle(card_list)
        type_dict = dict()

        for card in card_list:
            if card.get_type() == "Neutral":
                continue

            type_dict[card.get_type()] = card
            if len(type_dict) == 3:
                break

        for card in type_dict.values():
            card.gain_health(1)
            card.gain_attack(1)
