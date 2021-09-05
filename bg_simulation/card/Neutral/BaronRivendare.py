from ..Card import Card


class BaronRivendare(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = "내 하수인들의 죽음의 메아리 능력이 2번 발동합니다."
        self.type = "Neutral"
        self.name = "남작 리븐데어"
        self.name_eng = "Baron Rivendare"
        self.attack = 1
        self.health = 7
        self.tier = 5
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
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()

    def when_trigger_death_rattle(self, mine: "Player", opponent: "Player", dead: Card):
        dead.trigger_death_rattle(mine, opponent, if_first=False)
