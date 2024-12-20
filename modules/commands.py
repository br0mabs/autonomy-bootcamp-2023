"""
BOOTCAMPERS DO NOT MODIFY THIS FILE.

Different commands to send to the drone.
"""

import enum


class Command:
    """
    Commanding the drone.

    Any of the following methods will create a Command object with the correct command:

    * Command.create_null_command()
    * Command.create_set_relative_destination_command()
    * Command.create_halt_command()
    * Command.create_land_command()

    The Command object can then be used (e.g. passing it to the drone).
    """

    class CommandType(enum.Enum):
        """
        Different types of commands.
        """

        NULL = 0  # Stay the course
        SET_RELATIVE_DESTINATION = 1  # Move relative to current position
        HALT = 2  # Stop the drone ASAP
        LAND = 3  # Land at current position

    __create_key = object()

    @classmethod
    def create_null_command(cls) -> "Command":
        """
        Command that has no effect (default).
        """
        return Command(
            cls.__create_key,
            Command.CommandType.NULL,
            0.0,
            0.0,
        )

    @classmethod
    def create_set_relative_destination_command(
        cls, relative_x: float, relative_y: float
    ) -> "Command":
        """
        Command to set drone destination.
        Drone must be in halted state.
        relative is distance from current position of the drone in metres.
        """
        return Command(
            cls.__create_key,
            Command.CommandType.SET_RELATIVE_DESTINATION,
            relative_x,
            relative_y,
        )

    @classmethod
    def create_halt_command(cls) -> "Command":
        """
        Command to halt the drone.
        """
        return Command(
            cls.__create_key,
            Command.CommandType.HALT,
            0.0,
            0.0,
        )

    @classmethod
    def create_land_command(cls) -> "Command":
        """
        Command to land the drone.
        Drone must be in halted state.
        """
        return Command(
            cls.__create_key,
            Command.CommandType.LAND,
            0.0,
            0.0,
        )

    def __init__(
        self,
        class_private_create_key: object,
        command_type: CommandType,
        relative_x: float,
        relative_y: float,
    ) -> None:
        """
        Private constructor, use create() method.
        """
        assert class_private_create_key is Command.__create_key, "Use create() method"

        self.__command_type = command_type
        self.__relative_x = relative_x
        self.__relative_y = relative_y

    def get_command_type(self) -> CommandType:
        """
        Getter.
        """
        return self.__command_type

    def get_relative_destination(self) -> "tuple[float, float]":
        """
        Getter.
        """
        return self.__relative_x, self.__relative_y

    def __repr__(self) -> str:
        """
        To string.
        """
        representation = f"Command: {self.__command_type}"

        if self.__command_type == Command.CommandType.SET_RELATIVE_DESTINATION:
            representation += f" {self.get_relative_destination()}"

        return representation
