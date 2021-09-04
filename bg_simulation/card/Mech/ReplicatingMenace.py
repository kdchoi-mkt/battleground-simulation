from ..Card import Card

class ReplicatingMenace(Card):
    def __init__(self):
        Card.__init__(self)

    def reset(self):
        self.text = '합체, 죽음의 메아리: 1/1 초소형 로봇을 셋 소환합니다.'
        self.type = 'Mech'
        self.name = '증식하는 위협'
        self.name_eng = 'Replicating Menace'
        self.attack = 3
        self.health = 1
        self.tier = 3
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
        