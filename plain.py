def create_position(x, y):
    """
    Positions are represented by a tuple

    Receives values for coordinates and returns a position (x,y)

    int x int --> position
    """

    if isinstance(x, int) and isinstance(y, int):
        if x < 0 or y < 0:
            raise ValueError("create_position: invalid arguments")
        else:
            return (x,y)
    else:
        raise ValueError("create_position: invalid arguments")

def create_position_copy(p):
    """
    Receives a position and returns a copy of it

    position --> position
    """

    if not is_position(p):
        raise ValueError("create_position_copy: invalid arguments")

    p2 = p.copy()
    return p2

def get_pos_x(p):
    """
    Returns the x value of a position
    """

    return p[0]

def get_pos_y(p):
    """
    Returns the y value of a position
    """

    return p[1]

def is_position(arg):
    """
    If the given argument is a position, returns True

    universal --> bool
    """

    if not isinstance(get_pos_x(arg), int) or not isinstance(get_pos_y(arg), int):
        return False
    if get_pos_x(arg) < 0 or get_pos_y(arg) < 0:
        return False

    return True

def equal_positions(p1, p2):
    """
    If p1 and p2 correspond to the same position, returns True

    position x position --> bool
    """

    if get_pos_x(p1) == get_pos_x(p2) and get_pos_y(p1) == get_pos_y(p2):
        return True
    else:
        return False

def position_to_str(p):
    """
    Returns the chain '(x,y)' that represents p, x and y being it's coordinates

    position --> str
    """

    return f'({get_pos_x(p)}, {get_pos_y(p)})'

def get_adjacennt_positions(p):
    """
    Returns a tuple with the positions adjacent to p, clockwise

    position --> tuple
    """

    operations = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    adjacent = []
    x_p, y_p = get_pos_x(p), get_pos_y(p)

    for i in operations:
        x_i, y_i = get_pos_x(i), get_pos_y(i)
        if not x_p + x_i < 0 and not y_p + y_i < 0:
            adjacent.append((x_p + x_i, y_p + y_i))

    return tuple(adjacent)

def sort_positions(t):
    """
    Receives a sequence of positions and returns a tuple with those positions sorted accordingly
    to the plain reading order
    """

    return tuple(sorted(t , key=lambda coord: [coord[1], coord[0]]))

def create_animal(s, r, a):
    """
    Animals are represented as a dictionary with species, age, reproduction rate, hunger and feeding rate
    The last two only apply if the animal is a predator

    Receives a string and two positive integrers that represent the species's name, reproduction rate
    and fededing rate

    str x int x int --> animal
    """

    if not isinstance(s, str) or not isinstance(r, int) or not isinstance(a, int):
        raise ValueError("create_animal: invalid arguments")
    if r < 1 or a < 0 or len(s) < 1:
        raise ValueError("create_animal: invalid arguments")
    
    if a > 0: # predator
        return {"species":s,
        "age": 0,
        "rep_freq": r,
        "hunger": 0,
        "feed_freq": a}
    else: # prey
        return {"species":s,
        "age": 0,
        "rep_freq": r}

def create_copy_animal(a):
    """
    Receives an animal and creates a copy of it, leaving the original unaltered

    animal --> animal
    """
    if not is_animal(a):
        raise ValueError("create_copy_animal: invalid arguments")

    if is_predator(a):
        return {"species":get_species(a),
        "age": get_age(a),
        "rep_freq": get_rep_freq(a),
        "hunger": get_hunger(a),
        "feed_freq": get_feed_freq(a)}
    else: # prey
        return {"species":get_species(a),
        "age": get_age(a),
        "rep_freq": get_rep_freq(a)}

def get_species(a):
    """
    Returns the species of an animal
    
    animal --> str
    """

    return a["species"]

def get_rep_freq(a):
    """
    Returns the reproduction rate of an animal
    
    animal --> int
    """

    return a["rep_freq"]

def get_feed_freq(a):
    """
    Returns the feeding rate of an animal. If it's a prey, returns 0

    animal --> int
    """

    if "feed_freq" in a.keys():
        return a["feed_freq"]
    else:
        return 0

def get_age(a):
    """
    Returns the age of an animal
    
    animal --> int
    """

    return a["age"]

def get_hunger(a):
    """
    Returns the hunger of an animal. If it's a prey, returns 0

    animal --> int
    """

    if is_predator(a):
        return a["hunger"]
    else:
        return 0

def increase_age(a):
    """
    Modifies the animal, increasing it's age by 1

    animal --> animal
    """
    if is_animal(a):
        a["age"] += 1

    return a

