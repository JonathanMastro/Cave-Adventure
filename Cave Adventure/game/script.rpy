# The script of the game goes in this file.

#voice actors
define t = Character("DevTest")
define N = Character("")


#Game start
label start:
    scene devmap
    #creating flags/variables
    $ hiddenwall = "true"
    $ tnt = "false"
    N "Game start"
    jump ItemSelection


label ItemSelection:
    scene bg blank

    t "item selection - pick one"

    menu:
        "take tnt":
            $tnt = "true"
            jump CaveEntrance
        "take nothing":
            jump CaveEntrance

        #items to add
        #map - add menu option to check map in each room
        #crowbar for doors - add a room to find crowbar
        #if have time, add an "are you sure" option to the menu.




label CaveEntrance:

    scene bg outsidecave
    N "Cave Entrance"
    menu:
        "Enter cave":
            jump Room3






#Room #1
label Room1:
    #Forward and right picture
    scene bg forwardnright
    t "Room #1"

    menu:
        "Forward":
            jump Room6

        "Right":
            jump Room2


#Room #2
label Room2:
    #3 doors picture
    scene bg 3doors
    t "Room #2"

    menu:
        "Forward":
            jump Room7

        "Left":
            jump Room1

        "Right":
            jump Room3


#Room #3
label Room3:
    #3 doors picture
    scene bg 3doors
    t "Room #3"

    menu:
        "Forward":
            jump Room8

        "Left":
            jump Room2

        "Right":
            jump Room4

        "Backward":
            #exits the cave
            jump CaveEntrance


#Room #4
label Room4:
    #3 doors picture
    scene bg 3doors
    t "Room #4"

    menu:
        "Forward":
            jump Room9

        "Left":
            jump Room3

        "Right":
            jump Room5


#Room #5
label Room5:
    #Forward and left picture
    scene bg forwardnleft
    t "Room #5"

    menu:
        "Forward":
            jump Room10

        "Left":
            jump Room4


#Room #6
label Room6:
    #Forward and right picture
    scene bg forwardnright
    t "Room #6"

    menu:
        "Forward":
            jump Room11

        "Right":
            jump Room7

        "Backward":
            jump Room1

#Room #7
label Room7:
    #3 doors picture
    scene bg 3doors
    t "Room #7"

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
            jump Room7

#Room #8
label Room8:
    #3 doors picture
    scene bg 3doors
    t "Room #8"

    menu:
        "Forward":
            jump Room13

        "Left":
            jump Room7

        "Right":
            jump Room9

        "Backward":
            jump Room3

#Room #9
label Room9:
    #3 doors picture
    scene bg 3doors
    t "Room #9"

    menu:
        "Forward":
            jump Room14

        "Left":
            jump Room8

        "Right":
            jump Room10

        "Backward":
            jump Room4

#Room #10
label Room10:
    #Forward and left picture
    scene bg forwardnleft
    t "Room #10"

    menu:
        "Forward":
            jump Room15

        "Left":
            jump Room9

        "Backward":
            jump Room5

#Room #11
label Room11:
    #Right picture
    scene bg right
    t "Room #11"

    menu:
        "Right":
            jump Room12

        "Backward":
            jump Room6

#Room #12
label Room12:
    #Left and right picture
    scene bg leftnright
    t "Room #12"

    menu:
        "Left":
            jump Room11

        "Right":
            jump Room13

        "Backward":
            jump Room7

#Room #13
label Room13:
    #Left and right picture
    scene bg leftnright
    t "Room #13"

    menu:
        "Left":
            jump Room12

        "Right":
            jump Room14

        "Backward":
            jump Room8

#Room #14
label Room14:
    #Left and right picture
    scene bg leftnright
    t "Room #14"

    menu:
        "Left":
            jump Room13

        "Right":
            jump Room15

        "Backward":
            jump Room9

#Room #15
label Room15:
    #Left and blocked right picture
    if (hiddenwall == "true"):
        scene bg leftnbright
    else:
        scene bg leftnright

    t "Room #15"

    menu:
        "Left":
            jump Room14

        "Backward":
            jump Room10

        "blow up wall" if (tnt == "true" and hiddenwall == "true"):
            $tnt = "false"
            $hiddenwall = "false"
            jump Room15

        "Right" if hiddenwall == "false":
            jump Room16



#Room #16
label Room16:
    #treasure room
    scene bg treasureroom
    t "Room #16"

    menu:
        "Left":
            jump Room15
