import Control as c


def run():
    english1 = input(
        "First Period: English"
        "\nYou open your schoolbag and grab the assigned reading. Will you..."
        "\n1.Read alone like a scrub"
        "\n2.Ask Edward to read with you\n")
    if english1 == "1":
        print("\nYou decide to read by yourself. Its lonely, but you do get all your work done ahead of time.\n")
        english2 = input(
            "Glancing about the room, you notice Edward's supreme intellect has allowed him to finish early as well."
            "\nYou lingers on his form for too long, he looks up and meets your eyes!"
            "\n1.ABORT! ABORT! LOOK AWAY!"
            "\n2.Steel your resolve and give him a wave"
            "\n3.Bask unashamed in the glorious gaze of his dark chestnut brown eyes.")
        if english2 == "1":
            print("The shame of being caught hangs over you. You keep your head down and don't look up again until"
                  "the bell rings. ")
        if english2 == "2":
            print("Edward considers you for a moment, then waves back with a smile.")
            c.lp_up(1)
            print("Overwhelmed with giddiness at having gotten a reaction, you barely hear the bell ring. "
                  "On your way out of class you end up walking with Edward in the halls. You should say something "
                  "to break up the awkward atmosphere..."
                  "\n1. WIP"
                  "\n2. WIP"
                  "\n3. WIP")
            # edward waves back, small lp, leads to a conversation in the hallway
        if english2 == "3":
            print("You stare longingly into Edward's eyes. Hoping that your deepest affections can be broadcast"
                  "through this moment your sharing together."
                  "\nInstead, Edward makes a face and looks away. Stupid! You lost track of time swimming in his"
                  "chocolate fondue eyes and stared for way too long."
                  "\nSoon after this regrettable exchange, the bell rings and its time to go to second period.")
            c.lp_down(1)
    elif english1 == "2":
        print("You walk across the room and awkwardly ask Edward if he wants to read together.")
        c.lp_down(1)
        print("TESTING LovePoints: " + str(c.LP))

# Try not to put too many LP checks early on in the game, it wont be possible to get to 30 over a period or two
# The lp_down should have its own reaction message, so you don't need one
