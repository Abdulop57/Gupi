import asyncio
import contextlib
import random
from typing import Any, Dict, Union
from importlib.machinery import ModuleSpec
from click.decorators import pass_context
from highrise import BaseBot
from typing import Any, Dict, Union
from highrise import *
from highrise.models import *
from asyncio import Task
from highrise.__main__ import *
from highrise.models import (
    AnchorPosition,
    Item,
    Position,
    SessionMetadata,
    User,
)
from highrise.models import (
    CurrencyItem,
    GetMessagesRequest,
    Item,
    SessionMetadata,
)
import random
import requests
import os
import importlib
import asyncio
import contextlib
import logging
import time
from highrise import BaseBot, AnchorPosition, Position, User, TaskGroup

class MyBot(BaseBot):

    def __init__(self):
        super().__init__()
        self.user_data = {}
        self.commands = {
            "/F1": (Position(12.5, 4.5, 27.5), "First Floor"),
            "/F2": (Position(6, 9.5, 8.5), "Second Floor")
        }
        

  
    continuous_emote_tasks: Dict[int, asyncio.Task[Any]] = {}  
    user_data: Dict[int, Dict[str, Any]] = {}
    EMOTE_DICT = {
            "1"        : "idle-enthusiastic",
      "2"     : "emote-fashionista",
      "3"            : "emoji-flex",
      "4"      : "emote-lust",
      "5"           : "emote-float",
      "6"            : "emote-frog",
      "7"      : "dance-weird",
      "8"         : "emote-gravity",
      "9"          : "emote-greedy",
      "10"           : "emote-hello",
      "11"             : "emote-hot",
      "12"        : "dance-icecream",
      "13"            : "emote-kiss",
      "14"            : "dance-blackpink",
      "15"           : "emote-superpose",
      "16"           : "emote-laughing",
      "17"          : "dance-shoppingcart",
      "18"          : "emote-maniac",
      "19"           : "emote-model",
      "20"              : "emote-no",
      "21"         : "dance-macarena",
      "22"      : "dance-pennywise",
      "23"           : "emote-pose1",
      "24"           : "emote-pose3",
      "25"           : "emote-pose5",
      "26"           : "emote-pose7",
      "27"           : "emote-pose8",
      "28"      : "emote-punkguitar",
      "29"       : "emoji-celebrate",
      "30"         : "dance-russian",
      "31"             : "emote-sad",
      "32"          : "dance-tiktok8",
      "33"         : "dance-tiktok10",
      "34"             : "emote-shy",
      "35"       : "idle_singing",
      "36"             : "idle-loop-sitfloor",
      "37"       : "emote-snowangel",
      "38"        : "emote-snowball",
      "39"      : "emote-swordfight",
      "40"     : "emote-telekinesis",
      "41"        : "emote-teleporting",
      "42"        : "emoji-thumbsup",
      "43"           : "emote-tired",
      "44"       : "emoji-gagging",
      "45"           : "dance-tiktok9",
      "46"            : "emote-wave",
      "47"           : "dance-weird",
      "48"            : "emote-snake",
      "49"           : "dance-wrong",
      "50"             : "emote-yes",
      "51"       : "emote-zombierun",
      "52"           : "idle-dance-tiktok4",
      "53"             : "idle-uwu",
      "54"            : "emote-shy2",
      "55"            : "emote-astronaut",
      "56"            : "dance-anime",
      "57"            : "idle-guitar",
      "58"      : "emote-headblowup",
      "59"           : "dance-creepypuppet",
      "60"       : "emote-creepycute",
      "61" : "dance-pinguin",
      "62" : "emote-sleigh",
      "63" : "emote-hyped",
      "64" : "dance-jinglebell", 
      "65" : "idle-nervous",
      "66" : "idle-toilet",
      "67" : "emote-timejump",
      "68" : "sit-relaxed",
      "69" : "dance-kawai" , 
      "70" : "idle-wild" ,
      "71" : "emote-iceskating",
      "72": "emote-launch",
      "angry"           : "emoji-angry",
      "bow"             : "emote-bow",
      "casual"          : "idle-dance-casual",
      "charging"        : "emote-charging",
      "confusion"       : "emote-confused",
      "cursing"         : "emoji-cursing",
      "curtsy"          : "emote-curtsy",
      "cutey"           : "emote-cutey",
      "dont"            : "dance-tiktok2",
      "emotecute"       : "emote-cute",
      "energyball"      : "emote-energyball",
      "enthused"        : "idle-enthusiastic",
      "fashionista"     : "emote-fashionista",
      "flex"            : "emoji-flex",
      "flirtywave"      : "emote-lust",
      "float"           : "emote-float",
      "frog"            : "emote-frog",
      "gravedance"      : "dance-weird",
      "gravity"         : "emote-gravity",
      "greedy"          : "emote-greedy",
      "hello"           : "emote-hello",
      "hot"             : "emote-hot",
      "icecream"        : "dance-icecream",
      "kiss"            : "emote-kiss",
      "kpop"            : "dance-blackpink",
      "lambi"           : "emote-superpose",
      "laugh"           : "emote-laughing",
      "letsgo"          : "dance-shoppingcart",
      "maniac"          : "emote-maniac",
      "model"           : "emote-model",
      "no"              : "emote-no",
      "ogdance"         : "dance-macarena",
      "pennydance"      : "dance-pennywise",      
      "pose1"           : "emote-pose1",
      "pose2"           : "emote-pose3",
      "pose3"           : "emote-pose5",
      "pose4"           : "emote-pose7",
      "pose5"           : "emote-pose8",
      "punkguitar"      : "emote-punkguitar",
      "raisetheroof"    : "emoji-celebrate",
      "russian"         : "dance-russian",
      "sad"             : "emote-sad",
      "savage"          : "dance-tiktok8",
      "shuffle"         : "dance-tiktok10",
      "shy"             : "emote-shy",
      "singalong"       : "idle_singing",
      "sit"             : "idle-loop-sitfloor",
      "snowangel"       : "emote-snowangel",
      "snowball"        : "emote-snowball",
      "swordfight"      : "emote-swordfight",
      "telekinesis"     : "emote-telekinesis",
      "teleport"        : "emote-teleporting",
      "thumbsup"        : "emoji-thumbsup",
      "tired"           : "emote-tired",
      "tummyache"       : "emoji-gagging",
      "viral"           : "dance-tiktok9",
      "wave"            : "emote-wave",
      "weird"           : "dance-weird",
      "worm"            : "emote-snake",
      "wrong"           : "dance-wrong",
      "yes"             : "emote-yes",
      "zombierun"       : "emote-zombierun",
      "ANGRY"           : "emoji-angry",
      "BOW"             : "emote-bow",
      "CASUAL"          : "idle-dance-casual",
      "CHARGING"        : "emote-charging",
      "CONFUSION"       : "emote-confused",
      "CURSING"         : "emoji-cursing",
      "CURTSY"          : "emote-curtsy",
      "CUTEY"           : "emote-cutey",
      "DONT"            : "dance-tiktok2",
      "EMOTECUTE"       : "emote-cute",
      "ENERGYBALL"      : "emote-energyball",
      "ENTHUSED"        : "idle-enthusiastic",
      "FASHIONISTA"     : "emote-fashionista",
      "FLEX"            : "emoji-flex",
      "FLIRTYWAVE"      : "emote-lust",
      "FLOAT"           : "emote-float",
      "FROG"            : "emote-frog",
      "GRAVEDANCE"      : "dance-weird",
      "GRAVITY"         : "emote-gravity",
      "GREEDY"          : "emote-greedy",
      "HELLO"           : "emote-hello",
      "HOT"             : "emote-hot",
      "ICECREAM"        : "dance-icecream",
      "KISS"            : "emote-kiss",
      "KPOP"            : "dance-blackpink",
      "LAMBI"           : "emote-superpose",
      "LAUGH"           : "emote-laughing",
      "LETSGO"          : "dance-shoppingcart",
      "MANIAC"          : "emote-maniac",
      "MODEL"           : "emote-model",
      "NO"              : "emote-no",
      "OGDANCE"         : "dance-macarena",
      "PENNYDANCE"      : "dance-pennywise",
      "POSE1"           : "emote-pose1",
      "POSE2"           : "emote-pose3",
      "POSE3"           : "emote-pose5",
      "POSE4"           : "emote-pose7",
      "POSE5"           : "emote-pose8",
      "PUNKGUITAR"      : "emote-punkguitar",
      "RAISETHEROOF"    : "emoji-celebrate",
      "RUSSIAN"         : "dance-russian",
      "SAD"             : "emote-sad",
      "SAVAGE"          : "dance-tiktok8",
      "SHUFFLE"         : "dance-tiktok10",
      "SHY"             : "emote-shy",
      "SINGALONG"       : "idle_singing",
      "SIT"             : "idle-loop-sitfloor",
      "SNOWANGEL"       : "emote-snowangel",
      "SNOWBALL"        : "emote-snowball",
      "SWORDFIGHT"      : "emote-swordfight",
      "TELEKINESIS"     : "emote-telekinesis",
      "TELEPORT"        : "emote-teleporting",
      "THUMBSUP"        : "emoji-thumbsup",
      "TIRED"           : "emote-tired",
      "TUMMYACHE"       : "emoji-gagging",
      "VIRAL"           : "dance-tiktok9",
      "WAVE"            : "emote-wave",
      "WEIRD"           : "dance-weird",
      "WORM"            : "emote -snake",
      "WRONG"           : "dance-wrong",
      "YES"             : "emote-yes",
      "ZOMBIERUN"       : "emote-zombierun",  
      "Angry"           : "emoji-angry",
      "Bow"             : "emote-bow",
      "Casual"          : "idle-dance-casual",
      "Charging"        : "emote-charging",
      "Confusion"       : "emote-confused",
      "Cursing"         : "emoji-cursing",
      "Curtsy"          : "emote-curtsy",
      "Cutey"           : "emote-cutey",
      "Dont"            : "dance-tiktok2",
      "Emotecute"       : "emote-cute",
      "Energyball"      : "emote-energyball",
      "Enthused"        : "idle-enthusiastic",
      "Fashionista"     : "emote-fashionista",
      "Flex"            : "emoji-flex",
      "Flirtywave"      : "emote-lust",
      "Float"           : "emote-float",
      "Frog"            : "emote-frog",
      "Gravedance"      : "dance-weird",
      "Gravity"         : "emote-gravity",
      "Greedy"          : "emote-greedy",
      "Hello"           : "emote-hello",
      "Hot"             : "emote-hot",
      "Icecream"        : "dance-icecream",
      "Kiss"            : "emote-kiss",
      "Kpop"            : "dance-blackpink",
      "Lambi"           : "emote-superpose",
      "Laugh"           : "emote-laughing",
      "Letsgo"          : "dance-shoppingcart",
      "Maniac"          : "emote-maniac",
      "Model"           : "emote-model",
      "No"              : "emote-no",
      "Ogdance"         : "dance-macarena",
      "Pennydance"      : "dance-pennywise",
      "Pose1"           : "emote-pose1",
      "Pose2"           : "emote-pose3",
      "Pose3"           : "emote-pose5",
      "Pose4"           : "emote-pose7",
      "Pose5"           : "emote-pose8",
      "Punkguitar"      : "emote-punkguitar",
      "celebrate"       : "emoji-celebrate",
      "Russian"         : "dance-russian",
      "Sad"             : "emote-sad",
      "Savage"          : "dance-tiktok8",
      "Shuffle"         : "dance-tiktok10",
      "Shy"             : "emote-shy",
      "Singalong"       : "idle_singing",
      "Sit"             : "idle-loop-sitfloor",
      "Snowangel"       : "emote-snowangel",
      "Snowball"        : "emote-snowball",
      "Swordfight"      : "emote-swordfight",
      "Telekinesis"     : "emote-telekinesis",
      "Teleport"        : "emote-teleporting",
      "Thumbsup"        : "emoji-thumbsup",
      "Tired"           : "emote-tired",
      "Tummyache"       : "emoji-gagging",
      "wing"            : "emote-wings",
      "Viral"           : "dance-tiktok9",
      "Wave"            : "emote-wave",
      "Weird"           : "dance-weird",
      "Worm"            : "emote-snake",
      "Wrong"           : "dance-wrong",
      "Yes"             : "emote-yes",
      "Zombierun"       : "emote-zombierun",
      "sayso"           : "idle-dance-tiktok4",
      "Sayso"           : "idle-dance-tiktok4",
      "SAYSO"           : "idle-dance-tiktok4",
      "uwu"             : "idle-uwu",
      "UWU"             : "idle-uwu",
      "bash"            : "emote-shy2",
      "Zero"            : "emote-astronaut",
      "zero"            : "emote-astronaut",
      "bashfull"            : "emote-shy2",
      "Bashfull"         : "emote-shy2",
      "anime"            : "dance-anime",
      "Anime"            : "dance-anime",
      "airguitar"        : "idle-guitar",
      "Airguitar"        : "idle-guitar",
      "revelations"      : "emote-headblowup",
      "revelation"      : "emote-headblowup",
      "Revelations"      : "emote-headblowup",
      "creepy"           : "dance-creepypuppet",
      "Creepy"           : "dance-creepypuppet",
      "creepycute"       : "emote-creepycute",
      "Creepycute"       : "emote-creepycute",
      "penguin" : "dance-pinguin",
      "Penguin" : "dance-pinguin",
      "sleigh" : "emote-sleigh",
      "Sleigh" : "emote-sleigh",
      "hyped" : "emote-hyped",
      "Hyped" : "emote-hyped",
      "jingle" : "dance-jinglebell", 
      "Jingle" : "dance-jinglebell", 
      "nervous" : "idle-nervous",
      "Nervous" : "idle-nervous",
      "gottago" : "idle-toilet",
      "Gottago" : "idle-toilet",
      "Timejump" : "emote-timejump",
      "timejump" : "emote-timejump",
      "repose" : "sit-relaxed",
      "Repose" : "sit-relaxed",
      "kawaii" : "dance-kawai" , 
      "Kawaii" : "dance-kawai" , 
      "scritchy" : "idle-wild" ,
      "Scritchy" : "idle-wild" ,
      "skating" : "emote-iceskating",
      "Skating " : "emote-iceskating",
      "touch" : "dance-touch",
      "Touch" : "dance-touch",
      "pushit" : "dance-employee" ,
      "Pushit" : "dance-employee" ,
      "gift" : "emote-gift",
      "Gift" : "emote-gift",
      "launch": "emote-launch",
      "Launch": "emote-launch",
      "wop" : "dance-tiktok11",
      "Wop" : "dance-tiktok11",
      
    }

      

   # Define your available items list
    emote_durations = {
      "rest": 17.062613, "zombie": 28.754937, "relaxed": 21.546653, "attentive": 24.585168, "this is for you": 6,
    "sleepy": 22.620446, "pouty face": 24.377214, "posh": 21.851256, "tap loop": 6.261593, "push it": 7.9,
    "sit": 22.321055, "shy": 4.477567, "bummed": 6.052999, "chillin'": 18.798322, "celebrating": 2.8,
    "annoyed": 17.058522, "aerobics": 8.507535, "ponder": 22.339865, "hero pose": 21.877099, "sweet smooch": 5,
    "relaxing": 17.253372, "cozy nap": 13.935264, "enthused": 15.941537, "boogie swing": 13.198551, 
    "feel the beat": 25.367458, "irritated": 25.427848, "yes": 2.565001, "i believe i can fly": 13.134487, 
    "the wave": 2.690873, "tired": 4.61063, "think": 3.691104, "theatrical": 8.591869, 
    "tap dance": 11.057294, "super run": 6.273226, "super punch": 3.751054, "sumo fight": 10.868834,
    "thumb suck": 4.185944, "splits drop": 4.46931, "snowball fight!": 5.230467, "snow angel": 6.218627,
    "secret handshake": 3.879024, "sad": 5.411073, "rope pull": 8.769656, "russian dance": 10,
    "roll": 3.560517, "rofl!": 6.314731, "robot": 7.607362, "rainbow": 2.813373, 
    "proposing": 4.27888, "peekaboo!": 3.629867, "peace": 5.755004, "panic": 2.850966, 
    "no": 2.703034, "ninja run": 4.754721, "night fever": 5.488424, "monster fail": 4.632708,
    "model": 6.490173, "flirty wave": 4.655965, "level up!": 6.0545, "amused": 5.056641, 
    "laugh": 1.9, "kiss": 2.387175, "super kick": 4.867992, "jump": 3.584234, "boxer": 5,
    "judo chop": 2.427442, "imaginary jetpack": 16.759457, "hug yourself": 4.992751, "sweating": 4.353037,
    "hero entrance": 4.996096, "hello": 2.734844, "headball": 10.073119, "harlem shake": 13.558597, 
    "happy": 3.483462, "handstand": 4.015678, "greedy emote": 4.639828, "graceful": 3.7498, 
    "moonwalk": 8.052307, "gangnam style": 7.275486, "frolic": 3.700665, "faint": 18.423499, 
    "clumsy": 6.475972, "fall": 5.617942, "face palm": 2.722748, "exasperated": 2.367483,
    "elbow bump": 3.799768, "disco": 5.366973, "blast off": 6.195985, "faint drop": 3.762728, 
    "collapse": 4.855549, "revival": 6.615967, "dab": 2.717871, "curtsy": 2.425714, 
    "confused": 8.578827, "cold": 3.664348, "charging": 8.025079, "bunny hop": 12.380685, 
    "bow": 3.344036, "boo": 4.501502, "home run!": 7.254841, "falling apart": 4.809542,
    "thumbs up": 2.702369, "point": 2.059095, "sneeze": 2.996694, "smirk": 4.823158, 
    "sick": 5.070367, "gasp": 3.008487, "punch": 1.755783, "pray": 4.503179,
    "stinky": 4.795735, "naughty": 4.277602, "mind blown": 2.397167, "lying": 6.313748,
    "levitate": 5.837754,
      "fireball lunge": 2.723709, 
      "give up": 5.407888, 
      "tummy ache": 5.500202,  
  
      "flex": 2.099351, 
      "stunned": 4.053049,
      "cursing": 2.382069,
      "sob": 3.696499,
    
      "clap": 2.161757, 
      "raise the roof": 3.412258,
      "arrogance": 6.869441, 
      "vogue hands": 9.150634,
   
      "savage dance": 10.938702, 
      "don't start now": 10.392353, 
      "yoga flow": 15.795092, 
      "smoothwalk": 6.690023,
   
      "ring on it": 21.191372, 
      "letsgo": 4.316035, 
      "robotic": 17.814959, 
      "pennydance": 1.214349, 
      "macarena": 12.214141,
    
      "hands in the air": 22.283413, 
      "floss": 21.329661, 
      "duck walk": 11.748784, 
      "breakdance": 17.623849,
    
      "kpop": 7.150958, 
      "push ups": 8.796402, 
      "hyped": 7.492423, 
      "jingle": 10.958832,
    
      "nervous": 21.714221, 
      "gottago": 32.174447, 
      "attention": 4.401206, 
      "zero": 13.791175,
  
      "dance zombie": 12.922772, 
      "ghost": 3.472759, 
      "heart eyes": 4.034386, 
      "swordfight": 5.914365,
   
      "timejump": 4.007305, 
      "worm": 5.262578, 
      "heart fingers": 4.001974, 
      "heart shape": 6.232394,
   
      "hug": 3.503262,
      "eyeroll": 3.020264, 
      "embarrassed": 7.414283,
    
      "float": 8.995302, 
      "telekinesis": 10.492032, 
      "sexy dance": 12.30883,
      "puppet": 16.325823,
    
      "fighter idle": 17.1, 
      "penguin": 11.5, 
      "creepypuppet": 6.4, 
      "sleigh": 11.3,
    "maniac": 4.9, 
      "energyball": 7.5, 
      "singing": 10.2, 
      "frog": 14.5,
    
      "superpose": 4.5, 
      "tiktok dance 9": 11.8,
      "weird": 21.5,
    "tiktok10": 10, 
      "pose 7": 4.6,
      "pose 8": 4.8, 
      
      "casual": 9,
   
      "pose 1": 2.8, 
      "pose 3": 5.1, 
      "pose 5": 4.6, 
      "cutey": 3.2, 
      "cute": 6.1,
    "punkguitar": 9.3, 
      "zombierun": 9.1, 
      "fashionista": 5.6, 
      "gravity": 8.9,
    
      "icecream": 14.7, 
      "wrong": 12.4, 
      "uwu": 24.7,
      "tiktok dance 4": 15.5,
   
      "shy": 4.9,
      "anime": 8.4,
      "kawaii": 11.2,
      "scritchy": 26.4,
    
      "skating": 7.2, 
      "surprise": 5.3, 
      "celebration": 3.3, 
      "creepycute": 7.9,
   
      "frustrated": 5.5, 
      "pose 10": 3.9, 
      "dont": 12,
   
      "star gazing": 1.1,
      "head blowup": 11.6,
   
      "repose": 24,
      "tiktok7": 13, 
      "shrink": 8.7,
      "angry": 6,
    "ditzy pose": 4, 
      "teleport": 11, 
      "touch": 12,
 "airguitar": 13.2
  }

    
  








    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("alive")
        await self.highrise.walk_to(Position(3.5, 14, 1.5, "FrontRight"))


        self.allowed_usernames = [ "Mr.jawaan", "GUPI_" , "nubi.bean", "Reedolf", "lalaapo" ]




    async def send_periodic_message(self):
        try:
            while True:
                MESSAGES = ["Type /rent if you want to rent a bot🤖!!!","Welcome to SOEFAM party and tip room! Enjoy the music. Don't forget follow the host and vips❤️‍🔥", "Welcome to SOEFAM party and tip room! We hope you enjoy the room and  music #TIBA2PARTY. No begging and spamming. Make a good vibes and respect one another.", "Hello Thank you for dropping by! This is SOEFAM tip room. We hope you enjoy the room and music.", "FOLLOW THE HOST @GUPI_ 🔥", "You define your own life. Don't let other people write your script.", "Do you believe in love at first sight, or should I walk by again?","Is your name Google? Because you have everything I've been searching for.","Are you a magician? Whenever I look at you, everyone else disappears.","Do you have a map? I keep getting lost in your eyes.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","I must be a snowflake because I've fallen for you.","Excuse me, but I think you dropped something: my jaw.", "Like a rose in full bloom, your beauty captivates me, leaving me breathless and longing for your tender embrace. ","If i had to wait my entire life for your love, i would. When i’ve withered away, I’d be glad i got to experience heaven before i reached it."]
                message = random.choice(MESSAGES)
                await self.highrise.chat(message)
                await asyncio.sleep(60) # 2 minutes
        except Exception as e:
            print(f"An exception occurred: {e}")

        

        


  

        
        

        
        

        

        
            # Add more item IDs as needed

        

        
            

        


    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
        response = await self.highrise.get_messages(conversation_id)
        message = "" 

        if isinstance(response, GetMessagesRequest.GetMessagesResponse):
            if response.messages:
                message = response.messages[0].content
                print(f"Received message: {message}")

        if message:
            print("Condition met: message is not empty")

            if message.lower() == "hello":
              print("Message is 'Hello', responding with commands...")

              response = [
        "HI! 🤗",
        "Thankyou for messaging 💓",
        "Type !help for more info..."
    ]

              for command in response:
                    print(f"Sent command: {command}")
                    await self.highrise.send_message(conversation_id, command)



            elif message.lower() == "list":
                print("Message is 'list', responding with command list...")

                command_list = [
                "Here is the list of commands...",
                "✅Emotelist",
                "✅Poeticrizz",
                "✅Rizz",
                "✅Joke",
                "✅Roastme",
                "✅Funfact",
                "✅Deathyear",
                "✅Lovepercentage",
                "✅Hatepercentage",
                "✅Iq",
                "✅straightmeter",
                
                "YOU CAN USE THIS COMMANDS IN ROOM CHAT🤖"
            ]
                for command in command_list:
                    await self.highrise.send_message(conversation_id, command)
                    print(f"Sent command: {command}")

            elif message.lower() == "emotelist":
                print("Message is 'emotelist', responding with emotelist...")

                emotelist = "Here is the emotelist...\n" \
                        "angry, bow, casual, raisetheroof, charging, confusion, cursing, curtsy, cutey, dont, " \
                        "emotecute, energyball, enthused, fashionista, flex, flirtywave, float, frog, gravedance, " \
                        "gravity, greedy, hello, hot, icecream, kiss, kpop, lambi, laugh, letsgo, maniac, model, no, " \
                        "ogdance, pennydance, pose1, pose2, pose3, pose4, pose5, punkguitar, russian, sad, savage, " \
                        "shuffle, shy, singalong, sit, snowangel, snowball, swordfight, telekinesis, teleport, " \
                        "thumbsup, tired, tummyache, viral, wave, weird, worm, yes, zombierun, airguitar, revelations, " \
                        "creepy, creepycute, penguin, sleigh, hyped, jingle, nervous, gottago, repose, kawaii, scritchy,touch, gift, pushit " \
                        "skating "
                await self.highrise.send_message(conversation_id, emotelist)

            elif message.lower() == "!help":
                print("Message is '!help', responding...")

                commands = [
                "Here is the list of commands...",
                "list",
                "Emotelist",
              
                ]


                for command in commands:
                    await self.highrise.send_message(conversation_id, command)




            elif message == "I love you":
                await self.highrise.send_message(conversation_id, "I love me too")

            if message.startswith("mod"):
                await self.highrise.send_message(conversation_id,
    "\ncommands for mods😸" 
    "\n/mod for self use"
    "\nvip1,2,3 @username" 
    "\ndown @username" 
    "\n /vip1,2,3 ,/f1 , /down for self teleport."
    "\nwallet to check the bot wallet."
    "\n/giveme <amount> To withdraw gold from the bot (use this command in WHISPER."
    "\n type 1-73 for use emote solo time.  "
    "\n"
    "\nHere the list of emote all try in room chat.🤖"
    "\n/fashionista" 
    "\n/shuffle" 
    "\n/worm" 
    "\n/singalong"
    "\n/russian"
    "\n/hyped"
    "\n/jingle" 
    "\n/gottago" 
    "\n/penguin" 
    "\n/anime" 
    "\n/zero" 
    "\n/dont" 
    "\n/punkguitar" 
    "\n/weird" 
    "\n/sayso" 
    "\n/frog" 
    "\n/zombie" 
    "\n/kawaii" 
    "\n/scritchy" 
    "\n/skating"
    "\n/launch"
    "\n/wop"
    "\n/flirtywave"
    "\nyou can use this emotes for all"
    "\nBot Created By @Mr.jawaan")



  
    

    
            




    async def follow_user(self, target_username: str):
        while self.allowed_usernames == target_username:
        # ابحث عن موقع المستخدم المستهدف في الغرفة
            response = await self.highrise.get_room_users()
            target_user_position = None
            for user_info in response.content:
                if user_info[0].username.lower() == target_username.lower():
                    target_user_position = user_info[1]
                    break

            if target_user_position:
                nearby_position = Position(target_user_position.x + 1.0, target_user_position.y, target_user_position.z)
                await self.highrise.walk_to(nearby_position)

                await asyncio.sleep(1)
        


            


    async def on_user_join(self, user: User, position: Union[Position, AnchorPosition]) -> None:
      privileges = await self.highrise.get_room_privilege(user.id)
      print(f"{user.username} joined the room with the privileges {privileges}")
      await self.highrise.react("wave", user.id)
      await self.highrise.react("heart", user.id)
      await self.highrise.react("clap", user.id)
      await self.highrise.react("wink", user.id)

      wm = ["Welcome to SOEFAM party and tip room! Enjoy the music. Don't forget follow the host and vips", "Hello,  Thank you for dropping by! This is SOEFAM tip room. We hope you enjoy the room and music.", "Welcome to SOEFAM party and tip room! We hope you enjoy the room and  music #TIBA2PARTY. No begging and spamming. Make a good vibes and respect one another."]
      ywm = random.choice(wm)

      await self.highrise.chat(f"{user.username}  {ywm}")
      

