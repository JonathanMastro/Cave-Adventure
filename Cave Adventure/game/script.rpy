# The script of the game goes in this file.

#voice actors
define N = Character("")


#Game start
label start:
    scene devmap
    #creating flags/variables
    $ hiddenwall = "true"
    $ tnt = "false"
    $ crowbar = "false"
    $ tntused = "false"
    $ crowbarused = "false"
    $ map = "false"
    jump ItemSelection


label ItemSelection:
    scene bg blank

    N "Pick one item to help you in the game."

    menu:
        "take tnt":
            N "Are you sure?"
            menu:
                "Yes":
                    N "You've decided that taking explosives to find treasure in a cave is a good idea."
                    $tnt = "true"
                    jump CaveEntrance

                "No":
                    jump ItemSelection


        "take crowbar":
            N "Are you sure?"
            menu:
                "Yes":
                    N "You've decided to take the crowbar."
                    $crowbar = "true"
                    jump CaveEntrance

                "No":
                    jump ItemSelection


        "take map":
            N "Are you sure?"
            menu:
                "Yes":
                    N "You've decided to take the map."
                    $map = "true"
                    jump CaveEntrance

                "No":
                    jump ItemSelection


        "take nothing":
            N "Are you sure?"
            menu:
                "Yes":
                    N "You've decided you don't need any crutches like 'maps' or 'crowbars' to go treasure hunting."
                    jump CaveEntrance

                "No":
                    jump ItemSelection


label introduction:
    N "You head off to a cave rumoured to have massive riches hidden inside."


label CaveEntrance:

    scene bg outsidecave
    menu:
        "Enter cave":
            jump Room3
        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump CaveEntrance


#Room #1
label Room1:
    scene bg forwardnright

    menu:
        "Forward":
            jump Room6

        "Right":
            jump Room2

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room1


#Room #2
label Room2:
    scene bg 3doors

    menu:
        "Forward":
            jump Room7

        "Left":
            jump Room1

        "Right":
            jump Room3

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room2


#Room #3
label Room3:
    scene bg 3doors

    menu:
        "Forward":
            jump Room8

        "Left":
            jump Room2

        "Right":
            jump Room4

        "Backward":
            jump CaveEntrance

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room3


#Room #4
label Room4:
    scene bg 3doors

    menu:
        "Forward":
            jump Room9

        "Left":
            jump Room3

        "Right":
            jump Room5

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room4


#Room #5
label Room5:
    if (crowbar == "true"):
        scene bg forwardnleft
    else:
        scene bg crowbarforwardnleft
        N "You find a crowbar laying in the center of the room."

    menu:
        "Forward":
            jump Room10

        "Left":
            jump Room4

        "Pick up crowbar" if crowbar == "false":
            $ crowbar = "true"
            N "You pick up the crowbar."
            jump Room5

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room5


#Room #6
label Room6:
    scene bg forwardnright

    menu:
        "Forward":
            jump Room11

        "Right":
            jump Room7

        "Backward":
            jump Room1

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room6


#Room #7
label Room7:
    if (tnt == "true"):
        scene bg 3doors
    else:
        scene bg tnt3doors
        N "You find a stick of tnt laying in the center of the room."

    menu:
        "Forward":
            jump Room12

        "Left":
            jump Room6

        "Right":
            jump Room8

        "Backward":
            jump Room2

        "Pick up tnt" if tnt == "false":
            $ tnt = "true"
            N "You pick up the tnt and put it in your pocket."
            jump Room7

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room7


#Room #8
label Room8:
    scene bg 3doors

    menu:
        "Forward":
            jump Room13

        "Left":
            jump Room7

        "Right":
            jump Room9

        "Backward":
            jump Room3

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room8


#Room #9
label Room9:
    scene bg 3doors

    menu:
        "Forward":
            jump Room14

        "Left":
            jump Room8

        "Right":
            jump Room10

        "Backward":
            jump Room4

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room9


#Room #10
label Room10:
    scene bg forwardnleft

    menu:
        "Forward":
            jump Room15

        "Left":
            jump Room9

        "Backward":
            jump Room5

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room10


#Room #11
label Room11:
    scene bg right

    menu:
        "Right":
            jump Room12

        "Backward":
            jump Room6

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room11


#Room #12
label Room12:
    scene bg leftnright

    menu:
        "Left":
            jump Room11

        "Right":
            jump Room13

        "Backward":
            jump Room7

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room12


#Room #13
label Room13:
    scene bg leftnright

    menu:
        "Left":
            jump Room12

        "Right":
            jump Room14

        "Backward":
            jump Room8

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room13


#Room #14
label Room14:
    scene bg leftnright

    menu:
        "Left":
            jump Room13

        "Right":
            jump Room15

        "Backward":
            jump Room9

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room14


#Room #15
label Room15:
    if (hiddenwall == "true"):
        scene bg leftnbright
        N "There's a cracked wall on the right side of the room."
        N "Maybe something could break it open?"
    elif (tntused == "true"):
        scene bg leftnright
        N "There's a door shaped hole in the right wall caused by the tnt explosion."
    elif (crowbarused == "true"):
        scene bg leftnright
        N "There's a door shaped hole in the right wall caused by you and your crowbar."
    else:
        scene bg leftnright
        N "There's a door shaped hole in the right wall."


    menu:
        "Left":
            jump Room14

        "Backward":
            jump Room10

        "blow up wall" if (tnt == "true" and hiddenwall == "true"):
            $tnt = "false"
            $tntused = "true"
            $hiddenwall = "false"
            N "You light the tnt and throw it at the wall."
            N "You hear a loud explosion followed by rocks hitting the ground."
            jump Room15

        "Break open wall" if (crowbar == "true" and hiddenwall == "true"):
            $crowbarused = "true"
            $hiddenwall = "false"
            N "You take your crowbar out."
            N "You begin to use the crowbar to repeatedly whack the cracked wall and breaking rocks away."
            N "."
            N ".."
            N "..."
            jump Room15

        "Right" if hiddenwall == "false":
            jump Room16

        "Read map" if map == "true":
            show playermap
            menu:
                "done":
                    hide playermap
                    jump Room15


#Room #16 - treasure room
label Room16:
    scene bg treasureroom
    N "You've found the hidden treasure room!"
    N "The walls are made of gold and the floor is (badly drawn) marble tiles!"
    N "In the center is two big treasure chests filled with gold and jewels."

    menu:
        "Collect the treasure and leave":
            N "You take both chests and carry them home with you."
            N "With your newfound treasure, you now have enough money to live comfortably without ever having to work again."
            return
