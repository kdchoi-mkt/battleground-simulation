from ..Card import Card

class ImpMama(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '이 하수인은 피해를 받을 때마다 무작위 악마를 소환하고 그 악마에게 도발을 부여합니다.'
        self.type = 'Demon'
        self.name = '어미 임프'
        self.name_eng = 'Imp Mama'
        self.attack = 6
        self.health = 10
        self.tier = 6
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
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        