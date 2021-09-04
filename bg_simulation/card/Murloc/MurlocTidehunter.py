from ..Card import Card
from .MurlocScout import MurlocScout


class MurlocTidehunter(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "전투의 함성: 1/1 멀록 정찰병을 소환합니다."
        self.type = "Murloc"
        self.name = "멀록 바다사냥꾼"
        self.name_eng = "Murloc Tidehunter"
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
        self.death_rattle = False
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def trigger_after_battle_cry(self, mine):
        self._summon_card(mine, MurlocScout(), mine.get_card_list().index(self))
