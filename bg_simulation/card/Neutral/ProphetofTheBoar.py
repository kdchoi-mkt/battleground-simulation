from ..Card import Card

class ProphetofTheBoar(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '한 턴에 한 번: 내가 가시멧돼지를 낸 후에, 혈석을 얻습니다.'
        self.type = 'Neutral'
        self.name = '멧돼지의 예언자'
        self.name_eng = 'Prophet of the Boar '
        self.attack = 2
        self.health = 3
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
        