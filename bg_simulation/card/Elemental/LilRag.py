from ..Card import Card

class LilRag(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '내가 정령을 낸 후에, 아군 하수인에게 그 정령의 선술집 단계만큼 능력치를 부여합니다.'
        self.type = 'Elemental'
        self.name = '꼬마 라그'
        self.name_eng = 'Lil Rag'
        self.attack = 6
        self.health = 6
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
        