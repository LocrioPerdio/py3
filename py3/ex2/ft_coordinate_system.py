import math


def valid_syntax(coords: list[str]) -> bool:
    if len(coords) == 3:
        check_syntax = True
    else:
        check_syntax = False
        raise SyntaxError("Invalid syntax")
    return check_syntax


def get_player_pos() -> tuple:
    while True:
        user_input: str = input("Enter new coordinates as"
                                " floats in format 'x,y,z':")
        coords: list[str] = user_input.split(",")
        final: list[float] = []
        try:
            valid_syntax(coords)
            for coord in coords:
                try:
                    coord = float(coord)
                    final.append(coord)
                except ValueError:
                    print(f"Error on parameter {coord}:"
                          "could no convert string to float: '{coord}'")
        except SyntaxError as e:
            print(e)
        if len(final) == 3:
            break
    return tuple(final)


def get_distance(dest: tuple, origin: tuple) -> float:
    distance = math.sqrt((dest[0] - origin[0])**2 +
                         (dest[1] - origin[1])**2 + (dest[2] - origin[2])**2)
    distance = round(distance, 4)
    return distance


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_tuple: tuple = get_player_pos()
    print(f"Got a first tuple: {first_tuple}")
    print(f"It includes: X={first_tuple[0]}, Y={first_tuple[1]},"
          f" Z={first_tuple[2]}")
    print("Distance to center: ", end="")
    print(get_distance(first_tuple, [0, 0, 0]))
    print()
    print("Get a second set of coordinates")
    second_tuple: tuple = get_player_pos()
    print("Distance between the 2 set of coordinates: ", end="")
    print(get_distance(first_tuple, second_tuple))
