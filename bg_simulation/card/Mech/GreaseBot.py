from ..Card import Card


class GreaseBot(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '아군 하수인이 천상의 보호막을 잃은 후에, 그 하수인에게 영구히 +2/+1을 부여합니다.'
        self.type = 'Mech'
        self.name = '기름 로봇'
        self.name_eng = 'Grease Bot'
        self.attack = 3
        self.health = 6
        self.tier = 4
        self.live = True
        self.taunt = False
        self.divine_shield = True
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

    def when_lose_ds(self, mine, opponent, targeted):
        targeted.gain_health(1)
        targeted.gain_attack(2)
