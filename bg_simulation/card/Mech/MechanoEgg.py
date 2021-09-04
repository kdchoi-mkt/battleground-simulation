from ..Card import Card
from .Robosaur import Robosaur


class MechanoEgg(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '죽음의 메아리: 8/8 공룡로봇을 소환합니다.'
        self.type = 'Mech'
        self.name = '기계 알'
        self.name_eng = 'Mechano-Egg'
        self.attack = 0
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

    def _summon_robosaur(self, mine, opponent):
        index = mine.get_card_list().index(self)
        self._summon_card(mine, Robosaur(), index)

    def set_death_rattle_list(self) -> list:
        return [
            self._summon_robosaur
        ]
