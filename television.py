class Television:
    """
    television class has the following methods:
    init, power, mute, channel_up, channel_down, volume_up, volume_down, str
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        sets up the television as off, not muted, volume 0, and channel 0
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def get_muted(self) -> bool:
        """
        used to access the mute status of the tv
        :return: boolean True if muted and False if unmuted
        """
        return self.__muted

    def power(self) -> None:
        """
        Turns the television on when off
        and off when on
        :return: returns True if on and False if off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Mutes and unmutes the television when turned on
        :return: returns True if unmuted or False if muted
        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """
        Turns the channel up to the max and then back to the min
        :return: returns the new channel number as an int
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Turns the channel down to the min and then back to the max
        :return: returns the new channel number as an int
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Turns the volume up one int at a time up until the max volume
        :return: returns the new volume as an int
        """
        if self.__status:
            self.__muted = False
            if self.__volume == Television.MAX_VOLUME:
                return
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Turns the volume down one int at a time down until the min volume
        :return: returns the new volume as an int
        """
        if self.__status:
            self.__muted = False
            if self.__volume == Television.MIN_VOLUME:
                return
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        displays the current status of the television with the current power, channel, and volume
        :return: returns a string of the current status
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'




