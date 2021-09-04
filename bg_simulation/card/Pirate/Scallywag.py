from ..Card import Card
from .SkyPirate import SkyPirate
import random


class Scallywag(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "죽음의 메아리: 1/1 해적을 소환합니다. 그 해적이 즉시 공격합니다."
        self.type = "Pirate"
        self.name = "뱃사람"
        self.name_eng = "Scallywag"
        self.attack = 2
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

    def _summon_sky_pirate(self, mine, opponent):
        sky_pirate = SkyPirate()
        self._summon_card(mine, sky_pirate, mine.get_card_list().index(self))

        if opponent.get_live_card_num() > 0:
            if opponent.get_taunt_live_card_num() > 0:
                shield_minion = random.choice(opponent.get_live_taunt_card_list())
            else:
                shield_minion = random.choice(opponent.get_live_card_list())

            sky_pirate.battle(shield_minion, mine, opponent)

    def set_death_rattle_list(self) -> list:
        return [self._summon_sky_pirate]
