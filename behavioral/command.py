import time
from abc import abstractmethod


class TVRemote(object):
    '''Invoker'''
    def __init__(self) -> None:
        self._commands = {}
        self._history = []

    def setCommand(self, command_name, command):
        self._commands[command_name] = command

    def executeCommand(self, command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
            self._history.append((time.time(), command_name))
        else:
            print(f"There isn't `{command_name}` command in TV remote.")

    def get_last_command(self):
        if len(self._history) > 0:
            command = self._history[-1]
            print(f'Last command: {command[1]}, timestamp: {command[0]}')


class CommandInterface(object):
    @abstractmethod
    def execute(self):
        ...


class VolumeUpCommand(CommandInterface):
    def __init__(self, receiver) -> None:
        self.receiver = receiver

    def execute(self):
        self.receiver.volume_up()


class VolumeDownCommand(CommandInterface):
    def __init__(self, receiver) -> None:
        self.receiver = receiver

    def execute(self):
        self.receiver.volume_down()


class PlayCommand(CommandInterface):
    def __init__(self, receiver, video) -> None:
        self.receiver = receiver
        self.video = video

    def execute(self):
        self.receiver.play(self.video)


class PauseCommand(CommandInterface):
    def __init__(self, receiver) -> None:
        self.receiver = receiver

    def execute(self):
        self.receiver.pause()


class TV(object):
    '''Receiver'''
    @staticmethod
    def volume_up():
        print("Volume up !!!")

    @staticmethod
    def volume_down():
        print("Volume down !!!")

    @staticmethod
    def play(video):
        print(f"Play {video} !!!")

    @staticmethod
    def pause():
        print("Pause !!!")


if __name__ == '__main__':
    # recevier
    tv = TV()

    # invoker
    remote = TVRemote()

    play_netflix = PlayCommand(tv, 'Netflix')
    play_youtube = PlayCommand(tv, 'YouTube')
    volume_up = VolumeUpCommand(tv)
    volume_down = VolumeDownCommand(tv)
    pause = PauseCommand(tv)

    remote.setCommand('play_netflix', play_netflix)
    remote.setCommand('play_youtube', play_youtube)
    remote.setCommand('pause', pause)
    remote.setCommand('volume_up', volume_up)
    remote.setCommand('volume_down', volume_down)

    remote.executeCommand('play_netflix')
    remote.executeCommand('volume_up')
    remote.executeCommand('pause')
    remote.executeCommand('play_youtube')
    remote.get_last_command()
    remote.executeCommand('volume_down')
