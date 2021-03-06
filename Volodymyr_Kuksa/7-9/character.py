import threading
import dungeon_game_decorators
import dungeon_game_exceptions


class Character:
    """
    Basic character class.
    """

    def __init__(self, name):
        """
        Character constructor.

        :param name: name of the character.
        """
        self.__character_name = name
        self.__bag = 0
        self.__hp = 3

        self.hp_lock = threading.Lock()

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def increment_bag(self, step=1):
        """
        Increment __bag by step.

        :param step: incremental step.
        :type step: int.

        :return: None.
        """
        self.__bag += step

        if self.bag >= 3:
            raise dungeon_game_exceptions.PlayerBagFullError

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def decrement_hp(self, step=1):
        """
        Decrement __hp by step.

        :param step: decremental step.
        :type step: int.

        :return: None.
        """
        self.hp_lock.acquire()

        self.__hp -= step

        self.hp_lock.release()

        if not self.__hp:
            raise dungeon_game_exceptions.PlayerDiedError

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def is_alive(self):
        """
        Return True if character has more than 0 hit points.

        :return: True if character has more than 0 hit points, False otherwise.
        :rtype: bool.
        """
        return self.__hp > 0

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def is_bag_full(self):
        """
        Return True if character has 3 or more treasures in bag.

        :return: True if character has 3 or more treasures in bag, False otherwise.
        :rtype: bool.
        """
        return self.__bag >= 3

    @property
    def character_name(self):
        """
        Getter for name.

        :return: name of the character.
        :rtype: str.
        """
        return self.__character_name

    @character_name.setter
    def character_name(self, new_name):
        """
        Setter for name.

        :param new_name: new name for the character.
        :type new_name: str.
        """
        self.__character_name = new_name

    @property
    def hp(self):
        """
        Getter for hp.

        :return: hp.
        :rtype: int.
        """
        return self.__hp

    @hp.setter
    def hp(self, new_hp):
        """
        Setter for hp.

        :param new_hp: new value of hp.
        :type new_hp: int.
        """
        self.__hp = new_hp

    @property
    def bag(self):
        """
        Getter for bag.

        :return: bag.
        :rtype: int.
        """
        return self.__bag

    @bag.setter
    def bag(self, new_bag):
        """
        Setter for bag.

        :param new_bag: new value of bag.
        :type new_bag: int.
        """
        self.__bag = new_bag
