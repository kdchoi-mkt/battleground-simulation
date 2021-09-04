from ..Card import Card

class ScavengingHyena(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '아군 야수가 죽을 때마다 +2/+1을 얻습니다.'
        self.type = 'Beast'
        self.name = '청소부 하이에나'
        self.name_eng = 'Scavenging Hyena'
        self.attack = 2
        self.health = 2
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
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        