def reset_age(a):
    """
    Sets an animal's age to 0

    animal --> animal
    """
    
    if is_animal(a):
        a["age"] = 0

    return a

def increase_hunger(a):
    """
    Modifies the animal, increasing it's hunger by 1. Does not modify preys

    animal --> animal
    """

    if is_predator(a):
        a["hunger"] += 1

    return a

def reset_hunger(a):
    """
    Set's an animal's hunger to 0. Does not modify preys

    animal --> animal
    """

    if is_predator(a):
        a["hunger"] = 0

    return a

def is_animal(arg):
    """
    Returns True only if the given argument corresponds to an animal

    universal --> bool
    """

    if not isinstance(arg, dict):
        return False

    for entry in arg.keys():
        if entry not in ["species", "age", "rep_freq", "hunger", "feed_freq"]: # Se alguma das keys do dicionario não for uma das 5 da lista, não é TAD animal
            return False

    if not ("species" in arg.keys() and "age" in arg.keys() and "rep_freq" in arg.keys()): # especia, age e rep_freq são entrys obrigatórias quer para preys como predators
        return False

    if "hunger" in arg.keys() or "feed_freq" in arg.keys(): # Caso seja um predador
        if not "hunger" in arg.keys() or not "feed_freq" in arg.keys(): # Tem que ter ambas as keys hunger e feed_freq
            return False

    if not isinstance(arg["species"], str):
        return False

    if not isinstance(arg["age"], int) or not isinstance(arg["rep_freq"], int):
        return False

    if "hunger" in arg.keys():
        if not isinstance(arg["hunger"], int) or not isinstance(arg["feed_freq"], int):
            return False

    return True

def is_predator(arg):
    """
    Returns True if the given argument corresponds to a predator

    universal - bool
    """

    if not is_animal(arg):
        return False

    if not "hunger" in arg.keys():
        return False
    
    return True

def is_prey(arg):
    """
    Returns True if the given argument corresponds to a prey

    universal - bool
    """

    if not is_animal(arg):
        return False

    if "hunger" in arg.keys():
        return False
    
    return True

def equal_animals(a1, a2):
    """
    If both animals have the same characteristics, returns True

    animal X animal --> bool
    """

    if not is_animal(a1) or not is_animal(a2):
        return False
    if is_predator(a1):
        if not is_predator(a2):
            return False
        elif get_feed_freq(a1) != get_feed_freq(a2) or get_hunger(a1) != get_hunger(a2):
            return False

    
    if is_prey(a1):
        if not is_prey(a2):
            return False

    if get_species(a1) != get_species(a2) or get_rep_freq(a1) != get_rep_freq(a2) or get_age(a1) != get_age(a2):
        return False

    return True

def animal_to_char(a):
    """
    Returns the first letter of the animal's species. Uppercase if it's a predator, lowercase if it's a prey

    animal --> str
    """

    if is_predator(a):
        return get_species(a)[0].upper()
    else:
        return get_species(a)[0].lower()

def animal_to_str(a):
    """
    Returns the animal through a specific character chain

    animal --> str
    """

    if is_predator(a):
        return f"{a['species']} [{a['age']}/{a['rep_freq']};{a['hunger']}/{a['feed_freq']}]"
    else:
        return f"{a['species']} [{a['age']}/{a['rep_freq']}]"

def is_animal_fertile(a):
    """
    If the animal reached it's reproduction age, returns True

    animal --> bool
    """
    if not is_animal(a):
        return False

    if get_rep_freq(a) > get_age(a):
        return False

    return True

def is_animal_starving(a):
    """
    If an animal's hunger is equal or superior to it's feeding frequency, returns True

    animal --> bool
    """

    if is_prey(a):
        return False

    if get_feed_freq(a) > get_hunger(a):
        return False

    return True

def reproduce_animal(a):
    """
    Receives an animal and returns a new animal of the same species with an age (and hunger if it's a preadtor) equal to 0
    Also modifies the animal received as argument, changing it's age to 0

    animal --> animal
    """

    new = create_copy_animal(a)
    reset_age(new)
    if is_predator(new):
        reset_hunger(new)
    
    reset_age(a)
    return new

