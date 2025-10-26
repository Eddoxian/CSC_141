def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append(f"The Great {magician.title()}")
    return great_magicians

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ["houdini", "dynamo", "merlin"]
great_magicians = make_great(magicians)
show_magicians(great_magicians)