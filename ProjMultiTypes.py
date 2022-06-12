import enum

class programmState (enum.Enum):        # Meant to run the program as a state machine (not relly implemented)
    startup = 0
    geometry_selection = 1
    geometry_cylinder_C = 2
    geometry_cylinder_A = 3
    save_file = 4
    close_file = 5
    Exit = 6
    


class Eerrors (enum.Enum):              # Meant to return cusom error codes (not implemented)
    startup = 0
    E_file_open_error = 1
    E_file_save_error = 2
    E_file_close_error = 3
    E_cylinder_parameter_error = 4