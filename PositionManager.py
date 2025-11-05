"""
Lucio Plancarte
"""

from HashTableQuadratic import HashTable

class PositionManager(HashTable):

    def __init__(self, table_size):
        """
        Constructor for the PositionManager class

        Parameters:
        - table_size (int): The size of the hash table used for positions
                            storage
        """
        super().__init__(table_size)


    def add_position(self, position_id, description):
        """
        Add a position to the position manager.

        Parameters:
        - position_id (int): The position ID
        - description (str): The description for the position
        """
        self.put(position_id,description)
        print(f"Position '{position_id} - {description}' added.")

    def get_position(self, position_id):
        """
        Search for a position by id and display the associted description.
        If the position is foundd it shows: "ID _____ is _____"
        Otherwise, it shows "Position ____ not found."

        Parameters:
        - position_id (str): The id to search for.
        """
        if self.search(position_id):
            print(f"ID {position_id} is {self.get(position_id)}")
        else:
            print(f"Position {position_id} not found.")

    def remove_position(self, position_id):
        """
        Removes a position by its position_id
        Its shows the message "Position _____ removed"
        """
        self.remove(position_id)
        print(f"Position {position_id} removed")


    def display_positions(self):
        """
        Display all positions in the position manager.
        It shows the message 'All positions' and the the content
        of the  HashTable
        """
        print("All Positions")
        print(self)

