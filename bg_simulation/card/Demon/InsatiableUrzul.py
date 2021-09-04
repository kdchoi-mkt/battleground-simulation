from ..Card import Card

class InsatiableUrzul(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '도발, 내가 악마를 낸 후에, 밥의 선술집에 있는 하수인을 잡아먹습니다. 그 하수인의 능력치를 얻습니다.'
        self.type = 'Demon'
        self.name = '허기진 우르줄'
        self.name_eng = 'Insatiable Urzul'
        self.attack = 4
        self.health = 6
        self.tier = 5
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
        