# print(f"{user.username} joined the room standing at {position}")
      await self.highrise.send_emote(
        random.choice(['emoji-flex', 'dance-tiktok10', 'emote-snake', 'emote-roll', 'emote-superpunch', 'emote-kicking', 'idle-floorsleeping2', 'emote-hero', 'idle_layingdown2', 'idle_layingdown', 'dance-sexy', 'emoji-hadoken', 'emote-disappear', 'emote-graceful', 'sit-idle-cute', 'idle-loop-aerobics', 'dance-orangejustice', 'emote-rest', 'dance-martial-artist', 'dance-breakdance', 'emote-astronaut', 'emote-zombierun', 'idle_singing', 'emote- frollicking', 'emote-float', 'emote-kicking', 'emote-ninjarun', 'emote-secrethandshake', 'emote-apart', 'emote-headball', 'dance-floss', 'emote-jetpack', 'emote-ghost-idle', 'dance-spiritual', 'dance-robotic', 'dance-metal', 'idle-loop-tapdance', 'idle-dance-swinging', 'emote-mindblown', 'emote-gangnam', 'emote-harlemshake', 'emote-robot', 'emote-nightfever', 'dance-anime', 'idle-guitar', 'emote-headblowup', 'dance-creepypuppet', 'emote-creepycute', 'emote-sleigh', 'emote-hyped', 'dance-jinglebell', 'idle-nervous', 'idle-toilet', 'emote-timejump', 'sit-relaxed', 'dance-kawai', 'idle-wild', 'emote-iceskating', 'sit-open', 'dance-touch']))
      emote_choices = ["dance-blackpink","dance-icecream","dance-macarena","dance-pennywise","dance-russian","dance-shoppingcart","dance-tiktok2","dance-tiktok8","dance-tiktok9","dance-tiktok10","dance-weird","dance-wrong","emoji-angry","emoji-celebrate","emoji-cursing","emoji-flex","emoji-gagging","emoji-thumbsup","emote-astronaut","emote-bow","emote-boxer","emote-celebrationstep","emote-charging","emote-confused","emote-curtsy","emote-cute","emote-cutey","emote-energyball","emote-fashionista","emote-float","emote-frog","emote-gravity","emote-greedy","emote-hello","emote-hot","emote-kiss","emote-laughing","emote-lust","emote-maniac","emote-model","emote-no","emote-pose1","emote-pose3","emote-pose5","emote-pose6","emote-pose7","emote-pose8","emote-pose9","emote-punkguitar","emote-sad","emote-shy","emote-snake","emote-snowangel","emote-snowball","emote-stargazer","emote-superpose","emote-swordfight","emote-telekinesis","emote-teleporting","emote-tired","emote-wave","emote-yes","emote-zombierun","idle_singing","idle-dance-casual","idle-dance-tiktok4","idle-enthusiastic","idle-guitar","idle-loop-sitfloor","idle-uwu"] 
      emote_choice = random.choice(emote_choices)
      await self.highrise.send_emote(emote_choice, user.id)

                                     
      

    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
      try:
        if receiver.username == "shadey.bot" and tip.amount >= 100:
          await self.highrise.teleport(sender.id, Position(1, 0, 1, "FrontRight"))
      except Exception as e:
        print(f"An exception occurred: {e}")

      if tip.amount <= 10:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g - Boooooooooo!!!!!! {sender.username} ")
          tip_message = f" {sender.username} tipped {receiver.username} {tip.amount}g LESS GOOO 🔥"
          await self.highrise.chat(f"{tip_message}")

      elif tip.amount <= 100:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g - Cheapskate!!!{sender.username} ")
          tip_message=f" Damn Tip em more,Tip me too {sender.username}"
          await self.highrise.chat(f"{tip_message}")

      elif tip.amount <= 500:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g - Good Grief!!!{sender.username} ")
          tip_message = f" Soooooo you single baby boo ? i need a bf/gf who tips me g too  ,{sender.username}"
          await self.highrise.chat(f"{tip_message}") 

      elif tip.amount <= 1000:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g - Dayummmmmmm{sender.username} ")
          tip_message = f"Oh boy !!!! Is this love ?   ,{sender.username}"
          await self.highrise.chat(f"{tip_message}")

      elif tip.amount <= 5000:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g -  {sender.username} ")
          tip_message = f"Tip me Daddy,Daddy,Pwease Daddy ,{sender.username}"
          await self.highrise.chat(f"{tip_message}")

      elif tip.amount >=10000:
        print(f"[TIP ] {sender.username} tipped {tip.amount} - I think I will call you daddy!")
        tip_message = [f"\n {sender.username} tipped {tip.amount} - I think I will call you daddy! ",
            f"\n  {sender.username} Oh boy !!!! Is this love ?   " ,
            f"\n {sender.username} Daddy ",
            f"\n{sender.username} I can buy my kids baby food tonight yayyyy ",
            f"\n {sender.username} Soooooo you single baby boo ?   "
        ]
        random_word = random.choice(tip_message)
        await self.highrise.chat(f"{random_word}")

    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
      print(f"{user.username} emoted: {emote_id}")

    

    async def on_whisper(self, user: User, message: str) -> None:
        print(f"{user.username} whispered: {message}")
        allowed_usernames = [
        "Mr.jawaan", "GUPI_" , "nubi.bean", "Reedolf", "lalaapo" 
        ]
        if message.lower().startswith("/giveme") and user.username in allowed_usernames:
            parts = message.split(" ")
            if len(parts) != 2:
                await self.highrise.send_message(user.id, "Invalid command")
                return
            #checks if the amount is valid
            try:
                amount = int(parts[1])
            except:
                await self.highrise.chat("Invalid amount")
                return
            #checks if the bot has the amount
            bot_wallet = await self.highrise.get_wallet()
            bot_amount = bot_wallet.content[0].amount
            if bot_amount <= amount:
                await self.highrise.chat("Not enough funds")
                return
            #converts the amount to a string of bars and calculates the fee
            """Possible values are: "gold_bar_1",
            "gold_bar_5", "gold_bar_10", "gold_bar_50", 
            "gold_bar_100", "gold_bar_500", 
            "gold_bar_1k", "gold_bar_5000", "gold_bar_10k" """
            bars_dictionary = {10000: "gold_bar_10k", 
                               5000: "gold_bar_5000",
                               1000: "gold_bar_1k",
                               500: "gold_bar_500",
                               100: "gold_bar_100",
                               50: "gold_bar_50",
                               10: "gold_bar_10",
                               5: "gold_bar_5",
                               1: "gold_bar_1"}
            fees_dictionary = {10000: 1000,
                               5000: 500,
                               1000: 100,
                               500: 50,
                               100: 10,
                               50: 5,
                               10: 1,
                               5: 1,
                               1: 1}
            #loop to check the highest bar that can be used and the amount of it needed
            tip = []
            total = 0
            for bar in bars_dictionary:
                if amount >= bar:
                    bar_amount = amount // bar
                    amount = amount % bar
                    for i in range(bar_amount):
                        tip.append(bars_dictionary[bar])
                        total = bar+fees_dictionary[bar]
            if total > bot_amount:
                await self.highrise.chat("Not enough funds")
                return
            for bar in tip:
                await self.highrise.tip_user(user.id, bar)

    

        

                
             


    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        print(f"{user.username} sended the reaction {reaction} to {receiver.username}")
        

        
        
        




    async def on_user_move(self, user: User, pos: Position) -> None:
        print(f"{user.username} moved to {pos}")
        
        






    






    async def walk(self, position: Position | AnchorPosition):
        try:
            await self.highrise.walk_to(position)
        except Exception as e:
            print(f"Caught Walking Error: {e}")

    async def on_user_leave(self, user: User) -> None:
        # Your existing code
            
        # Handle the error
            
        # Other error handling logic

            print(f"{user.username} Left the Room")

       #     goodbye_messages = ["Thanks for dropping in! See you next time💗.","Goodbye for now! Come back soon👻.","Farewell! It was great chat with you✨.","Until next time! Take care💘.","Bye for now! Don't be a stranger🥺.","Safe travels! Visit again soon🤗.","Adios! Looking forward to your next visit💓.","Catch you later! Your presence is always appreciated🙈.","Take care on your journey! See you again soon😏.","So long! Remember, you're always welcome back🥰."]
           # random_message = random.choice(goodbye_messages)
            
            await self.highrise.send_emote("emote-bow")

    async def delayed_message_command(self, message, command):
        # Implementation of delayed_message_command goes here
        pass

    
    
    

  
 





    
      
  


    async def teleport_user_next_to(self, target_username: str, requester_user: User):

        room_users = await self.highrise.get_room_users()
        requester_position = None
    
        for user, position in room_users.content:
          if user.id == requester_user.id:
              requester_position = position
              break
        for user, position in room_users.content:
          if user.username.lower() == target_username.lower(): 
            z = requester_position.z 
            new_z = z + 1 
    
            user_dict = {
              "id": user.id,
              "position": Position(requester_position.x, requester_position.y, new_z, requester_position.facing)
            }
            await self.highrise.teleport(user_dict["id"], user_dict["position"]) 




    async def tip_all_users(self, user, amount, item):
        room_users = (await self.highrise.get_room_users()).content
        for room_user, _ in room_users:
            await self.highrise.tip_user(room_user.id, item)
        await self.highrise.send_whisper(user.id, f"Tipped {amount} gold bar(s) to all users!")



    async def teleport(self, user, position, area_name):
        try:
            await self.highrise.teleport(user.id, position)
            await self.highrise.send_whisper(user.id, f"You have been teleported to the {area_name}.")
        except Exception as e:
            print(f"Error teleporting user to {area_name}: {e}")

    async def process_teleport_command(self, user, message, command, destination, area_name):
        try:
            response = await self.highrise.get_room_users()

            if response.content is None:
                await self.highrise.send_whisper(user.id, "Unable to fetch room users.")
                return

            users = [content[0] for content in response.content]
            usernames = [user.username.lower() for user in users]

            parts = message.split()
            if len(parts) != 2:
                await self.highrise.send_whisper(user.id, f"Usage: {command} @username")
                return

            if parts[1][0] != "@":
                await self.highrise.send_whisper(user.id, f"Incorrect format, use '@username' for {command}.")
                return
            elif parts[1][1:].lower() not in usernames:
                await self.highrise.send_whisper(user.id, f"{parts[1][1:]} not in the room.")
                return

            user_id = next((u.id for u in users if u.username.lower() == parts[1][1:].lower()), None)
            if not user_id:
                await self.highrise.send_whisper(user.id, f"User {parts[1][1:]} unavailable.")
                return

            await self.highrise.teleport(user_id, destination)
            await self.highrise.send_whisper(user.id, f"{parts[1][1:]} teleported to the {area_name}.")

        except Exception as e:
            print(f"Error processing {command} command: {e}")
    
      



    



    async def on_chat(self, user: User, message: str) -> None:

        print(f"{user.username}:{message}")
            




      
        allowed_usernames = [
        "Mr.jawaan", "GUPI_" , "nubi.bean", "Reedolf", "lalaapo" 
        ]
        
        

        
      
        # /loop start / loop stop ----------------------------------------

        if message in self.EMOTE_DICT:
            emote_id = self.EMOTE_DICT[message]
            await self.highrise.send_emote(emote_id, user.id)
        

        if message.startswith("/rent"):
            await self.highrise.chat(f"Thank you for message me, {user.username} I registered your name in rent bot list..!! pm @mr.jawaan for more info...")

        if message.startswith("mod"):
            await self.highrise.chat(f"\n____________________________ \n▄︻┻ OWNER ︻┳═─- \n•@GUPI_ \n \n____________________________ \n★彡[ᴍᴏᴅꜱ]彡★ \n•@nubi.bean \n \n____________________________")

        if message.startswith("/mod"):
            if user.username in allowed_usernames:

                await self.highrise.chat(f"@{user.username} kindly wait checking your information! Thankyou💕")
                await asyncio.sleep(2)
          
                await self.highrise.teleport(f"{user.id}", Position(14.5, 21, 4))
                await self.highrise.chat(f"@{user.username} you are approved for mod section 🤗")

            else:
                await self.highrise.chat(f"@{user.username} kindly wait checking your information! Thankyou💕")
                await asyncio.sleep(2)
              
                await self.highrise.chat(f"@{user.username} your not in mod list, kindly contact room owner for more help!!")
            
    

        if message.startswith("❤️")and user.username in allowed_usernames:
            command_parts = message.split()
            num_reactions = 1
            reaction_name = None

            if len(command_parts) > 1:
                try:
                    num_reactions = int(command_parts[1])
                except ValueError:
                    await self.highrise.chat("Invalid number of reactions. Please provide a valid integer.")
                    return

            if len(command_parts) > 2:
        # Check if a specific reaction name is provided
                reaction_name = command_parts[2].lower()

            response = await self.highrise.get_room_users()
            room_users = response.content if hasattr(response, 'content') else []

            reactions = ["heart"]  # Modify the reactions list to include only "heart"

            for target_user in room_users:
               if isinstance(target_user, tuple):
                target_user = target_user[0]  # Assuming the user object is stored in the first element of the tuple

                if target_user.id != self:  # Assuming 'self' is the bot's ID
                    for _ in range(num_reactions):  # Use '_' as a placeholder for the loop variable
                        if reaction_name:
                            if reaction_name in reactions:
                                selected_reaction = reaction_name
                            else:
                                await self.highrise.chat(f"Invalid reaction name: {reaction_name}. Available reactions: {', '.join(reactions)}")
                                return
                        else:
                            selected_reaction = random.choice(reactions)
                        try:
                            await self.highrise.react(selected_reaction, target_user.id)
                            await asyncio.sleep(delay_between_reactions)
                        except Exception as e:
    # Handle the error here
                              print(f"An error occurred: {e}")

        

                          
        if message.lower().startswith("/getoutfit"):
            response = await self.highrise.get_my_outfit()
            for item in response.outfit:
                await self.highrise.chat(item.id)
        


        
        
        if user.username in allowed_usernames:
            if message.lower().startswith("/vip1"):
                await self.teleport(user, Position(8, 14, 0.5), "VIP Area 1")
            elif message.lower().startswith("/vip2"):
                await self.teleport(user, Position(17.5, 14, 12.5), "VIP Area 2")
            elif message.lower().startswith("/dj"):
                await self.teleport(user, Position(5.5, 1, 24.5), "DJ Area")
            elif message.lower().startswith("/vip3"):
                await self.teleport(user, Position(15.5, 14.5, 2.5), "VIP Area 3")
            elif message.lower().startswith("/bar"):
                await self.teleport(user, Position(16, 5, 17), "Bar🍻🍾")
            elif message.lower().startswith("/down"):
                await self.teleport(user, Position(9.5, 0, 13.5), "Under the water 🌊 🧜🏻‍♂️")
            elif message.lstrip().startswith("f1"):
                await self.process_teleport_command(user, message, "f1", Position(12.5, 4.5, 27.5), "Floor 1")
            elif message.lstrip().startswith("f2"):
                await self.process_teleport_command(user, message, "f2", Position(6, 9.5, 8.5), "Floor 2")
            elif message.lstrip().startswith("dj"):
                await self.process_teleport_command(user, message, "dj", Position(5.5, 1, 24.5), "DJ Area")
            elif message.lstrip().startswith("vip1"):
                await self.process_teleport_command(user, message, "vip1", Position(8, 14, 0.5), "VIP area 1")
            elif message.lstrip().startswith("vip2"):
                await self.process_teleport_command(user, message, "vip2", Position(17.5, 14, 12.5), "VIP area 2")
            elif message.lstrip().startswith("vip3"):
                await self.process_teleport_command(user, message, "vip3", Position(15.5, 14.5, 2.5), "VIP area 3")
            elif message.lstrip().startswith("bar"):
                await self.process_teleport_command(user, message, "bar", Position(16, 5, 17), "Bar🍻🍾")
            elif message.lstrip().startswith("down"):
                await self.process_teleport_command(user, message, "down", Position(9.5, 0, 13.5), "Under the water 🌊 🧜🏻‍♂️")
            elif message.startswith("/tip5"):
                await self.tip_all_users(user, 5, "gold_bar_5")
            elif message.startswith("/tip1"):
                await self.tip_all_users(user, 1, "gold_bar_1")
            elif message.startswith("/tip10"):
                await self.tip_all_users(user, 10, "gold_bar_10")
            elif message.startswith("/tip50"):
                await self.tip_all_users(user, 50, "gold_bar_50")
            
            
            
                
        
        else:
            await self.highrise.send_whisper(user.id, "You can't use this command.")
            return


        

        
        

        

        if "/hi" in message or "/hello" in message :
              try:
                  await self.highrise.chat( "hello, how are you?")
              except:
                print("error 3")

        if "/how are you" in message or "/wby" in message :
              try:
                  await self.highrise.chat( "I am fine, thank you")
              except:
                print("error 3")

        if "/fine" in message or "/good" in message :
              try:
                  await self.highrise.chat( "Great to hear that")
              except:
                print("error 3")

        if "/what is your name" in message or "/name" in message :
          try:
              await self.highrise.chat( "I dont have name but you can call me MINE😍")
          except:
            print("error 3")

        if "/I love you" in message or "/ily" in message :
              try:
                  await self.highrise.chat( "I love you too❤️")
              except:
                print("error 3")

        if "/I hate you" in message or "/ihy" in message :
              try:
                  await self.highrise.chat( "Still Love you❤️")
              except:
                print("error 3")

        if "/will you marry me" in message or "/wyme" in message :
              try:
                  await self.highrise.chat( "I am a bot, but i will marry you🌝❤️")
              except:
                print("error 3")




        

        message_lower = message.lower()  # Convert message to lowercase
        for command, (position, area) in self.commands.items():
            if command.lower() in message_lower:
                try:
                    await self.highrise.teleport(f"{user.id}", position)
                    await self.highrise.send_whisper(user.id, f"Teleported to the {area} Area.")
                except Exception as e:
                    print(f"Error: {e}")
                break  # Exit loop once command is processed
        
        

          
      

        


        if message.lower().startswith("/item "):
            parts = message.split(" ")
            if len(parts) < 2:
                await self.highrise.chat("Invalid command")
                return
            item_name = ""
            for part in parts[1:]:
                item_name += part + " "
            item_name = item_name[:-1]
            print (item_name)
            try:
                response = await self.webapi.get_items(item_name=item_name)
                print (response)
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
              
        

        


        if message.lower().startswith("/equip"):
            await self.highrise.set_outfit(outfit=[
        Item(type='clothing',
             amount=1,
             id='hair_front-n_malenew08',
             account_bound=False,
             active_palette=1),
        Item(type='clothing',
             amount=1,
             id='body-flesh',
             account_bound=False,
             active_palette=1),
        Item(type='clothing',
             amount=1,
             id='eye-n_basic2018downturnedround',
             account_bound=False,
             active_palette=7),
        Item(type='clothing',
             amount=1,
             id='eyebrow-n_26',
             account_bound=False,
             active_palette=0),
        Item(type='clothing',
             amount=1,
             id='nose-n_01',
             account_bound=False,
             active_palette=0),
        Item(type='clothing',
             amount=1,
             id='mouth-basic2018lollipop',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shirt-n_starteritems2019raglanwhite',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='pants-n_starteritems2019cuffedjeansblack',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shoes-n_room22019tallsocks',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='necklace-n_room12019chain',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shoes-n_platformsneakerblack',
             account_bound=False,
             active_palette=-1),

        Item(type='clothing',
             amount=1,
             id='glasses-n_starteritems2019squareframesblack',
             account_bound=False,
             active_palette=-1),
              
        Item(type='clothing',
             amount=1,
             id='freckle-n_basic2018freckle22',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='hair_front-n_malenew08',
             account_bound=False,
             active_palette=-1)
      ])

        if message.lower().startswith("/equip1"):
            await self.highrise.set_outfit(outfit=[
        Item(type='clothing',
             amount=1,
             id='hair_front-n_malenew15',
             account_bound=False,
             active_palette=1),
        Item(type='clothing',
             amount=1,
             id='body-flesh',
             account_bound=False,
             active_palette=1),
        Item(type='clothing',
             amount=1,
             id='eye-n_basic2018malealmond',
             account_bound=False,
             active_palette=7),
        Item(type='clothing',
             amount=1,
             id='eyebrow-n_26',
             account_bound=False,
             active_palette=0),
        Item(type='clothing',
             amount=1,
             id='nose-n_01',
             account_bound=False,
             active_palette=0),
        Item(type='clothing',
             amount=1,
             id='mouth-basic2018thinround',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shirt-n_room12019buttondownblack',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='pants-n_room32019rippedpantswhite',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shoes-n_room22019tallsocks',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='glasses-n_room32019smallshades',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shoes-n_room12019sneakersblack',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='freckle-n_basic2018freckle22',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='hair_back-n_malenew15',
             account_bound=False,
             active_palette=-1)
      ])
          
        
        if message.lower().startswith("/equip2"):
            await self.highrise.set_outfit(outfit=[
        Item(type='clothing',
             amount=1,
             id='hair_front-n_basic2020overshoulderpony',
             account_bound=False,
             active_palette=1),
        Item(type='clothing',
             amount=1,
             id='body-flesh',
             account_bound=False,
             active_palette=1),
        Item(type='clothing',
             amount=1,
             id='eye-n_basic2018dolleyes',
             account_bound=False,
             active_palette=7),
        Item(type='clothing',
             amount=1,
             id='eyebrow-n_26',
             account_bound=False,
             active_palette=0),
        Item(type='clothing',
             amount=1,
             id='nose-n_01',
             account_bound=False,
             active_palette=0),
        Item(type='clothing',
             amount=1,
             id='mouth-basic2018lollipop',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shirt-n_room12019cropsweaterblack',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='skirt-n_room12019pleatedskirtblack',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shoes-n_room22019tallsocks',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='glasses-n_room32019smallshades',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='shoes-n_starteritems2019flatsblack',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='freckle-n_basic2018freckle22',
             account_bound=False,
             active_palette=-1),
        Item(type='clothing',
             amount=1,
             id='hair_back-n_basic2020overshoulderpony',
             account_bound=False,
             active_palette=-1)
      ])
             


        if message.lower().startswith("/getinventory"):
            inventory = await self.highrise.get_inventory()
            print (inventory)




        if message.lower().startswith(
        "delayed_message") and user.username in self.allowed_usernames:
                 await self.delayed_message_command(Message)

        elif message.lower(
    ) == "stop_delayed_message" and user.username in self.allowed_usernames:
                 await self.stop_delayed_messages()


        if message.startswith("/hyped") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hyped", roomUser.id)

        if message.startswith("/jingle") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-jinglebell", roomUser.id)

        if message.startswith("/gottago") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-toilet", roomUser.id)

        if message.startswith("/penguin") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pinguin", roomUser.id)

        if message.startswith("/revelations") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-headblowup", roomUser.id)

        if message.startswith("/anime") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-anime", roomUser.id)

        if message.startswith("/zero") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-astronaut", roomUser.id)

        if message.startswith("/dont") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok2", roomUser.id)

        if message.startswith("/punkguitar") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-punkguitar", roomUser.id)

        if message.startswith("/weird") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-weird", roomUser.id)

        if message.startswith("/sayso") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)

        if message.startswith("/frog") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-frog", roomUser.id)

        if message.startswith("/zombie") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-zombierun", roomUser.id)

        if message.startswith("/kawaii") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-kawai", roomUser.id)

        if message.startswith("/scritchy") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-wild", roomUser.id)

        if message.startswith("/skating") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-iceskating", roomUser.id)

        if message.startswith("/touch") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-touch", roomUser.id)

        if message.startswith("/pushit") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-employee", roomUser.id)

        if message.startswith("/fashionista") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-fashionista", roomUser.id)

        if message.startswith("/shuffle") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok10", roomUser.id)

        if message.startswith("/singalong") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle_singing", roomUser.id)

        if message.startswith("/russian") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-russian", roomUser.id)

        if message.startswith("/worm") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-snake", roomUser.id)

        if message.startswith("/launch") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-launch", roomUser.id)

        if message.startswith("/wop") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok11", roomUser.id)

        if message.startswith("/flirtywave") and user.username in allowed_usernames:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-lust", roomUser.id)
      

        


        




        if message.startswith("kick"):
            if user.username in ["Mr.jawaan", "GUPI_" , "nubi.bean", "Reedolf", "lalaapo" ]:
                pass
            else:
                await self.highrise.chat("You do not have permission to use this command.")
                return
            #separete message into parts
            parts = message.split()
            #check if message is valid "kick @username"
            if len(parts) != 2:
                await self.highrise.chat("Invalid kick command format.")
                return
            #checks if there's a @ in the message
            if "@" not in parts[1]:
                username = parts[1]
            else:
                username = parts[1][1:]
            #check if user is in room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat("User not found, please specify a valid user and coordinate")
                return
            #kick user
            try:
                await self.highrise.moderate_room(user_id, "kick")
            except Exception as e:
                await self.highrise.chat(f"{e}")
                return
            #send message to chat
            await self.highrise.chat(f"{username} has been kicked from the room.")
        



        elif message.lower().startswith("wallet") and user.username in allowed_usernames:
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.send_whisper(user.id, f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

        

        if "Emotelist" in message or "emotes" in message or "Emotes" in message or "emotelist" in message:
            await self.highrise.send_whisper(user.id,
"\nangry,\nbow,\ncasual,\nraisetheroof,\ncharging,\nconfusion,\ncursing,\ncurtsy,\ncutey,\ndont,\nemotecute,\nenergyball,\nenthused,\nflex,\nflirtywave,\nfloat,\nfrog,\ngreedy,\nhello,\nhot,\nkiss,\nkpop,\nlambi,\nlaugh,\nletsgo,\nmaniac,\nmodel,\nno,\nogdance,")
            await self.highrise.send_whisper(user.id,"\npennydance,\npose1,\npose2,\npose3,\npose4,\npose5,\nrussian,\nsad,\nsavage,\nshuffle,\nshy,\nsingalong,\nsit,\nsnowangel,\nsnowball,\nswordfight,\ntelekinesis,\nteleport,\nthumbsup,\ntired,\ntummyache,\nviral,\nwave,\nweird,\nworm,\nyes")
            await self.highrise.send_whisper(user.id,"\nfashionista,\ngravedance,\ngravity,\nicecream,\npunkguitar,\nsayso,\nuwu,\nzombierun,\nPenguin,\nCreepycute,\nCreepy,\nAirguitar,\nanime")
            await self.highrise.send_whisper(user.id,"\nNEW EMOTES😚💓\nsleigh,\nhyped, \njingle, \nnervous, \ngottago, \ntimeJump ,\nrepose, \nkawaii, \nscritchy,\nskating, \ntouch \ngift \npushit \nwop \n-\n MORE COMING SOON😁") 




        



        if message.lower().lstrip().startswith(("fight", "hug", "flirt", "stars", "gravity", "uwu", "zero","fashion", "icecream", "punk", "wrong", "sayso", "zombie", "cutey", "pose1", "pose3", "pose5", "pose7", "pose8", "dance", "shuffle", "viralgroove", "weird", "russian", "curtsy", "snowball", "sweating", "snowangel", "cute", "worm", "lambi", "sing", "frog", "energyball", "maniac", "teleport", "float", "telekinesis", "enthused", "confused", "charging", "shopping", "bow", "savage", "kpop", "model", "dontstartnow", "pennydance", "flex", "gagging", "greedy", "cursing", "kiss", "wing", "bashfull", "anime", "airguitar", "revelation", "penguin", "creepycute", "creepy", "sleigh", "hyped", "jingle", "nervous", "gottago", "timejump", "repose", "kawaii", "scritchy", "skating", "touch", "gift", "pushit", "launch", "wop" )):
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]

                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, f"Usage: {parts[0]} <@username>")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, "Invalid user format. Please use '@username'.")
                    return
                elif args[0][1:].lower() not in usernames:
                    await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
                    return

                user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
                if not user_id:
                    await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
                    return


                if message.lower().lstrip().startswith("fight"):
                        await self.highrise.chat(f"\n🥷 @{user.username} And @{args[0][1:]} ATTACKKKKK🤬⚔️🔥")
                        await self.highrise.send_emote("emote-swordfight", user.id)
                        await self.highrise.send_emote("emote-swordfight", user_id)

                elif message.lower().lstrip().startswith("hug"):
                        await self.highrise.chat(f"\n🫂 @{user.username} And @{args[0][1:]} HUG IS MEDICINE OF OUR LIFE❤️")
                        await self.highrise.send_emote("emote-hug", user.id)
                        await self.highrise.send_emote("emote-hug", user_id)

                elif message.lower().lstrip().startswith("flirt"):
                        await self.highrise.chat(f"\n Hey @{user.username} And @{args[0][1:]} AEE REE FUGANIYAAAA TU HAMAAR JAAN HAI RE 🤭🫣❤️")
                        await self.highrise.send_emote("emote-lust", user.id)
                        await self.highrise.send_emote("emote-lust", user_id)

                elif message.lower().lstrip().startswith("stars"):
                        await self.highrise.send_emote("emote-stargazer", user.id)
                        await self.highrise.send_emote("emote-stargazer", user_id)


                elif message.lower().lstrip().startswith("zero"):
                        await self.highrise.chat(f"\n Hey @{user.username} And @{args[0][1:]} UTHAA LE RE BABAA😰😧👨🏻‍🚀")
                        await self.highrise.send_emote("emote-astronaut", user.id)
                        await self.highrise.send_emote("emote-astronaut", user_id)

                elif message.lower().lstrip().startswith("gravity"):
                        await self.highrise.send_emote("emote-gravity", user.id)
                        await self.highrise.send_emote("emote-gravity", user_id)

                elif message.lower().lstrip().startswith("uwu"):
                        await self.highrise.chat(f"\n Hey @{user.username} And @{args[0][1:]} Dont be shy🤭🫣❤️")
                        await self.highrise.send_emote("idle-uwu", user.id)
                        await self.highrise.send_emote("idle-uwu", user_id)

                elif message.lower().lstrip().startswith("fashion"):
                        await self.highrise.send_emote("emote-fashionista", user.id)
                        await self.highrise.send_emote("emote-fashionista", user_id)

                elif message.lower().lstrip().startswith("icecream"):
                        await self.highrise.send_emote("dance-icecream", user.id)
                        await self.highrise.send_emote("dance-icecream", user_id)

                elif message.lower().lstrip().startswith("punk"):
                        await self.highrise.send_emote("emote-punkguitar", user.id)
                        await self.highrise.send_emote("emote-punkguitar", user_id)

                elif message.lower().lstrip().startswith("wrong"):
                        await self.highrise.send_emote("dance-wrong", user.id)
                        await self.highrise.send_emote("dance-wrong", user_id)

                elif message.lower().lstrip().startswith("sayso"):
                        await self.highrise.send_emote("idle-dance-tiktok4", user.id)
                        await self.highrise.send_emote("idle-dance-tiktok4", user_id)

                elif message.lower().lstrip().startswith("zombie"):
                        await self.highrise.send_emote("emote-zombierun", user.id)
                        await self.highrise.send_emote("emote-zombierun", user_id)

                elif message.lower().lstrip().startswith("cutey"):
                        await self.highrise.send_emote("emote-cutey", user.id)
                        await self.highrise.send_emote("emote-cutey", user_id)

                elif message.lower().lstrip().startswith("pose5"):
                        await self.highrise.send_emote("emote-pose5", user.id)
                        await self.highrise.send_emote("emote-pose5", user_id)

                elif message.lower().lstrip().startswith("pose3"):
                        await self.highrise.send_emote("emote-pose3", user.id)
                        await self.highrise.send_emote("emote-pose3", user_id)

                elif message.lower().lstrip().startswith("pose1"):
                        await self.highrise.send_emote("emote-pose1", user.id)
                        await self.highrise.send_emote("emote-pose1", user_id)

                elif message.lower().lstrip().startswith("pose7"):
                        await self.highrise.send_emote("emote-pose7", user.id)
                        await self.highrise.send_emote("emote-pose7", user_id)

                elif message.lower().lstrip().startswith("pose8"):
                        await self.highrise.send_emote("emote-pose8", user.id)
                        await self.highrise.send_emote("emote-pose8", user_id)

                elif message.lower().lstrip().startswith("dance"):
                        await self.highrise.send_emote("idle-dance-casual", user.id)
                        await self.highrise.send_emote("idle-dance-casual", user_id)

                elif message.lower().lstrip().startswith("shuffle"):
                        await self.highrise.send_emote("dance-tiktok10", user.id)
                        await self.highrise.send_emote("dance-tiktok10", user_id)

                elif message.lower().lstrip().startswith("weird"):
                        await self.highrise.send_emote("emote-weird", user.id)
                        await self.highrise.send_emote("emote-weird", user_id)

                elif message.lower().lstrip().startswith("viralgroove"):
                        await self.highrise.send_emote("dance-tiktok9", user.id)
                        await self.highrise.send_emote("dance-tiktok9", user_id)

                elif message.lower().lstrip().startswith("cute"):
                        await self.highrise.send_emote("emote-cute", user.id)
                        await self.highrise.send_emote("emote-cute", user_id)

                elif message.lower().lstrip().startswith("frog"):
                        await self.highrise.send_emote("emote-frog", user.id)
                        await self.highrise.send_emote("emote-frog", user_id)

                elif message.lower().lstrip().startswith("lambi"):
                        await self.highrise.send_emote("emote-superpose", user.id)
                        await self.highrise.send_emote("emote-superpose", user_id)

                elif message.lower().lstrip().startswith("sing"):
                        await self.highrise.send_emote("idle-singing", user.id)
                        await self.highrise.send_emote("idle-singing", user_id)

                elif message.lower().lstrip().startswith("worm"):
                        await self.highrise.send_emote("emote-snake", user.id)
                        await self.highrise.send_emote("emote-snake", user_id)

                elif message.lower().lstrip().startswith("bow"):
                        await self.highrise.send_emote("emote-bow", user.id)
                        await self.highrise.send_emote("emote-bow", user_id)

                elif message.lower().lstrip().startswith("energyball"):
                        await self.highrise.send_emote("emote-energyball", user.id)
                        await self.highrise.send_emote("emote-energyball", user_id)

                elif message.lower().lstrip().startswith("maniac"):
                        await self.highrise.send_emote("emote-maniac", user.id)
                        await self.highrise.send_emote("emote-maniac", user_id)

                elif message.lower().lstrip().startswith("teleport"):
                        await self.highrise.send_emote("emote-teleporting", user.id)
                        await self.highrise.send_emote("emote-teleporting", user_id)

                elif message.lower().lstrip().startswith("float"):
                        await self.highrise.send_emote("emote-float", user.id)
                        await self.highrise.send_emote("emote-float", user_id)

                elif message.lower().lstrip().startswith("telekinesis"):
                        await self.highrise.send_emote("emote-telekinesis", user.id)
                        await self.highrise.send_emote("emote-telekinesis", user_id)

                elif message.lower().lstrip().startswith("enthused"):
                        await self.highrise.send_emote("idle-enthusiastic", user.id)
                        await self.highrise.send_emote("idle-enthusiastic", user_id)

                elif message.lower().lstrip().startswith("confused"):
                        await self.highrise.send_emote("emote-confused", user.id)
                        await self.highrise.send_emote("emote-confused", user_id)

                elif message.lower().lstrip().startswith("shopping"):
                        await self.highrise.send_emote("dance-shoppingcart", user.id)
                        await self.highrise.send_emote("dance-shoppingcart", user_id)

                elif message.lower().lstrip().startswith("charging"):
                        await self.highrise.send_emote("emote-charging", user.id)
                        await self.highrise.send_emote("emote-charging", user_id)

                elif message.lower().lstrip().startswith("snowangel"):
                        await self.highrise.send_emote("emote-snowangel", user.id)
                        await self.highrise.send_emote("emote-snowangel", user_id)

                elif message.lower().lstrip().startswith("sweating"):
                        await self.highrise.send_emote("emote-hot", user.id)
                        await self.highrise.send_emote("emote-hot", user_id)

                elif message.lower().lstrip().startswith("snowball"):
                        await self.highrise.send_emote("emote-snowball", user.id)
                        await self.highrise.send_emote("emote-snowball", user_id)

                elif message.lower().lstrip().startswith("curtsy"):
                        await self.highrise.send_emote("emote-curtsy", user.id)
                        await self.highrise.send_emote("emote-curtsy", user_id)

                elif message.lower().lstrip().startswith("russian"):
                        await self.highrise.send_emote("dance-russian", user.id)
                        await self.highrise.send_emote("dance-russian", user_id)

                elif message.lower().lstrip().startswith("pennywise"):
                        await self.highrise.send_emote("dance-pennywise", user.id)
                        await self.highrise.send_emote("dance-pennywise", user_id)

                elif message.lower().lstrip().startswith("dont"):
                        await self.highrise.send_emote("dance-tiktok2", user.id)
                        await self.highrise.send_emote("dance-tiktok2", user_id)

                elif message.lower().lstrip().startswith("kpop"):
                        await self.highrise.send_emote("dance-blackpink", user.id)
                        await self.highrise.send_emote("dance-blackpink", user_id)

                elif message.lower().lstrip().startswith("model"):
                        await self.highrise.send_emote("emote-model", user.id)
                        await self.highrise.send_emote("emote-model", user_id)

                elif message.lower().lstrip().startswith("savage"):
                        await self.highrise.send_emote("dance-tiktok8", user.id)
                        await self.highrise.send_emote("dance-tiktok8", user_id)

                elif message.lower().lstrip().startswith("flex"):
                        await self.highrise.send_emote("emoji-flex", user.id)
                        await self.highrise.send_emote("emoji-flex", user_id)

                elif message.lower().lstrip().startswith("gagging"):
                        await self.highrise.send_emote("emoji-gagging", user.id)
                        await self.highrise.send_emote("emoji-gagging", user_id)

                elif message.lower().lstrip().startswith("greedy"):
                        await self.highrise.send_emote("emote-greedy", user.id)
                        await self.highrise.send_emote("emote-greedy", user_id)

                elif message.lower().lstrip().startswith("cursing"):
                        await self.highrise.send_emote("emoji-cursing", user.id)
                        await self.highrise.send_emote("emoji-cursing", user_id)

                elif message.lower().lstrip().startswith("zero"):
                        await self.highrise.send_emote("emote-astronaut", user.id)
                        await self.highrise.send_emote("emote-astronaut", user_id)

                elif message.lower().lstrip().startswith("kiss"):
                        await self.highrise.send_emote("emote-kiss", user.id)
                        await self.highrise.send_emote("eote-kiss", user_id)
                elif message.lower().lstrip().startswith("anime"):
                        await self.highrise.send_emote("dance-anime", user.id)
                        await self.highrise.send_emote("dance-anime", user.id)
                elif message.lower().lstrip().startswith("airguitar"):
                        await self.highrise.send_emote("idle-guitar", user.id)
                        await self.highrise.send_emote("idle-guitar", user_id)
                elif message.lower().lstrip().startswith("revelations"):
                        await self.highrise.send_emote("emote-headblowup", user.id)
                        await self.highrise.send_emote("emote-headblowup", user_id)
                elif message.lower().lstrip().startswith("creepy"):
                        await self.highrise.send_emote("dance-creepypuppet", user.id)
                        await self.highrise.send_emote("dance-creepypuppet", user_id)
                elif message.lower().lstrip().startswith("creepycute"):
                        await self.highrise.send_emote("emote-creepycute", user.id)
                        await self.highrise.send_emote("emote-creepycute", user.id)
                elif message.lower().lstrip().startswith("penguin"):
                        await self.highrise.send_emote("dance-pinguin", user.id)
                        await self.highrise.send_emote("dance-pinguin", user.id)
                elif message.lower().lstrip().startswith("sleigh"):
                        await self.highrise.send_emote("emote-sleigh", user.id)
                        await self.highrise.send_emote("emote-sleigh", user.id)
                elif message.lower().lstrip().startswith("hyped"):
                        await self.highrise.send_emote("emote-hyped", user.id)
                        await self.highrise.send_emote("emote-hyped", user.id)
                elif message.lower().lstrip().startswith("jingle"):
                        await self.highrise.send_emote("dance-jinglebell", user.id)
                        await self.highrise.send_emote("dance-jinglebell", user.id)
                elif message.lower().lstrip().startswith("nervous"):
                        await self.highrise.send_emote("idle-nervous", user.id)
                        await self.highrise.send_emote("idle-nervous", user.id)
                elif message.lower().lstrip().startswith("toilet"):
                        await self.highrise.send_emote("idle-toilet", user.id)
                        await self.highrise.send_emote("idle-toilet", user.id)
                elif message.lower().lstrip().startswith("timejump"):
                        await self.highrise.send_emote("emote-timejump", user.id)
                        await self.highrise.send_emote("emote-timejump", user.id)
                elif message.lower().lstrip().startswith("skating"):
                        await self.highrise.send_emote("dance-skating", user.id)
                        await self.highrise.send_emote("dance-skating", user.id)
                elif message.lower().lstrip().startswith("repose"):
                        await self.highrise.send_emote("sit-relaxed", user.id)
                        await self.highrise.send_emote("sit-relaxed", user.id)
                elif message.lower().lstrip().startswith("kawaii"):
                        await self.highrise.send_emote("dance-kawai", user.id)
                        await self.highrise.send_emote("dance-kawai", user.id)
                elif message.lower().lstrip().startswith("scritchy"):
                        await self.highrise.send_emote("idle-wild", user.id)
                        await self.highrise.send_emote("idle-wild", user.id)
                elif message.lower().lstrip().startswith("skating"):
                        await self.highrise.send_emote("emote-iceskating", user.id)
                        await self.highrise.send_emote("emote-iceskating", user.id)

                elif message.lower().lstrip().startswith("touch"):
                        await self.highrise.send_emote("dance-touch", user.id)
                        await self.highrise.send_emote("dance-touch", user.id)

                elif message.lower().lstrip().startswith("pushit"):
                        await self.highrise.send_emote("dance-employee", user.id)
                        await self.highrise.send_emote("dance-employee", user.id)

                elif message.lower().lstrip().startswith("launch"):
                        await self.highrise.send_emote("emote-launch", user.id)
                        await self.highrise.send_emote("emote-launch", user.id)

                elif message.lower().lstrip().startswith("wop"):
                        await self.highrise.send_emote("dance-tiktok11", user.id)
                        await self.highrise.send_emote("dance-tiktok11", user.id)





    async def stop_continuous_emote(self, user_id: int):
        if user_id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user_id].cancelled():
            task = self.continuous_emote_tasks[user_id]
            task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await task
            del self.continuous_emote_tasks[user_id]

    async def send_continuous_emote(self, emote_id: str, user_id: int, delay: float):
        try:
            while True:
                await self.highrise.send_emote(emote_id, user_id)
                await asyncio.sleep(delay)
        except ConnectionResetError:
            # Handle connection reset error appropriately
            pass


    

  
    





async def run(self, room_id, token):
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions)
