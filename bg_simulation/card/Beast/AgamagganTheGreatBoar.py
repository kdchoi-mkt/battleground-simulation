from ..Card import Card

class AgamagganTheGreatBoar(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내 혈석이 추가로 +1/+1을 부여합니다.'
        self.type = 'Beast'
        self.name = '위대한 멧돼지 아감마간'
        self.name_eng = 'Agamaggan, The Great Boar'
        self.attack = 6
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
        