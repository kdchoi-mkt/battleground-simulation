from ..Card import Card

class NomiKitchenNightmare(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내가 정령을 낸 후에, 이번 게임 동안 밥의 선술집에 있는 정령들이 +1/+1을 얻습니다.'
        self.type = 'Neutral'
        self.name = '주방의 악몽 노미'
        self.name_eng = 'Nomi, Kitchen Nightmare'
        self.attack = 4
        self.health = 4
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
        