def create_plain(d, r, a, p):
    """
    The plain is a dictionary with generate_mountain, rocks and animal_positions as keys
    The value of generate_mountain is the position of the rock located at the bottom right of the plain
    The value of rocks is a tuple with the positions that correspond to the rocks in the plain
    The value animal_positions is a dictionary where each entry corresponds to a position, where the animal
    is at and it's value is the animal there located

    d: position of the mountain in the bottom right corner
    r: rock positions
    a: animals
    p: animal positions

    Receives the position of the mountain in the bottom right corner, a tuple with the positions of all rocks,
    a tuple with the animals and another tuple with the positions of those animals

    Returns the plain that represents the map and the animals belonging to it

    It verifies the validity of the arguments, throwing a ValueError if they're invalid

    position x tuple x tuple x tuple --> plain    
    """

    pos = ()

    if not is_position(d):
        raise ValueError("create_plain: invalid arguments")

    if not isinstance(r, tuple) or not isinstance(a, tuple) or not isinstance(p, tuple):
        raise ValueError("create_plain: invalid arguments")

    if len(a) < 1:
        raise ValueError("create_plain: invalid arguments")

    if len(a) != len(p):
        raise ValueError("create_plain: invalid arguments")

    if len(r) > 0:
        for rock in r:
            if not is_position(rock):
                raise ValueError("create_plain: invalid arguments")

            if get_pos_x(rock) == 0 or get_pos_x(rock) == get_pos_x(d) or get_pos_y(rock) == 0 or get_pos_y(rock) == get_pos_y(d): # In case a rock is where a mountain would be
                raise ValueError("create_plain: invalid arguments")

    for position in p:
        if not is_position(position):
            raise ValueError("create_plain: invalid arguments")
        
        if get_pos_x(position) >= get_pos_x(d) or get_pos_y(position) >= get_pos_y(d):
            raise ValueError("create_plain: invalid arguments")

        if get_pos_x(position) == 0 or get_pos_x(position) == get_pos_x(d) or get_pos_y(position) == 0 or get_pos_y(position) == get_pos_y(d): # In case an animal is where a mountain would be
            raise ValueError("create_plain: invalid arguments")

        for rock in r:
            if equal_positions(rock, position): # Animal where a rock is
                raise ValueError("create_plain: invalid arguments")

        pos += (get_pos_x(position), get_pos_y(position)),

    for animal in a:
        if not is_animal(animal):
            raise ValueError("create_plain: invalid arguments")

    plain = {"generate_mountain": d,
    "rocks": r,
    "animal_positions": dict(list(zip(pos, a)))}    

    return plain

def create_copy_plain(m):
    """
    Receives a plain and returns a copy of it

    plain --> plain
    """

    if not is_plain(m):
        raise ValueError("create_copy_plain: invalid arguments")
        
    m2 = m.copy()
    return m2

def get_size_x(m):
    """
    Returns the dimension Ox of the plain

    plain --> int
    """

    return get_pos_x(create_position(get_pos_x(m["generate_mountain"]), get_pos_y(m["generate_mountain"]))) + 1

def get_size_y(m):
    """
    Returns the dimension Oy of the plain

    plain --> int
    """
    return get_pos_y(create_position(get_pos_x(m["generate_mountain"]), get_pos_y(m["generate_mountain"]))) + 1

def get_predator_count(m):
    """
    Returns the number of predators present in the plain
    
    plain --> int
    """

    predator_count = 0
    for pos in m["animal_positions"]:
        if is_predator(get_animal(m, create_position(pos[0], pos[1]))):
            predator_count += 1

    return predator_count

def get_prey_count(m):
    """
    Returns the number of preys present in the plain
    
    plain --> int
    """

    prey_count = 0
    for pos in m["animal_positions"]:

        if is_prey(get_animal(m, create_position(pos[0], pos[1]))):
            prey_count += 1

    return prey_count

def get_animal_positions(m):
    """
    Devolve um tuple com as posições ocupadas por animals, e ordenadas
    por ordem de leitura.

    Returns a tuple with the positions occupied by animals, sorted by reading order
    
    plain --> positions tuple
    """

    positions = []
    for pos in m["animal_positions"]:
        positions.append(pos)

    return tuple(sort_positions(positions))

def get_animal(m, p):
    """
    Returns the animal that is in the given position of the plain

    plain x position -> animal
    """
    if (get_pos_x(p), get_pos_y(p)) in m["animal_positions"]:
        return m["animal_positions"][(get_pos_x(p), get_pos_y(p))]

    return m

def delete_animal(m, p):
    """
    Modifies the plain, deleting the animal in the given position
    
    plain X position -> plain
    """
    
    if (get_pos_x(p), get_pos_y(p)) in m["animal_positions"]:
        del m["animal_positions"][(get_pos_x(p), get_pos_y(p))]

    return m

