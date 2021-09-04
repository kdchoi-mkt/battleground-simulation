from ..Card import Card

class KalecgosArcaneAspect(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내가 전투의 함성 하수인을 낸 후에, 내 용족들에게 +1/+1을 부여합니다.'
        self.type = 'Dragon'
        self.name = '비전의 위상 칼렉고스'
        self.name_eng = 'Kalecgos, Arcane Aspect'
        self.attack = 4
        self.health = 12
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
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        