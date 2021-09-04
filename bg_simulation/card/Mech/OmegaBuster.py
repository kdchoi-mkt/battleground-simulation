from ..Card import Card
from .Microbot import Microbot


class OmegaBuster(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '죽음의 메아리: 1/1 초소형 로봇을 여섯 소환합니다. 소환하지 못한 초소형 로봇 하나당 내 기계들에게 +1/+1을 부여합니다.'
        self.type = 'Mech'
        self.name = '오메가 섬멸로봇'
        self.name_eng = 'Omega Buster'
        self.attack = 6
        self.health = 6
        self.tier = 6
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
        index = mine.get_card_list().index(self)
        card_num = mine.get_live_card_num()

        summoned_mech = 0
        for _ in range(0, 6):
            result = self._summon_card(mine, Microbot(), index)
            if result == True:
                summoned_mech += 1

        for card in mine.get_live_card_list():
            if card.get_type() == 'Mech' or card.get_type() == 'All':
                card.gain_health(6 - summoned_mech)
                card.gain_attack(6 - summoned_mech)

    def set_death_rattle_list(self) -> list:
        return [
            self._summon_microbot
        ]