def move_animal(m, p1, p2):
    """
    Modifies the plain, movimg the animal from p1 to p2

    plain x position x position --> plain
    """

    m["animal_positions"][(p2[0], p2[1])] = m["animal_positions"][(p1[0], p1[1])]
    del m["animal_positions"][(p1[0], p1[1])]

    return m

def add_animal(m, a, p):
    """
    Modifies the plain, adding an animal to the given position

    plain x animal x position --> plain
    """

    m["animal_positions"][p] = a

    return m

def is_plain(m):
    """
    Returns True if the given argument corresponds to a plain

    universal --> bool
    """

    if not isinstance(m, dict):
        return False

    for entry in m.keys():
        if entry not in ["generate_mountain", "rocks", "animal_positions"]:
            return False

    if not ("generate_mountain" in m.keys() and "rocks" in m.keys() and "animal_positions" in m.keys()):
        return False

    if not is_position(m["generate_mountain"]):
        return False

    for rock in m["rocks"]:
        if not is_position(rock):
            return False

    if not isinstance(m["animal_positions"], dict):
        return False

    if not is_position(m["generate_mountain"]):
        return False
    
    for rock in m["rocks"]:
        if not is_position(rock):
            return False

    for animal in m["animal_positions"]:
        if not is_position(animal):
            return False

    if len(m["animal_positions"]) < 1:
        return False

    return True

def is_position_animal(m, p):
    """
    Returns true if the given position is occupied by an animal

    plain x position --> bool
    """

    if not p in m["animal_positions"].keys():
        return False

    return True

def is_position_obstacle(m, p):
    """
    Returns true if the given position is occupied by a mountain or a rock

    plain x position --> bool
    """
    
    if p in m["rocks"]:
        return True

    if get_pos_x(p) == 0 or get_pos_x(p) == m["generate_mountain"][0] or get_pos_y(p) == 0 or get_pos_y(p) == m["generate_mountain"][1]:
        return True
    
    return False

def is_position_free(m, p):
    """
    Returns True if the position is not occupied

    plain x position --> bool
    """

    if is_position_animal(m, p) or is_position_obstacle(m, p):
        return False

    return True

def equal_plains(p1, p2):
    """
    Returns True if both plains are equal

    plain X plain --> bool
    """

    if is_plain(p1) and is_plain(p2):
        if p1 == p2:
            return True
    
    return False

def plain_to_str(m):
    """
    Returns a string of characters that represents the given plain
    The corners are shown as "+", mountains as "-" or "|", animals are represented with the letter from animal_to_char,
    rocks are represented by "@"

    plain --> str
    """

    string = ''
    for j in range(get_size_y(m)):
        for i in range(get_size_x(m)):
            if i == 0 and j == 0:
                string += '+'
            elif i == get_pos_x(m["generate_mountain"]) and j == 0:
                string += '+'
            elif i == 0 and j == get_pos_y(m["generate_mountain"]):
                string += '+'
            elif i == get_pos_x(m["generate_mountain"]) and j == get_pos_y(m["generate_mountain"]):
                string += '+'
            elif is_position_animal(m, (i,j)):
                string += animal_to_char(get_animal(m, (i,j)))
            elif j == 0 or j == get_pos_y(m["generate_mountain"]):
                string += '-'
            elif i == 0 or i == get_pos_x(m["generate_mountain"]):
                string += '|'
            elif is_position_free(m, (i,j)):
                string += '.'
            elif is_position_obstacle(m, (i,j)):
                string += '@'
            elif is_position_animal(m, (i,j)):
                string += animal_to_char(get_animal(m, (i,j)))
        
        string += '\n'

    return string.strip()

def obtain_numeric_value(m, p):
    """
    Returns the numeric value associated to the plain's reading order of the given position

    plain X position --> int
    """

    return (get_pos_x(m["generate_mountain"]) + 1) * get_pos_y(p) + get_pos_x(p)

