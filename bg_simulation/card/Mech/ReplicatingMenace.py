from ..Card import Card
from .Microbot import Microbot


class ReplicatingMenace(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "합체, 죽음의 메아리: 1/1 초소형 로봇을 셋 소환합니다."
        self.type = "Mech"
        self.name = "증식하는 위협"
        self.name_eng = "Replicating Menace"
        self.attack = 3
        self.health = 1
        self.tier = 3
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

    def _summon_microbot(self, mine, opponent):
        self._summon_card(mine, Microbot(), mine.get_card_list().index(self))
        self._summon_card(mine, Microbot(), mine.get_card_list().index(self))
        self._summon_card(mine, Microbot(), mine.get_card_list().index(self))

    def set_death_rattle_list(self) -> list:
        return [self._summon_microbot]
