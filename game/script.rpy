# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alea Tori")
define v = Character("Disembodied Voice")
define d = Character("Distorted Voice")

#variables for the game
default choseClothes = False 


# The game starts here.

label start:

    call spriteExamples

    # Opening scene
    scene black bg 
    "I only see darkness, I only hear whispers in my dreams." 
    "My feet drag against the concrete sidewalk."
    "Yet another restless night."
    "East End High is a 5-minute walk from home."
    "Class starts in 5 minutes."
    "5 precious minutes that I need to {i}remember...{/i}"
    "A chilling voice cuts through the dark memory."
    "{i}Fosc jo.{/i}"
    "I open my eyes to the tired concrete."
    "My feet walk me to class, but I am not moving them."
    "If I could just remember what was in that dream."
    scene schoolHallway bg
    menu: 
        "Ignore": 
            "Best if I just ignore it."
            "My five, futile minutes disappear as I walk into the classroom."
            "I rub my exhausted, throbbing head. I even start swatting at the whisper floating around in my mind."
        "Keep Thinking": 
            "I mouth the words."
            "I lift my head and recite it out loud: {i}Fosc jo.{/i}"
            "Is it Spanish?"
            "As I walk, I pull up a translator on my phone and type it in. It can't interpret the words."
            # audio: error noise
            "Definity {i}not{/i} Spanish."
            "I lower my phone to my pocket."
            "But then I feel a chill against my wrist."
            "Frozen, I turn my head slowly."
            "But I'm already in the empty hallway, at the foot of the door to the same old classroom with the same old classmates."
            "Relief and disappointment flood and flush from my mind."
    #next choice
    menu: 
        "Have Lunch": 
            "I walk into the cafeteria after class."
            "Sitting alone at a table, I stare at the uninspiring chicken sandwich on my tray."
            # art put entity in the background
            "But I don't think I have the appetite right now."
            "I think I'll skip lunch today."
        "Go to Study Hall": 
            "Maybe I just don't have the appetite for the cafeteria's uninspiring chicken sandwiches today."
            "I quickly exit the room and walk opposite my classmates while they head to lunch."
            "As I walk away from the classroom, I stare out the window."
            "The light shines brightly every time I look through it."
            "Almost as though I'm looking right after being showered in darkness."
            "I turn away from the windows towards my locker, opening it to retrieve my backpack, but just behind the edge of the locker ..."
            #art: put a facelss, formless figure in the background
            # no audio
            "I turn my head, but there's no one standing there."
            "The sun is clouded and the light stops blinding me for a moment."
            "I think I'll just study at home today."
    #time passes
    scene ch1Room bg 
    "I close the door behind me as I return to my room."
    "I throw my backpack to the floor and lie face down on my bed, taking a pillow into my arms and burying my face in it."
    "Another day wasted thinking about this silly dream."
    "{i}Fosc jo{/i}."
    # art: put a transparent figure on a chair in the background.
    "Am I seeing things?"
    "I sit up from my bed, pushing myself off the pillow."
    "The chair is empty."
    menu: 
        "Ignore": 
            "There's nothing there, I tell myself."
            "It's all just in my head."
            "I should at least try to get some sleep. I lower myself back into my pillow."
            # audio: object falling to the floor.
            scene book bg
            "It was just a book. I must have left it hanging from my desk."
        "Go and Look": 
            "I move my legs off the bed and sit at the edge."
            "I run my hand across the chair."
            "My mind must be playing tricks."
            "I'm creeping myself out."
            "There's no one here, but I could've sworn that someone was following me today."
            "But there's no point in dwelling on it when I'm alone in my bedroom."
            "I really want to sleep."
            "It's all in my head. It's all in my head."
            "It's all in my head. I repeat it until my eyes flutter shut and I drift away, back into the dark."
            # art: put a transparent, mysterious figure sitting on a chair in the background. 
    jump october_29th

