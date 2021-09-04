class Card(object):
    def __init__(
        self
    ):
        self.reset()

    def reset(self):
        self.type = 'None'
        self.attack = 2
        self.health = 1
        self.tier = 1
        self.live = True
        self.taunt = False
        self.divine_shield = False
        self.fury = False
        self.revive = False
        self.frenzy = False

    def when_attack(self, mine, opponent, targeted):
        pass

    def when_dead(self, mine, opponent, dead):
        pass

    def get_type(self):
        return self.type

    def lose_health(self, damage, mine, opponent):
        if self.divine_shield == True:
            self.divine_shield = False
        else:
            self.health -= damage

            if self.health <= 0:
                self.live = False
                self.trigger_death_rattle(mine, opponent)
                mine.trigger_dead(opponent, self)

                if self.revive == True:
                    self.reset()
                    self.health = 1
                    self.revive = False
            else:
                if self.frenzy == True:
                    self.trigger_frenzy(self)

    def trigger_frenzy(self):
        pass

    def gain_attack(self, damage):
        self.attack += damage

    def set_health(self, health):
        self.health = health

    def set_attack(self, attack):
        self.attack = attack

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_tier(self):
        return self.tier

    def is_live(self):
        return self.live

    def is_taunt(self):
        return self.taunt

    def set_taunt(self, taunt):
        self.taunt = taunt

    def is_fury(self):
        return self.fury

    def set_fury(self, fury):
        self.fury = fury

    def is_divine_shield(self):
        return self.divine_shield

    def set_divine_shield(self, divine_shield):
        self.divine_shield = divine_shield

    def is_revive(self):
        return self.is_revive

    def set_revive(self, revive):
        self.is_revive = revive

    def trigger_death_rattle(self, mine, opponent):
        pass

    def __repr__(self):
        return f"Type: {self.type}, Attack: {self.attack}, Health: {self.health}"
