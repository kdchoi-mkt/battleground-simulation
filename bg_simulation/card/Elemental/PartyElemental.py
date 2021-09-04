from ..Card import Card

class PartyElemental(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내가 정령을 낸 후에, 다른 무작위 아군 정령에게 +1/+1을 부여합니다.'
        self.type = 'Elemental'
        self.name = '파티의 정령'
        self.name_eng = 'Party Elemental'
        self.attack = 3
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
        self.death_rattle = False
        self.battle_cry = False
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        