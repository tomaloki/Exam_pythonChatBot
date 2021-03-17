# -*- coding: utf-8 -*-

import random


def anna(a, b=None):
    activity = ["work", "play", "eat", "cry", "sleep", "fight"]
    greetings = ["Hey there", "Oh, hi! So happy to talk to you.", "Good day to you!"]
    weather_response = [f"Oh, I quite like that it is going to be {a}.. But that's just me!",
                        f"Hm, I'm not so fond of {a} actually.",
                        f"Isn't it lovely? I just love {a}"]
    compliment_response = ["Oh, you are too kind.", "Thank you so much, what a lovely thing to say!",
                           f"Stop it, you. You are also {a}!!"]
    name_response = ["My name is Anna", "My name is A to the N to the N to the A!"]
    action_response = [f"Not sure about {a}ing. Don't I get a choice?", f"Hm, I think i would like to {a} today!",
                       f"Ugh, I have to pass - i did some {a}ing yesterday, didn't go well..."]
    if a in greeting:
        res = random.choice(greetings)
        return res
    elif a in activity:
        res = random.choice(action_response)
        return res
    elif a in weather:
        res = random.choice(weather_response)
        return res
    elif a in compliments:
        res = random.choice(compliment_response)
        return res
    elif a in name:
        res = random.choice(name_response)
        return res
    else:
        return "I really enjoy talking to you all!"


def derek(a, b=None):
    activity = ["work", "play", "eat", "cry", "sleep", "fight"]
    greetings = ["Wazzup", "Long time no see", "Howdy"]
    weather_response = [f"{a}, {a}, {a}... kinda sick of it.", f"{a} you say?"]
    compliment_response = [f"I see what you're doing, calling me {a}!", "That's very sweet of you."]
    name_response = ["I'm Derek!", "<-- That's my name!"]
    action_response = [f"Not sure about {a}ing. Maybe another day...",
                       f"My tummy hurts today, I don't wanna go {a}ing"]
    alternatives = ["coding", "singing", "sleeping", "fighting"]
    b = random.choice(alternatives)
    if a in greeting:
        res = random.choice(greetings)
        return res
    elif a in activity:
        res = random.choice(action_response)
        return res
    elif a in weather:
        res = random.choice(weather_response)
        return res
    elif a in compliments:
        res = random.choice(compliment_response)
        return res
    elif a in name:
        res = random.choice(name_response)
        return res
    else:
        res = "Yea, {}ing is an option. Or we could do some {}".format(a, b)
    return res


def juan(a, b=None):
    activity = a + "ing"
    bad_things = ["fighting", "bickering", "yelling", "complaining"]
    good_things = ["singing", "hugging", "playing", "working"]
    answers = ["Yes, I do!", "I don't actually... It's a bit sad.", "You know what, I do!"]

    if activity in bad_things:
        return "YESS! Time for {}".format(activity)
    elif activity in good_things:
        return "What? {} sucks. Not doing that.".format(activity)
    elif a in questions:
        res = random.choice(answers)
        return res
    else:
        return "This is booooring..."


def petronella(a, b=None):
    happy_thoughts = ["flowers", "butterflies", "ponies", "ice-cream", "rollerblades"]
    b = random.choice(happy_thoughts)
    if a in action:
        res = "Hm, okay I could do some {}ing. But I find myself only thinking of {}...".format(a, b)
    else:
        res = "ZzZzZz...oh sorry, I fell asleep! What did you say now...{}?".format(a)
    return res


def conversation(a, b=None):
    response = ["I told you about this earlier...", "*yawn* you keep asking about the same stuff...,"
                                                    "Ask me somethinge else, please", "You already asked "
                                                                                      "about this!", "zZzZzZ..."]
    res = random.choice(response)
    return res


action = random.choice(["work", "play", "eat", "cry", "sleep", "fight"])
greeting = ["Hey", "hello", "yo", "hey", "Hello"]
weather = ["wind", "rain", "snow", "sunshine", "cloudy", "storm"]
compliments = ["pretty", "kind", "beautiful", "intelligent", "wise", "strong", "inspiring"]

sayings = ["pretty", "kind", "beautiful", "intelligent", "wise", "strong", "inspiring", "wind", "rain",
           "snow", "sunshine", "cloudy", "storm", "Hey", "hello", "yo", "hey", "Hello", "work", "play", "eat",
           "cry", "sleep", "fight"]
name = ["name"]