def get_move(m, p):
    """
    Returns the next positiob of the animal on the given plain, according to move rules

    Those rules are:
        - Animals can only move up, down, left or right
        - They can't occupy positions occupied by mountains or rocks
        - Predators try to move to an adjacent position that contains a prey. If none exists,
          tries to move to an empty one. If no moves are possible, it does not move
        - Preys try to move to an adjacent position that is empty
        - To choose between multiple options, we enumerate all the possible ones, starting at 0
          and moving clockwise from 12
        - The chosen position is the one with index equal to N % p, N being the current position's
          index and p the number of possible new positions

    plain X position --> position    
    """

    with_prey = []
    free_pos = []
    possible = {}
    adjacent = get_adjacennt_positions(p)

    for position in adjacent:
        if not is_position_obstacle(m,position):
            if is_position_animal(m,p):
                if is_predator(get_animal(m, p)):
                    if is_position_animal(m, position):
                        if is_prey(get_animal(m, position)):
                            with_prey.append(position)

        if not is_position_obstacle(m,position):
            if is_position_free(m, position):
                free_pos.append(position)

    if len(with_prey) == 1:
        return with_prey[0]
    elif len(with_prey) > 1:
        for i in range(len(with_prey)):
            possible[i] = with_prey[i]
    elif len(free_pos) == 1:
        return free_pos[0]
    elif len(free_pos) > 1:
        for i in range(len(free_pos)):
            possible[i] = free_pos[i]
    else:
        return p


    num_value = obtain_numeric_value(m, p)

    selected = num_value % len(possible)

    return possible[selected]

def generation(m):
    """
    Modifies the given plain according to the evolution corresponding to a full generation
    and returns the plain itself
    A full generation is obtained apllying the corresponding move to each animal given the conditions
    and reproducing it, eating or killing according to the described rules
    
    plain -> plain
    """

    if not is_plain(m):
        raise ValueError("generation: invalid arguments")

    positions = ()
    for animal in m["animal_positions"]:
        positions += animal,

    used = ()
    positions2 = sort_positions(positions)
    for anim in positions2:
        if not any(equal_positions(anim, moveus) for moveus in used):
            animal = get_animal(m, anim)
            increase_hunger(animal)
            increase_age(animal)
            move = get_move(m, anim)
            if not equal_positions(anim, move):
                if is_predator(animal):
                    if is_position_animal(m, move):
                        used += move,

                        reset_hunger(animal)
                        delete_animal(m, move)
                        move_animal(m, anim, move)
                        if is_animal_fertile(animal):
                            add_animal(m, reproduce_animal(animal), anim)
                    else:
                        move_animal(m, anim, move)
                        if is_animal_fertile(animal):
                            add_animal(m, reproduce_animal(animal), anim)
                
                else: # prey
                    move_animal(m, anim, move)
                    if is_animal_fertile(animal):
                        add_animal(m, reproduce_animal(animal), anim)

                if is_animal_starving(animal):
                    delete_animal(m, move)

            else:
                if is_animal_starving(animal):
                    delete_animal(m, move)

    return m
    
def simula_ecossistema(f, g, v):
    """
    It's the principal funciton that allows to simulate the ecossystem of a plain
    
        f: corresponds to a text file with the configuration for the simulation
        g: number of generations to simulate
        v: changes between verbose and quiet modes
            - On quiet mode, the plain, predator count and prey count are shown at the start of the simulation
              and again at the end of it
            - On verbose mode, output is only shown if either the predator or prey count changes

    str X int X bool --> tuple
    """

    if not isinstance(f, str):
        raise ValueError('simula_ecossistema: invalid arguments')

    if not isinstance(g, int):
        raise ValueError('simula_ecossistema: invalid arguments')

    if not isinstance(v, bool):
        raise ValueError('simula_ecossistema: invalid arguments')

    animals = []
    animal_positions = []
    created = []

    lines = open(f, "r").readlines()
    lines2 = tuple(linha.strip() for linha in lines)

    for i in range(2, len(lines2)):
        tuple = eval(lines2[i])
        animals.append((tuple[0], tuple[1], tuple[2]))
        animal_positions.append(tuple[3])

    for i in range(len(animals)):
        created.append(create_animal(animals[i][0], animals[i][1], animals[i][2]))

    rocks = ()
    for rock in eval(lines2[1]):
        rocks += (create_position(rock[0], rock[1])),

    plain = create_plain(eval(lines2[0]), rocks, tuple(created), tuple(animal_positions))
    predators, preys = get_predator_count(plain), get_prey_count(plain)
    print(f"Predators: {predators} vs Preys: {preys} (Gen. 0)")
    print(plain_to_str(plain))
    for i in range(1, g + 1):
        generation(plain)
        if v:
            if get_predator_count(plain) != predators or get_prey_count(plain) != preys:
                predators, preys = get_predator_count(plain), get_prey_count(plain)
                print(f"Predators: {predators} vs Preys: {preys} (Gen. {i})")
                print(plain_to_str(plain))

    if not v:
        predators, preys = get_predator_count(plain), get_prey_count(plain)
        print(f"Predators: {predators} vs Preys: {preys} (Gen. {g})")
        print(plain_to_str(plain))

    return (predators, preys)