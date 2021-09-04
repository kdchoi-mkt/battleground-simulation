from ..Card import Card
from .Tabbycat import Tabbycat


class Alleycat(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "전투의 함성: 1/1 고양이를 소환합니다."
        self.type = "Beast"
        self.name = "길고양이"
        self.name_eng = "Alleycat"
        self.attack = 1
        self.health = 1
        self.tier = 1
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

    def trigger_after_battle_cry(self, mine):
        self._summon_card(mine, Tabbycat(), mine.get_card_list().index(self))
