from ..Card import Card
from .DamagedGolem import DamagedGolem


class HarvestGolem(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '죽음의 메아리: 2/1 손상된 골렘을 소환합니다.'
        self.type = 'Mech'
        self.name = '허수아비골렘'
        self.name_eng = 'Harvest Golem'
        self.attack = 2
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

    def _summon_damaged_golem(self, mine, opponent):
        index = mine.get_card_list().index(self)
        self._summon_card(mine, DamagedGolem(), index)

    def set_death_rattle_list(self) -> list:
        return [
            self._summon_damaged_golem
        ]
