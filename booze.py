bottles = [
    # alcoholics
    {"name": "Tequila", "value": "teq"},
    {"name": "Cachaca", "value": "cacha"},
    {"name": "Vodka", "value": "vodka"},
    {"name": "Rum (weiß)", "value": "rum"},
    {"name": "Pfirsichlikör", "value": "peach"},
    {"name": "Blue Curacao", "value": "blue"},

    # mixables
    {"name": "Orangensaft", "value": "osaft"},
    {"name": "Grenadine", "value": "grena"},
    {"name": "Limettensaft", "value": "lime"},
    {"name": "Ananassaft", "value": "pine"},
    {"name": "Coca Cola", "value": "cola"},
    {"name": "Cranberrysaft", "value": "cran"}
]

# ALL MIXES ARE TO BE TESTED FOR TASTE AND AMOUNT
mixes = [
    # ingredient amount in "ml"
    # longdrinks should be around 350-400ml
    # Langtrink = Longdrink, SchwanzSchwanz = Cocktails, Fahrer = Alkoholfrei

    # recipes might use dashes = 1 ml, gotta try it
    {
        "name": "A Kick in the Crotch",
        "ingredients": {"vodka": 20, "blue": 15, "cran": 15},
        "type": "Shooter"  # to be replaced with dumb german expression
    },
    {
        "name": "Ananascocktail",
        "ingredients": {"pine": 120, "osaft": 90},
        "type": "Fahrer"
    },
    {
        "name": "Rum Cola",
        "ingredients": {"rum": 40, "cola": 160},
        "type": "Langtrink"
    },
    {
        "name": "Black Thunder",
        "ingredients": {"vodka": 40, "blue": 20, "cola": 160},
        "type": "Langtrink"
    },
    {
        "name": "Blue Lagoon",
        "ingredients": {"rum": 30, "blue": 20, "pine": 70},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Blue Tequila",
        "ingredients": {"blue": 20, "teq": 20},
        "type": "Extravaganz"
    },
    {
        "name": "Cape Cod",
        "ingredients": {"vodka": 40, "cran": 160},
        "type": "Langtrink"
    },
    {
        "name": "Vodka Cola",
        "ingredients": {"vodka": 20, "cola": 180},
        "type": "Langtrink"
    },
    {
        "name": "Emerald Dream",
        "ingredients": {"vodka": 50, "blue": 20, "osaft": 100},
        "type": "Langtrink"
    },
    {
        "name": "Finnish Virgin",
        "ingredients": {"vodka": 50, "blue": 10, "osaft": 20, "lime": 10},
        "type": "Langtrink"
    },
    {
        "name": "Fireman's Sour",
        "ingredients": {"rum": 40, "lime": 30, "grena": 15},
        "type": "Langtrink"
    },
    {
        "name": "Fuzzy Navel",
        "ingredients": {"osaft": 150, "peach": 30, "vodka": 30},
        "type": "Langtrink"
    },
    {
        "name": "Green Devil",
        "ingredients": {"blue": 10, "osaft": 20, "rum": 20},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Green Eyes",
        "ingredients": {"vodka": 30, "blue": 30, "osaft": 120},
        "type": "Langtrink"
    },
    {
        "name": "Green Pineapple",
        "ingredients": {"teq": 30, "pine": 60, "blue": 20},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Grüne Witwe",
        "ingredients": {"blue": 40, "osaft": 160},
        "type": "Langtrink"
    },
    {
        "name": "Hund und Katze",
        "ingredients": {"vodka": 40, "blue": 40, "rum": 40, "grena": 20, "lime": 20, "pine": 100, "osaft": 100},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Madras",
        "ingredients": {"vodka": 50, "osaft": 150, "cran": 150},
        "type": "Langtrink"
    },
    {
        "name": "Mars Explosion",
        "ingredients": {"grena": 10, "osaft": 100, "vodka": 20, "rum": 20},
        "type": "Extravaganz"
    },
    {
        "name": "Mexican Screwdriver",
        "ingredients": {"teq": 40, "osaft": 100},
        "type": "Langtrink"
    },
    {
        "name": "Monkey Wrench",
        "ingredients": {"rum": 40, "pine": 310},
        "type": "Langtrink"
    },
    {
        "name": "Pacific Sunrise",
        "ingredients": {"teq": 20, "blue": 20, "lime": 20},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Peach Sling",
        "ingredients": {"peach": 40, "vodka": 20, "osaft": 60, "grena": 100},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Pink Pussycat",
        "ingredients": {"vodka": 40, "grena": 1, "pine": 309},
        "type": "Langtrink"
    },
    {
        "name": "Purple Rain",
        "ingredients": {"blue": 100, "cran": 100, "vodka": 100},
        "type": "Extravaganz"
    },
    {
        "name": "Revolicion",
        "ingredients": {"teq": 20, "vodka": 20, "osaft": 80},
        "type": "Langtrink"
    },
    {
        "name": "Rum Orange",
        "ingredients": {"rum": 40, "osaft": 310},
        "type": "Langtrink"
    },
    {
        "name": "Russian Flag",
        "ingredients": {"grena": 10, "blue": 10, "vodka": 10},
        "type": "Shooter"
    },
    {
        "name": "Save Drive To Me",
        "ingredients": {"osaft": 60, "lime": 30, "grena": 20, "pine": 100},
        "tpye": "Fahrer"
    },
    {
        "name": "Schicksalsschlag",
        "ingredients": {"teq": 15, "rum": 15, "blue": 15, "osaft": 150},
        "type": "Langtrink"
    },
    {
        "name": "Screwdriver",
        "ingredients": {"vodka": 50, "osaft": 300},
        "type": "Langtrink"
    },
    # Sex on the Beach are to be compared with each other, keep 2 versions max
    {
        "name": "Sex on the Beach V1",
        "ingredients": {"vodka": 40, "cran": 80, "peach": 20, "osaft": 80},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Sex on the Beach V2",
        "ingredients": {"vodka": 40, "peach": 20, "pine": 80, "cran": 80, "grena": 1},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Sex on the Beach V3",
        "ingredients": {"vodka": 40, "peach": 40, "grena": 30, "pine": 110},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Sex on the Beach V4",
        "ingredients": {"vodka": 40, "peach": 20, "osaft": 80, "cran": 80, "grena": 10},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Sex on the Beach V5",
        "ingredients": {"vodka": 40, "cran": 60, "peach": 20, "osaft": 50, "pine": 50},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Sex on the Beach V6",
        "ingredients": {"vodka": 20, "grena": 30, "peach": 20, "osaft": 60, "pine": 40},
        "type": "SchwanzSchwanz"
    },
    # fck Sex on the Beach tbh
    {
        "name": "Soft Poison",
        "ingredients": {"blue": 20, "osaft": 160},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Spooky Juice",
        "ingredients": {"vodka": 30, "blue": 20, "grena": 10, "osaft": 100},
        "type": "Langtrink"
    },
    {
        "name": "Sunset",
        "ingredients": {"cola": 70, "osaft": 100, "grena": 30},
        "type": "Fahrer"
    },
    {
        "name": "Sweety",
        "ingredients": {"pine": 80, "osaft": 100, "grena": 20},
        "type": "Fahrer"
    },
    {
        "name": "Tequila",
        "ingredients": {"teq": 30},
        "type": "Shooter"
    },
    {
        "name": "The Waikiki",
        "ingredients": {"vodka": 40, "pine": 120},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Vodka Cranberry",
        "ingredients": {"vodka": 40, "cran": 120},
        "type": "Langtrink"
    },
    {
        "name": "Vokda Gimlet",
        "ingredients": {"vodka": 40, "lime": 20},
        "type": "SchwanzSchwanz"
    },
    {
        "name": "Vodka Sunrise",
        "ingredients": {"vodka": 40, "teq": 30, "osaft": 60, "grena": 10},
        "type": "Langtrink"
    }
]
