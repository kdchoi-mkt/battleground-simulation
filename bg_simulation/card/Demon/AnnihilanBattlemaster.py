from ..Card import Card

class AnnihilanBattlemaster(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '전투의 함성: 내 영웅이 받은 피해 1당 생명력을 +1 얻습니다.'
        self.type = 'Demon'
        self.name = '아나이힐란 전투모병관'
        self.name_eng = 'Annihilan Battlemaster'
        self.attack = 3
        self.health = 1
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
        self.battle_cry = True
        self.available_in_shop = True
        self.death_rattle_list = self.set_death_rattle_list()
        