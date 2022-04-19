from abc import abstractmethod


class VideoPlayer(object):
    def __init__(self, state):
        self._state = state
        self._state.set_player(self)
        print("Player is created.")

    def play(self):
        self._state.play()

    def pause(self):
        self._state.pause()

    def change_state(self, state):
        self._state = state


class StateInterface(object):
    def __init__(self, player=None) -> None:
        self.player = player

    def set_player(self, player):
        self.player = player

    @abstractmethod
    def play(self):
        print("PLAYING...")

    @abstractmethod
    def pause(self):
        print("PAUSING...")


class unStartedState(StateInterface):
    def play(self):
        super().play()
        self.player.change_state(PlayingState(self.player))
        print("The video started playing the video from the beginning.")

    def pause(self):
        super().pause()
        print("The video hasn't started ... ><")


class PlayingState(StateInterface):
    def play(self):
        super().play()
        print("The video has been playing !!!")

    def pause(self):
        super().pause()
        self.player.change_state(PausedState(self.player))
        print("The video was paused.")


class PausedState(StateInterface):
    def play(self):
        super().play()
        self.player.change_state(PlayingState(self.player))
        print("The video continued playing !!!")

    def pause(self):
        super().pause()
        print("The video has been paused !!!")


class FinishedState(StateInterface):
    def play(self):
        super().play()
        self.player.change_state(PlayingState(self.player))
        print("The video started playing the video from the beginning.")

    def pause(self):
        super().pause()
        print("The video has finished !!!")


if __name__ == '__main__':
    init_state = unStartedState()
    player = VideoPlayer(init_state)

    player.pause()
    player.play()
    player.pause()
    player.pause()
    player.play()
    player.change_state(FinishedState(player))
    player.pause()
    player.play()
    player.pause()
    player.pause()
    player.play()
