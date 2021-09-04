from ..Card import Card
from .Imp import Imp


class IckyImp(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "죽음의 메아리: 1/1 임프를 둘 소환합니다."
        self.type = "Demon"
        self.name = "성가신 임프"
        self.name_eng = "Icky Imp "
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
        self.death_rattle = True
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def _summon_two_imp(self, mine, opponent):
        self._summon_card(mine, Imp(), mine.get_card_list().index(self))
        self._summon_card(mine, Imp(), mine.get_card_list().index(self))

    def set_death_rattle_list(self) -> list:
        return [self._summon_two_imp]
