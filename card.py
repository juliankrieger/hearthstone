import attr

@attr.s
class Card:
    id = attr.ib(default=None)
    dbfId = attr.ib(default=None)
    name = attr.ib(default=None)
    text = attr.ib(default=None)
    flavor = attr.ib(default=None)
    artist = attr.ib(default=None)
    attack = attr.ib(default=None)
    cardClass = attr.ib(default=None)
    collectible = attr.ib(default=None)
    cost = attr.ib(default=None)
    elite = attr.ib(default=None)
    faction = attr.ib(default=None)
    health = attr.ib(default=None)
    mechanics = attr.ib(default=None)
    rarity = attr.ib(default=None)
    set = attr.ib(default=None)
    type = attr.ib(default=None)
    playRequirements = attr.ib(default=None)
    referencedTags = attr.ib(default=None)
    race = attr.ib(default=None)
    targetingArrowText = attr.ib(default=None)
    durability = attr.ib(default=None)
    overload = attr.ib(default=None)
    spellDamage = attr.ib(default=None)
    collectionText = attr.ib(default=None)
    armor = attr.ib(default=None)
    entourage = attr.ib(default=None)
    puzzleType = attr.ib(default=None)
    hideStats = attr.ib(default=None)
    howToEarn = attr.ib(default=None)
    howToEarnGolden = attr.ib(default=None)
    classes = attr.ib(default=None)
    multiClassGroup = attr.ib(default=None)
    questReward = attr.ib(default=None)

    def __repr__(self):
        return self.name