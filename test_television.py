import unittest
from television import Television

class MyTestCase(unittest.TestCase):

#all but one method currently does not return values (they will return None).
#Check for changes in output with str(self.tv1)
#could use 'assertTrue()' for checking bool values

    def setUp(self):
        self.tv1 = Television()

    def tearDown(self):
        del self.tv1

    def test_init(self):
        #first test checks power, channel, and volume. Second test checks mute status
        self.assertEqual(str(self.tv1), 'Power = False, Channel = 0, Volume = 0')
        self.assertEqual(self.tv1.get_muted(), False)

    def test_power(self):
        #checks for power to be turned off and then checks for power to be off
        self.tv1.power()
        self.assertEqual(str(self.tv1), 'Power = True, Channel = 0, Volume = 0')
        self.tv1.power()
        self.assertEqual(str(self.tv1), 'Power = False, Channel = 0, Volume = 0')

    def test_mute(self):
        #checks muting after tv is turned on
        self.tv1.power()
        self.tv1.mute()
        self.assertEqual(self.tv1.get_muted(), True)

        #checks if mute status changes from False if volume is turned down from 0
        self.tv1.volume_down()
        self.assertEqual(self.tv1.get_muted(), False)

        #checks for mute status to work (True) after volume is greater than 0
        self.tv1.volume_up()
        self.tv1.mute()
        self.assertEqual(self.tv1.get_muted(), True)

        #checks for mute status to be True after turning volume from 1 to 0 and then muting
        self.tv1.volume_down()
        self.tv1.mute()
        self.assertEqual(self.tv1.get_muted(), True)


    def test_channel_up(self):
        #checks for power off and channel up to not change the channel
        self.tv1.channel_up()
        self.assertEqual(str(self.tv1), 'Power = False, Channel = 0, Volume = 0')

        #checks for the channel_up to work
        self.tv1.power()
        self.tv1.channel_up()
        self.assertEqual(str(self.tv1), 'Power = True, Channel = 1, Volume = 0')

        #checks for channel to go past the max and back to the min channel
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        self.assertEqual(str(self.tv1), 'Power = True, Channel = 0, Volume = 0')


    def test_channel_down(self):
        # checks for power off and channel down to not change the channel
        self.tv1.channel_down()
        self.assertEqual(str(self.tv1), 'Power = False, Channel = 0, Volume = 0')

        # checks for the channel_down to go lower than the min and be set at the max channel
        self.tv1.power()
        self.tv1.channel_down()
        self.assertEqual(str(self.tv1), 'Power = True, Channel = 3, Volume = 0')

        # checks for channel to go back to the min
        self.tv1.channel_down()
        self.tv1.channel_down()
        self.tv1.channel_down()
        self.assertEqual(str(self.tv1), 'Power = True, Channel = 0, Volume = 0')

    def test_volume_down(self):
        # checks for power off and volume_down do not change anything
        self.tv1.volume_down()
        self.assertEqual(str(self.tv1), 'Power = False, Channel = 0, Volume = 0')

        # checks for power on and volume_down to work
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        self.assertEqual(str(self.tv1), 'Power = True, Channel = 0, Volume = 1')

        # checks that volume_down doesn't go beyond the min_volume
        self.tv1.volume_down()
        self.tv1.volume_down()
        self.tv1.volume_down()
        self.tv1.volume_down()
        self.assertEqual(str(self.tv1), 'Power = True, Channel = 0, Volume = 0')


    def test_volume_up(self):
        # checks for power off and volume up to not change anything
        self.tv1.volume_up()
        self.assertEqual(str(self.tv1), 'Power = False, Channel = 0, Volume = 0')

        #checks for power on and volume_up to work
        self.tv1.power()
        self.tv1.volume_up()
        self.assertEqual(str(self.tv1), 'Power = True, Channel = 0, Volume = 1')

        #checks that volume_up doesn't go beyond the max_volume
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.assertEqual(str(self.tv1), 'Power = True, Channel = 0, Volume = 2')



if __name__ == '__main__':
    unittest.main()
