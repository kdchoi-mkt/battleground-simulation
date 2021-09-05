from ..Card import Card


class ZappSlywick(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "질풍, 이 하수인은 공격력이 가장 낮은 적 하수인을 무조건 공격합니다."
        self.type = "Neutral"
        self.name = "잽 슬라이윅"
        self.name_eng = "Zapp Slywick"
        self.attack = 7
        self.health = 10
        self.tier = 6
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.windfury = True
        self.reborn = False
        self.frenzy = False
        self.poison = False
        self.avenge = False
        self.avenge_count = 0
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
