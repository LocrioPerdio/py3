import math

#TODO recortar espacios despues del split

def valid_syntax(coords: list[str]) -> bool:
    for coord in coords:
        if len(coord) == 3:
            if coord[0].isdigit() and coord[1] == "." and coord[2].isdigit():
                check_syntax = True
        else:
            check_syntax = False
            raise SyntaxError("Invalid syntax")
    return(check_syntax)


def get_player_pos() -> tuple:
    while(True):
        user_input: str = input("Enter new coordinates as floats in format 'x,y,z':")
        coords: list[str] = user_input.split(",")
        final: list[float] = []
        try:
            valid_syntax(coords)
        except SyntaxError as e:
            print(e)
        for coord in coords:
            try:
                coord = float(coord)
                final.append(coord)
            except ValueError as e:
                print(f"Error on parameter {coord}: could no convert string to float: '{coord}'")
        if len(final) == 3:
            break
    return tuple(final)

if __name__ == "__main__":
    print ("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_tuple: tuple = get_player_pos()
    print(f"Got a first tuple: {first_tuple}")

