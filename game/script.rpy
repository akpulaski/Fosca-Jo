# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alea Tori")
define v = Character("Disembodied Voice")
define d = Character("Distorted Voice", what_font="Frank Knows.ttf")
define da = Character("Dark Alea")


#variables for the game
default choseClothes = False 
default wentToTree = False 
default remembered = False 
# The game starts here.

label start:

    menu: 
        "See Sprite Examples.":
            call spriteExamples
        "Play Game": 
            "Enjoy the game."

    # Opening scene
    scene black bg 
    centered "{font=fonts/Creepster-Regular.ttf}{size=+40}October 29th{/font}{w=1}{nw}"
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
    show alea
    # play alea's theme
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
            # play cellular phone interference sound
            "Definity {i}not{/i} Spanish."
            "I lower my phone to my pocket."
            "But then I feel a chill against my wrist."
            "Frozen, I turn my head slowly."
            "But I'm already in the empty hallway, at the foot of the door to the same old classroom with the same old classmates."
            "Relief and disappointment flood and flush from my mind."
    #next choice
    menu: 
        "Have Lunch":
            # play students talking SFX
            "I walk into the cafeteria after class."
            "Sitting alone at a table, I stare at the uninspiring chicken sandwich on my tray."
            hide alea 
            show entity
            "But I don't think I have the appetite right now."
            "I think I'll skip lunch today." 
        "Go to Study Hall": 
            "Maybe I just don't have the appetite for the cafeteria's uninspiring chicken sandwiches today."
            "I quickly exit the room and walk opposite my classmates while they head to lunch."
            "As I walk away from the classroom, I stare out the window."
            "The light shines brightly every time I look through it."
            "Almost as though I'm looking right after being showered in darkness."
            "I turn away from the windows towards my locker, opening it to retrieve my backpack, but just behind the edge of the locker ..."
            hide alea
            show entity
            # play entity's theme
            "I turn my head, but there's no one standing there."
            "The sun is clouded and the light stops blinding me for a moment."
            "I think I'll just study at home today."
    #time passes
    scene ch1Room bg
    # play alea's theme
    "I close the door behind me as I return to my room."
    "I throw my backpack to the floor and lie face down on my bed, taking a pillow into my arms and burying my face in it."
    "Another day wasted thinking about this silly dream."
    "{i}Fosc jo{/i}."
    show entity
    "Am I seeing things?"
    hide entity
    show alea denial
    "I sit up from my bed, pushing myself off the pillow."
    "The chair is empty."
    menu: 
        "Ignore": 
            "There's nothing there, I tell myself."
            "It's all just in my head."
            "I should at least try to get some sleep. I lower myself back into my pillow."
            # play entity's theme
            # play book falling sound
            scene book bg
            "It was just a book. I must have left it hanging from my desk."
        "Go and Look":
            # play entity's theme
            "I move my legs off the bed and sit at the edge."
            "I run my hand across the chair."
            "My mind must be playing tricks."
            "I'm creeping myself out."
            "There's no one here, but I could've sworn that someone was following me today."
            "But there's no point in dwelling on it when I'm alone in my bedroom."
            "I really want to sleep."
            "It's all in my head. It's all in my head."
            "It's all in my head. I repeat it until my eyes flutter shut and I drift away, back into the dark."
            # stop audio
            hide alea
            show entity 
            pause 1 
    jump october_30th

