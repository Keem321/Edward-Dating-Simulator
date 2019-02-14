import random
day = 1
# global variable to keep track of the days (replaces counter for 5 day loop)
LP = 10
# LovePoints, how to win, unlocks new paths, core of the game really.


def lp_up(level):
    global LP
    print(posReacTable.get(random.randint(0, 9)))
    if level == 1:
        LP += 1
    if level == 2:
        LP += 3
    if level == 3:
        LP += 5


def lp_down(level):
    global LP
    print(negReacTable.get(random.randint(0, 9)))
    if level == 1:
        LP -= 1
    if level == 2:
        LP -= 3
    if level == 3:
        LP -= 5


def lp_big_up(level):
    global LP
    print(extraPosReacTable.get(random.randint(0, 9)))
    if level == 1:
        LP += 10
    if level == 2:
        LP += 15
    if level == 3:
        LP += 20


def lp_big_down(level):
    global LP
    print(extraNegReacTable.get(random.randint(0, 9)))
    if level == 1:
        LP -= 10
    if level == 2:
        LP -= 15
    if level == 3:
        LP -= 20


posReacTable = {
    0: "Edward is pleased with you.",
    1: "Edward smiles at you.",
    2: "Edward makes eye contact with you and smiles",
    3: "Edward giggles.",
    4: "You made Edward happy!",
    5: "The corners of Edward's luscious lips turn up slightly.",
    6: "Edward gives you a thumbs up.",
    7: "Edward chuckles.",
    8: "You can see Edward's pleasure with your actions.",
    9: "Edward makes physical contact with you.",
    }

negReacTable = {
    0: "Edward is displeased with you.",
    1: "Edward frowns at you.",
    2: "Edward makes eye contact with you and frowns",
    3: "Edward looks displeased.",
    4: "You made Edward sad!",
    5: "The glorious light in Edward's eyes dims a little.",
    6: "Edward shoots you a sideways glance",
    7: "Edward groans under his breath.",
    8: "You can see Edward's displeasure with your actions.",
    9: "Edward makes an awkward glance away from you.",
    }

extraNegReacTable = {
    0: "Edward is angry at you!",
    1: "Edward groans with displeasure.",
    2: "Edward scowls.",
    3: "Edward makes an outraged face!",
    4: "Edward rolls his eyes in disgust.",
    5: "Edward can barely contain his anger.",
    6: "Edward's baby face is a frightening sight to behold as it is contorted by his anger.",
    7: "You have offended Edward!",
    8: "Edward does not like this!",
    9: "Edward is visually upset!",
    }

extraPosReacTable = {
    0: "Edward laughs and smiles!",
    1: "Edward blushes but looks happy.",
    2: "Edward cannot contain his happiness.",
    3: "Edward gives you a look of deep compassion.",
    4: "Edward is elated!",
    5: "You made Edward extremely happy!",
    6: "Edward puts his hand on your shoulder, and smiles.",
    7: "Edward looks deep into his eyes.",
    8: "Edward gives you a smile, and you notice the smile linger on for a few minutes...",
    9: "Edward looks down at his feet, but he is trying not to show the large smile on his face. ",
}
