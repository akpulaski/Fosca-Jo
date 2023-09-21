# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alea Tori")


# The game starts here.

label start:

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
    scene park bg 
    "My feet walk me to call, but I am not moving them."
    "If I could just remember what was in that dream."
    scene schoolHallway bg
    menu: 
        "Ignore.": 
            "Best if I just ignore it."
            "My five, futile minutes disappear as I walk into the classroom."
            "I rub my exhausted, throbbing head. I even start swatting at the whisper floating around my mind."
        "Keep Thinking.": 
            "I mouth the words."
            "I lift my head and recit it aloud: {i}Fosc jo.{/i}"
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
        "Have Lunch.": 
            "I walk into the cafeteria after class."
            "Sitting alone at a table, I stare at the uninspiring chick sanwich on my tray."
            # art: put the looming transparent entity in the background
            "But I don't think I have the appetite right now."
            "I think I'll skip lunch today."
        "Go to Studay Hall.": 
            "Maybe I just don't have the appetite for the cafeteria's uninspiring chicken sandwiches."
            "I quickly exit the room and walk opposite my classmates while they head to get lunch."
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
    "I throw my backpack to the floor and lie face down on my bed, taking a pillow into my arms and burying my face into it."
    "Another day wasted thinking about this silly dream."
    "{i}Fosc jo{/i}."
    # art: put a transparent figure on a chair in the background.
    "Am I seeing things?"
    "I sit up from my bed, pushing myself off the pillow."
    "The chair is empty."
    menu: 
        "Ignore.": 
            "There's nothing there, I tell myself."
            "It's all just in my head."
            "I shoudl at least try to get some sleep. I lower myself back into my pillow."
            # audio: object falling to the floor.
            scene book bg
            "It was just a book. I must have left it hanging from my desk."
        "Go and Look.": 
            "I move my legs off the bed and sit at the edge."
            "I run my hand across the chair."
            "My mind must be playing tricks."
            "I'm creeping myself out."
            "There's no one here, but I could've sworn that today someone was following me."
            "But there's no point in dwelling on it when I'm alone in my bedroom."
            "I really want to sleep."
            "It's all in my head. It's all in my head."
            "It's all in my head. I repeat it until my eyes flutter shut and I drift away, back into the dark."
            # art: put a transparent, mysterious figure sitting on a chair in the background. 
    jump october_29th


label october_29th: 
    return