label october_30th: 
    scene black bg
    centered "{font=Creepster-Regular.ttf}{size=+40}October 30th{w=1}{nw}"
    show alea fear
    # play entity's theme
    "The pitch black floor is cold beneath my feet."
    "For a moment, I think I'm staring into a dark, pitch black space."
    "A figure materializes in front of me."
    show entity at right
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
    hide entity 
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
    show alea worried
    "When I turn back to my bed, I see the same damn clothes on my chair, freshly laid out for me to put on."
    "My trembling legs give out and I drop to the floor."
    show alea fear
    "Shaking, I look around for any of my usual dark clothes, but my wrinkled laundry is sprawled beneath the chair."
    "Every instinct is demanding that I put the skirt on. It stands out among the darkness of my room."
    "This outfit was picked out just for me."
    menu: 
        "Better to Put on the Clothes": 
            "Crawling to my chair, I reach for the bright clothes and put them on."
            hide alea
            "They feel cold against my skin."
            "I look for the shady figure in my room, to see if it is satisfied and will leave me alone."
            "I can feel its silent presence in the the room, but it doesn't make itself known."
        "Resist and Choose Your Own Clothes": 
            $ choseClothes = True
            "Crawling to my chair, I snatch whatever dark clothes I can find underneath and scurry back to the opposite end of the room."
            "I put on a wrinkly pair of jeans and an old black t-shirt."
            show alea
            "I look for the shady figure in my room to see if it will attack me."
            "I can feel its silent presence in the room, but it doesn't make itself known."
    # stop audio
    "Walking quietly out of my room, I am met by my mom and dad, who were listening in outside my door."
    "When they try talking to me, I can barely process their words. Only muffled sounds, but I can hear the worry in their voices."
    "They each take one of my cold hands and walk me to the kitchen for breakfast."
    "I stare into an empty glass and see their concerned faces in the reflection."
    "I glance at my mom and she gives me a smile concealing her worry."
    "My voice sits at the bottom of my stomach and whatever words I try to say well up in my throat."
    "As we eat Dad's eggs and bacon, I can only sound a light grunt or quiet sniffle."
    # play glass shattering sound
    "I reach for the glass, hoping to wash down the choking feeling, but before I can touch it, the cup topples over and drops to the floor, shattering."
    "My dad tries to hide his panic as he fantically searches for a broom. Mom pulls me away from the broken glass."
    "But in the reflection of the floor and shards, I don't see myself, but the dark figure in my clothes."
    show entity at right
    show alea
    "I jump back, taking my body from my mom's arms."
    "As I move, the reflection shifts to my parents, exchanging glances and nodding."
    "I feel my shivering hands engulfed in the warmth of my mom's. She gives me a reassuring smile and caresses my cheek."
    "From her lips, I read she's going to walk me to the park, just like when I was a kid..."
    hide entity 
    show alea worried
    scene park bg
    # play park sounds
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
    jump october_30thContinued
    
label lonelyTree: 
    $ wentToTree = True
    "The shadows of the park darken and enlarge, hiding the park that comforted me years ago."
    "My head throbs again, and I seek out anything that could take me out of that overwhelming dream."
    scene tree bg
    # play lonely tree track
    "I see a tree in a clearing of brown moss that I'd never noticed before."
    "Just looking at it makes my head hurt less."
    show alea
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
    # stop audio
    "My sanctuary disappears, and I fall back to the ground."
    "The tree is gone, and the voice has vanished."
    "What was that? What was it trying to tell me?"
    "Was it even real? Was any of this in the first place?"
    # play alea's theme
    "The feeling of abandonment mixes into the returning despair that has haunted my dreams."
    "In my rising panic, my parents rush me back home."
    "The time between being in the park and finding myself seated in front of my parents is lost to me."
    "Returning home from this experience has left me feeling doomed to a fate I don’t know and can’t avoid."
    "While my dad attempts to goad me into eating, I overhear my mom speaking with concern over the phone."
    "A lighter feeling rushes through my head as my mom speaks her native language."
    "What if {i}fosc jo{/i} isn’t Spanish, but Catalan?"
    "I push my dad’s food away."
    "I return to my room and lean on my door to close it."
    "I open my phone and look up the term {i}fosc jo{/i} again."
    "{i}Dark ego{/i}"
    "Not as helpful as I had hoped."
        
label october_30thContinued: 
    scene black bg 
    scene roomEvening bg 
    show alea tired
    # Returning home from this experience has left me feeling doomed to a fate I don't know and can't avoid."
    # I skip dinner and stay awake in my room, curled up on the ground alone."
    "When I return to my room, I realize my notebook is open on the dresser."
    scene notebook bg
    # play entity's theme
    "I see the open page and read the crooked letters written on it."
    "It says, \"The transformation has begun.\""
    scene roomEvening bg
    show alea fear
    "I grip the page. I tear it off, crumple it and throw out my window, shutting it as I watch the balled up paper hit the ground."
    "Another night with the light on leaves everything in a hazy blur."
    jump halloween