label october_29th: 
    scene black bg
    "The pitch black floor is cold beneath my feet."
    "For a moment, I think I'm staring into a dark, pitch black space."
    "A figure materializes in front of me."
    "The blank, grainy face of the figure stares into me."
    "In the darkness, it's wearing a light, flowing skirt and a bright white shirt..."
    "I know those clothes - I threw them to the back of my closet years ago."
    "The figure reaches out to me."
    "When I take a step back, it floats forward, through me."
    "When I turn to face it, I'm in my classroom."
    "I sit at my desk, surrounded by my classmates like they're getting along."
    "I turn to exit the room, but as I walk backwards through the door, I'm in the corner of the cafeteria."
    "The figure is surrounded by even more people."
    "{i}Fosc Jo{/i}"
    "My hand twitches. It rears its head at me and stares at me with its blank, ambiguous face."
    "My body lurches, and I'm back in my bed, covered in a sweat."
    "I sit up to feel my forehead - cold and wet."
    "It's time to get up again."
    scene roomMorning bg 
    "My feet touch an array of clothes on the floor."
    "My room is a mess of clothes and books."
    "It didn't look like this last night..."
    "Who could have done this?"
    "I walk across the messy floor to my door and check the knob."
    "Still locked."
    "When I turn back to my bed, I see the same damn clothes on my chair, freshly laid out for me to put on."
    "My trembling legs give out and I drop to the floor."
    "Shaking, I look around for any of my usual dark clothes, but my wrinkled laundry is sprawled beneath the chair."
    "Every instinct is demanding that I put the skirt on. It stands out among the darkness of my room."
    "This outfit was picked out just for me."
    menu: 
        "Better to Put on the Clothes": 
            "Crawling to my chair, I reach for the bright clothes and put them on."
            "They feel cold against my skin."
            "I look for the shady figure in my room, to see if it is satisfied and will leave me alone."
            "I can feel its silent presence in the the room, but it doesn't make itself known."
        "Resist and Choose Your Own Clothes": 
            $ choseClothes = True
            "Crawling to my chair, I snatch whatever dark clothes I can find underneath and scurry back to the opposite end of the room."
            "I put on a wrinkly pair of jeans and an old black t-shirt."
            "I look for the shady figure in my room to see if it will attack me."
            "I can feel its silent presence in the room, but it doesn't make itself known."
    "Walking quietly out of my room, I am met by my mom and dad, who were listening in outside my door."
    "When they try talking to me, I can barely process their words. Only muffled sounds, but I can hear the worry in their voices."
    "They each take one of my cold hands and walk me to the kitchen for breakfast."
    "I stare into an empty glass and see their concerned faces in the reflection."
    "I glance at my mom and she gives me a smile concealing her worry."
    "My voice sits at the bottom of my stomach and whatever words I try to say well up in my throat."
    "As we eat Dad's eggs and bacon, I can only sound a light grunt or quiet sniffle."
    "I reach for the glass, hoping to wash down the choking feeling, but before I can touch it, the cup topples over and drops to the floor, shattering."
    "My dad tries to hide his panic as he fantically searches for a broom. Mom pulls me away from the broken glass."
    "But in the reflection of the floor and shards, I don't see myself, but the dark figure in my clothes."
    "I jump back, taking my body from my mom's arms."
    "As I move, the reflection shifts to my parents, exchanging glances and nodding."
    "I feel my shivering hands engulfed in the warmth of my mom's. She gives me a reassuring smile and caresses my cheek."
    "From her lips, I read she's going to walk me to the park, just like when I was a kid..."
    scene park bg 
    "After a little convincing, my dad gets me to toss a frisbee with him on the park lawn."
    "Of course, I miss the catch and it lands next to my mom, sitting on a bench."
    "She picks it up and gestures that we switch, and replaces me in dad's frisbee game."
    "I sit down and try to take in the sounds of the park. I look around a little to settle down."
    if choseClothes:
        menu:
            "Look at the Animals": 
                jump lookAtAnimals
            "Lonely Tree": 
                jump lonelyTree
    jump lookAtAnimals #automatic choice if didn't choose own clothes
    
    label lookAtAnimals: 
        "When I was a kid, I used to surround myself with the animals in the park."
        "But the butterflies and the birds are almost nowhere to be seen."
        "Even the squirrels retreat behind the trees whenever I look their way."
        "Envy swirls in me as they escape when I can't."
        jump october_29thContinued
    
    label lonelyTree: 
        "The shadows of the park darken and enlarge, hiding the park that comforted me years ago."
        "My head throbs again, and I seek out anything that could take me out of that overwhelming dream."
        scene tree bg        
        "I see a tree in a clearing of brown moss that I'd never noticed before."
        "Just looking at it makes my head hurt less."
        "While my parents toss the frisbee, I walk over to the tree."
        "The closer I get, the less I feel the entity's hold on me."
        "Underneath the lonely tree, I can't feel the darkness anymore."
        "How?"
        "A gentle force wraps around me and ushers me to rest underneath the tree."
        "My muscles relax and my mind focuses. A disembodied, feminine voice calls to me." 
        v "{i}I know how you suffer.{/i}"
        "Its presence mirrors the gentle forces coming off of the tree."
        v "{i}What haunts you will try to take what is precious to you.{/i}"
        "My voice returns to me as I respond to the benevolent presence."
        a "What am I supposed to do?"
        v "{i}The answer lies in you.{/i}"
        a "That's predictable. I need more answers than that."
        v "{i}Time is short. The being that pursues you is returning.{/i}"
        v "{i}All I can say before I leave you is that the being lies within you and only you have the power to control her.{/i}"
        v "{i}You must focus and accept yourself.{/i}"
        v "{i}It is only through acceptance that the negativity can be-{/i}"
        d "Xafarder! Ves-te'n ja!"
        "A deep, distorted voice cuts through the illusion."
        "My sanctuary disappears, and I fall back to the ground."
        "The tree is gone, and the voice has vanished."
        "What was that? What was it trying to tell me?"
        "Was it even real? Was any of this in the first place?"
        "The feeling of abandonment mixes into the returning despair that has haunted my dreams."
        #This part needs to updated. Note: the lonely tree choice ends here and if the player chooses look at animals the player will see the text from line 208 after the text for that section  
        #She overhears her mom speaking to some of her relatives in Barcelona. Then she receives an epiphany. 
        #What if the phrase “fosc jo” wasn’t Spanish but Catalan. 
        #She looks the term up online and among the main results is the phrase “dark ego.” 
        #Even though Alea knows what the term means it does not help her predicament. 
        
    label october_29thContinued: 
        scene roomEvening bg 
        "Returning home from this experience has left me feeling doomed to a fate I don't know and can't avoid."
        "I skip dinner and stay awake in my room, curled up on the ground alone."
        "When I get up, I realize my notebook is open on the dresser."
        scene notebook bg
        "I see the open page and read the crooked letters written on it."
        "It says, \"The transformation has begun.\""
        "I grip the page. I tear it off, crumple it and throw out my window, shutting it as I watch the balled up paper hit the ground."
        "Another night with the light on leaves everything in a hazy blur."

        return


label spriteExamples: 
    show alea 
    "This is the basic command to show a sprite: show alea"
    show alea denial
    "If you show the same character but with a different expression, it automatically replaces the previous one. This is an example of \'show alea denial\'"
    show alea worried 
    "This is an example of \'show alea worried\'"
    hide alea 
    show entity
    "However, to show a different character, you should hide the previous character."
    hide entity 
    show alea sigh at left
    "You can also change where on the screen the sprite shows up with adding \'at left\', \'at center\', etc to the end."
    show alea tired 
    "This is an example of \'show alea tired\'"
    
    return