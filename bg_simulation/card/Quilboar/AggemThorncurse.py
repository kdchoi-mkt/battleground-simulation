from ..Card import Card

class AggemThorncurse(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '이 하수인에게 혈석을 낸 후에, 모든 아군 종족에게 각각 +1/+1을 부여합니다. (종족마다 하나씩)'
        self.type = 'Quilboar'
        self.name = '아겜 쏜커스'
        self.name_eng = ' Aggem Thorncurse'
        self.attack = 3
        self.health = 6
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
        