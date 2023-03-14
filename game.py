"""
Module for a game 5
"""
class Room:
    """
    Represents a room in the game.
    """
    def __init__(self, type):
        """
        Initializes a Room object.

        Parameters:
        - type (str): the type of room.

        Attributes:
        - type (str): the type of room.
        - description (str): the description of the room.
        - character (obj): the character in the room.
        - item (obj): the item in the room.
        - neighbor_rooms (dict): the neighboring rooms and ways to get to them.
        """
        self.type = type
        self.description = None
        self.character = None
        self.item = None
        self.neighbor_rooms = {}

    def set_description(self, description):
        """
        Sets the description of the room.

        Parameters:
        - description (str): the description of the room.
        """
        self.description = description  

    def get_details(self):
        """ 
        Prints the details of the room.
        """
        print(self.type)
        print("--------------------")
        print(self.description)
        for room, way in self.neighbor_rooms.items():
            print(f"The {room} is {way}")

    def __str__(self):
        """
        Returns the string representation of the room.

        Returns:
        - str: the type of room.
        """
        return f"{self.type}"

    def link_room(self, room, way):
        """
        Links the room to a neighboring room.

        Parameters:
        - room (obj): the neighboring room to link to.
        - way (str): the way to get to the neighboring room.
        """
        self.neighbor_rooms[room] = way

    def set_character(self, character):
        """
        Sets the character in the room.

        Parameters:
        - character (obj): the character in the room.
        """
        self.character = character

    def get_character(self):
        """
        Returns the character in the room.

        Returns:
        - obj: the character in the room.
        """
        return self.character

    def get_item(self):
        """
        Returns the item in the room.

        Returns:
        - obj: the item in the room.
        """
        return self.item

    def set_item(self, item):
        """
        Sets the item in the room.

        Parameters:
        - item (obj): the item in the room.
        """
        self.item = item

    def move(self, way):
        """
        Moves to a neighboring room.

        Parameters:
        - way (str): the way to get to the neighboring room.

        Returns:
        - obj: the neighboring room.
        - obj: the current room if there is no neighboring room in the specified way.
        """
        for i in self.neighbor_rooms.items():
            if i[1] == way:
                return i[0]
        return self


class Enemy:
    """Represents an enemy character in the game."""
    defeated = 0
    def __init__(self, name, description):
        """init"""
        self.name = name
        self.description = description
        self.weakness = None
        self.conversation = None

    def set_weakness(self, weakness):
        """set_weakness"""
        self.weakness = weakness

    def set_conversation(self, conversation):
        """set_conversation"""
        self.conversation = conversation

    def fight(self, item):
        """fight"""
        if item == self.weakness:
            return True
        return False
    def get_defeated(self):
        """
        get defeated
        """
        Enemy.defeated += 1
        return  Enemy.defeated
    def describe(self):
        """describe a person"""
        print(f"{self.name} is here!")
        print(self.description)
    def talk(self):
        """dialoge"""
        print(f"[{self.name} says]: {self.conversation}")

class Item:
    """Item class"""
    def __init__(self, name):
        """init"""
        self.name = name
        self.description = None

    def set_description(self, description):
        """set description"""
        self.description = description

    def get_name(self):
        """get name"""
        return self.name
    
    def describe(self):
        """describe"""
        print(f'The {self.name} is here - {self.description}')