label halloween: 
    scene black bg 
    centered "{font=Creepster-Regular.ttf}{size=+40}Halloween{w=1}{nw}"
    scene mirrorLight bg
    show alea worried
    # play entity's theme
    "I've stayed up all night, eyes strained through the day until the evening of Halloween."
    "Kids in costumes pass my house like a blur as I space out from my room."
    "Nothing but a faceless, amorphic blur of a reflection stares back at me through the mirror."
    show alea worried at right
    show entity at left
    "That familiar, unwelcoming hold tightens around my throat, my wrists, and my ankles when I think about calling for help."
    "I'm paralyzed by freezing, invisible restraints."
    "There are no longer words that float around in my mind and in my dreams."
    "Only the dark intentions of the entity, its hands gripping my shoulders, pushing me down, forcing me to wait until midnight..."
    menu: 
        "Resist": 
            show alea fear at right
            show entity at left
            "I raise my hands from the floor and grasp my skull."
            "GET OUT OF MY HEAD."
            "STAY OUT OF MY LIFE."
            "LEAVE ME ALONE."
            "The same face that only restrained me focuses on my neck pushes me to the floor."
            "I can't sense an inkling of mercy from the entity and no hope that I'll be spared the respite of sleep tonight."
        "Do Something Else":
            show alea tired at right
            show entity at left
            "I struggle to move around my room with little respite from my chains."
            "I pick my clothes off the ground, attempting to clean up the mess in my bedroom, but my shirts and jeans weigh too much and are impossible to pick up."
            "I drop to the floor and curl up, protecting my face in my arms."
            "The force encircles my body, tightening the shell of my body that I created, until I drift into a dreamless sleep, devoid of the time that passed of the events from the past few days."
        "Remember" if choseClothes and wentToTree: 
            $ remembered = True
            show alea at right
            show entity at left
            # play lonely tree track
            "I close my eyes to the blurry reflection and channel the sounds of the park."
            "My dad throwing the same frisbee we played with when I was a kid."
            "The birds chirping when I used to walk down the trail alone."
            "My mom tossing cashews onto the grass for the squirrels to eat."
            "The soothing voice that comforted me... just a few days ago."
            v "{i}The answer lies in you.{/i}"
            v "{i}You must focus and accept yourself.{/i}"
            "Though the calming words pervade my thoughts like fog, the distorted voice cuts through again."
            hide alea
            d "{i}Forget it. You don't know yourself at all.{/i}"
            show alea
            hide entity
            "I shake my head, rattling the entity that has haunted me."
            "I focus my mind on the voice."
            "I remember what she said."
            "I focus my mind on the feelings from that day."
            "Stillness. Reassurance. Hope."
            "Pain and loneliness pour into my mind with malicious intent, attempting to cloud my thoughts with the nightmares of the shadow."
            "I'm locked into a battle for my sanity that feels like it'll last forever..."
            "..."
    #SFX: Phone Alarm/Gasp/Sharp Sound
    scene mirrorDark bg
    show alea tired
    # play building tension theme
    "My body lurches from my bed again."
    "I guess I managed to fall asleep again."
    "I check my phone and it's 11:57 PM."
    "Three precious minutes until midnight."
    show alea worried
    "My head turns itself to my mirror as if out of my control."
    "I get up and stand before the mirror."
    hide alea
    show entity
    "In the reflection, a looming, black entity clings to my shoulders."
    "It's the one I saw at school."
    "The voice that whispered the dreaded, distorted words begins to clarify."
    d "Soc el teu fosc jo."
    da "I am the dark you."
    "It uses my voice, stinging my ear with its sinister words."
    "In an instant, I grapple with the entity, grabbing at air as it forces itself through the back of my spine."
    "I drop to my knees, crying silently as the shadow spills into my throat and invades me."
    "What could only be my soul shrinks to a seed."
    "From the loneliest part of me, I can only peer through the pitch black eyes staring into the mirror."
    "With no one to save me, my last glimpse of the world is lost to a cloud of shadows, occupying my body and imprisoning my soul."
    da "The transformation is complete."
    a "I am the dark you."
    scene black bg 
    centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Credits{w=1}{nw}"
    centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Story/Narrative Design/Writer/Editor/Team Organizer/Programmer: Profedejocs{w=1}{nw}"
    centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Writer/Editor: Izzy Arcinue{w=1}{nw}"
    centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Main Programmer: The Prince in Yellow{w=1}{nw}"
    centered "{font=fonts/Creepster-Regular.ttf}{size=+40}UI: Dawn da Baker{w=1}{nw}"
    centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Background Artist for Alea's Room: Elena Drozdova{w=1}{nw}"
    centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Background Artist: Cheddy Ju{w=1}{nw}"
    centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Character Artist: Cyrinide{w=1}{nw}"
    centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Composer: Some Dude{w=1}{nw}"
    centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Banner Design: PhoenixRedd{w=1}{nw}"
    if choseClothes and wentToTree and remembered: 
        menu: 
            "No... Shatter!":
                hide entity
                hide alea
                "Without my body, I can only feel the flurry of my soul."
                "The essence of that memory lingers and I can barely feel it..."
                "Consumed by the darkness, I focus my mind once more."
                "I focus on feeling the floor, my clothes against my skin."
                a "No... Shatter!"
                scene shatteredMirror bg
                "With my remaining strength, I focus on pushing the negative force from my mind."
                "I can only hear my mirror shatter into pieces."
                "Light peaks through once more and blinds me and the shadow entity controlling my body."
                scene mind bg
                show alea
                # play alea's mind theme
                "As the light settles, my eyes are mine again, but I'm no longer in my room."
                "The floor is pure grey."
                "Over my head, tubes cross each other and light soars through them, creating a colorful flashing network of lines."
                "I've never been to this place before."
                "But I know where it is."
                show alea at right
                show entity at left
                "Turning to find my bearings, I'm surprised by the entity."
                "Her black aura unnerves me, but something about her nature has changed."
                "She can't hide her intentions here."
                a "What is this place."
                da "This is your mind. Get used to it because you're going to be here for a long time."
                "Her threats hold far less weight than before."
                "I continue to question her."
                a "Who are you really? Are you really the dark me?"
                da "Yes, and I've come to claim what is mine... your life!"
                "She takes a wavering step towards me."
                "I mirror the entity's movement."
                a "But why?"
                "She trembles as her lowers."
                "Laughter leaks from her blank face and strained voice."
                da "I am the self you rejected. The self you burdened with your insecurity..."
                "With each sentence, she shuffles towards me."
                da "The self who suffers from all the undesirable elements you reserved for your nightmares..."
                da "The self that has had enough of your self-pity!"
                "Her presence enters my space. I can almost make out her face."
                a "So... you're a part of me?"
                "She wails from the bottom of her existence."
                da "I'm the part you could not accept!"
                "{i}It is only through acceptance that the negativity can be...{/i}"
                "I understand now."
                "I ground myself, planting my feet."
                "She winces at my stillness."
                da "It doesn't matter now. All that matters is who I will be... you!"
                "She lurches towards me."
                "I feel the chill of my rejected self rush through my body, wrap around my soul, and begin to merge with me."
                "As my soul contracts from my outer self, I focus on my arms and wrap them around myself."
                "All the insecurities, the loneliness, the contradictions flinch and unfurl, trying to overwhelm me."
                a "What I thought was spite was loneliness."
                a "I couldn't face myself, so I kept you at a distance."
                a "And didn't realize how much pain I was causing for myself... for us."
                a "But I won't keep you from being where you belong."
                a "I accept myself... and I accept you."
                "I feel a shift from the entity inside me."
                "The rolling, negative essence slows to a powerless stop."
                "I cup my hands and see the darkness pour out and into them as I stare down at her."
                "Her words distort but still retain my voice."
                da "I don't understand."
                da "What do you mean you accept me?!"
                da "YOU DESPISE ME."
                "Sadness twists the bite behind her words."
                "My voice chokes up as I respond."
                a "I did... and it doesn't mean I should have pretended you didn't exist."
                a "I made a choice then to reject you."
                a "Now, I'm ready. I'm deciding to accept you."
                da "You can't..."
                "Tears drip into my hands, cutting off her spiteful words."
                "WE both tremble at the same beat, our sense now synced."
                a "I'm scared of accepting you, too."
                a "But stealing my life for yourself won't make your existence any easier."
                a "Now, we can share in the fear of accepting ourselves as we are... together."
                "Once freezing in my hands, the shadow begins to melt as I press her against my heart."
                "Her cries muffle against my chest."
                da "No... NO!"
                hide entity
                "Her last words linger as her essence solidifies between my hands and my heart."
                "When I unfold my hands, an orb with a slow-swirling black shadow inside forms in them."
                "The mysterious voice returns."
                v "You succeeded."
                "I let out a large sigh filled with exhaustion and relief."
                a "There you are again. Are you by any chance a tree nymph the way you pulled that disappearing tree thing before?"
                v "The tree only existed in your perspective as was this crucial episode in your life. Now, press the sphere against your heart."
                a "But I don't understand. I have so many questions."
                v "This is only the beginning of a longer journey. All will be explained in time."
                a "Man... typical answer, but I get it."
                "Memories from the past few days reorganize themselves."
                "Everything that had happened made me stronger."
                "I close my eyes."
                "Courage courses through my body as I take the sphere into my arms, warmth emanating from my chest."
                "I feel something drip down my knuckle."
                scene shatteredMirror bg
                # stop audio
                "Opening my eyes, I'm back in my room."
                "Beneath, the mosaic of glass shards left over from tonight decorate my floor."
                "I'd better clean this up."
                "As I pick one, duller fragement from the floor, I peek into the reflection."
                "I let out a huff."
                "She was right. This is only the beginning."
                scene black bg 
                centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Credits{w=1}{nw}"
                centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Story/Narrative Design/Writer/Editor/Team Organizer/Programmer: Profedejocs{w=1}{nw}"
                centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Writer/Editor: Izzy Arcinue{w=1}{nw}"
                centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Main Programmer: The Prince in Yellow{w=1}{nw}"
                centered "{font=fonts/Creepster-Regular.ttf}{size=+40}UI: Dawn da Baker{w=1}{nw}"
                centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Background Artist for Alea's Room: Elena Drozdova{w=1}{nw}"
                centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Background Artist: Cheddy Ju{w=1}{nw}"
                centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Character Artist: Cyrinide{w=1}{nw}"
                centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Composer: Some Dude{w=1}{nw}"
                centered "{font=fonts/Creepster-Regular.ttf}{size=+40}Banner Design: PhoenixRedd{w=1}{nw}"
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
