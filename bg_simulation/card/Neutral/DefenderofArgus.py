from ..Card import Card

class DefenderofArgus(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 양옆의 하수인들에게 +1/+1과 도발을 부여합니다.'
        self.type = 'Neutral'
        self.name = '아르거스의 수호자'
        self.name_eng = 'Defender of Argus'
        self.attack = 3
        self.health = 3
        self.tier = 4
        self.live = True
        self.taunt = True
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
        