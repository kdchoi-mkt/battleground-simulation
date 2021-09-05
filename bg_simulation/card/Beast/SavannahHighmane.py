from .Hyena import Hyena
from ..Card import Card


class SavannahHighmane(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "죽음의 메아리: 2/2 하이에나를 2마리 소환합니다."
        self.type = "Beast"
        self.name = "사바나 사자"
        self.name_eng = "Savannah Highmane"
        self.attack = 6
        self.health = 5
        self.tier = 4
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

    def _summon_hyena(self, mine, opponent):
        self._summon_card(mine, Hyena(), mine.get_card_list().index(self))

    def set_death_rattle_list(self) -> list:
        return [self._summon_hyena]
