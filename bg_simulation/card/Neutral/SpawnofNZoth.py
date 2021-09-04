from ..Card import Card

class SpawnofNZoth(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '죽음의 메아리: 내 하수인들에게 +1/+1을 부여합니다.'
        self.type = 'Neutral'
        self.name = '느조스의 피조물'
        self.name_eng = 'Spawn of NZoth'
        self.attack = 2
        self.health = 2
        self.tier = 2
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
        