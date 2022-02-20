print("""WELCOME TO BOB'S AUTO!
    Let's start Fixing! 🔧 
    
    You were driving down the street one night.
    Boom your lights for your car goes off; the engine turns pops off.
    You try to turn back on but nothing.
    """)

q1 = input(""""Do you?
A. Knock on some house door and ask for gas.
or
B. Check in the trunk and see if you find any gas there: """)

if q1 == 'A':
    q2 = input("""You get out of the car walk over to house 391.
    You hit the door bell and nice old woman comes and greets you in you ask her for gas.
    She says here is the gas and you walk back to your car fill it up turn the engine on and she roars.
    
    You drive a little longer and see an O'reily auto parts and you really feal like getting some adons to
    make your car have a little more bling bling.
    
    You go into the shop and see a new spark plug that has 10x extra super bling bling in it.
    So you ask the person at the cash register and ask how much it is for the spark plug.
    He says that its $20
    
    Do you?
    A. Buy it
    or
    B. Not""")
    if q2 == 'A':
        input("""You reach into your pocket to find a $20 dollar bill.
        You find out you only have $15.
        Do you
        A. Ask him if he would be ok with having $15 for it
        or
        B. Say that you dont have enough money and Not buy it like the last question""")
    elif q2 == 'B':
        input("""You say to him nah I will go somewere else He puts you with a weird face and you leave the store.
        You hop into your car and you see that the cadillac converter is stolen.
        You don't go back into the O'relys because it would be kind of awkward so you go into another store called Soomboon
        Auto repair service. While walking strait  to the store you see a $20 on the ground.
        You are super happy in excitment.
        Do you
        A. go back to the O'reilys with it
        or
        B. Go and get the caddilac converter instead.""")
    else:
        print('u stoopid')
elif 'B':
    q3 = input("""You get out of the car and open the trunk you search back there for a whole entire minute.
    You do not find anything. 
    So you just feel stuck and wanna go back home.
    Do you
    A. Sleep in the car for the night
    or 
    B. Walk your way back to the house in the middle of the night.""")
    if q3 == 'A':
        input("""You at least find a sleeping back in the trunk.
        You bend down the back chairs to make it flat lock all the doors and huggle into the sleeping back
        and sleep.""")
    elif q3 == 'B':
        input("""""")
else:
    print('u stoopid')
