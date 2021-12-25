from pygame import mixer

mixer.init

class Dj:
    
    def __init__(self):
        mixer.init()
        mixer.set_num_channels(1)
        self.playlist = [
            mixer.Sound("tchan_intro.mp3"),
            mixer.Sound("tchan_loop.mp3")
        ]

    def play_intro(self):
        self.playlist[0].play(fade_ms=500)

    def play_background_music(self):
        self.playlist[1].play(loops=-1)