import random

def gen_pass(pass_length):
    elements = "+-/*!&$?=@<>#" 
    password = "" 

    for i in range(pass_length):                 # dla każdej pozycji w haśle?
        password += random.choice(elements)  # dodaj losowy znak

    return password                         # zwraca goteowe hasło


# Losuje jedną emotkę z listy emoji
def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"] # lista emoteke
    return random.choice(emoji) # zraca losową emotkę

# Symuluje rzut monetą
def flip_coin():
    flip = random.randint(0, 2)      # Losuje liczbę 0,1 lub 2

    if flip == 0:                # Jeśli wylosowano 0
        return "Orzeł"            # Zwraca tekst 'Orzeł'
    else:                        # Jeśli wylosowano 1 lub 2
        return "Reszka"              # Zwraca tekst 'Reszka'
    
def gen_random_number():
    random_number = gen_random_number()  
    return random.randint(1, 100)