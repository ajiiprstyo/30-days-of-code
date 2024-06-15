class AudioPlayer:
    def __init__(self, volume=50):
        self.volume = volume

    def volumeUp(self):
        if self.volume < 100:
            self.volume += 10
            print(f"Volume increased to {self.volume}")
        else:
            print("Volume is already at maximum")

    def volumeDown(self):
        if self.volume > 0:
            self.volume -= 10
            print(f"Volume decreased to {self.volume}")
        else:
            print("Volume is already at minimum")

# Membuat instance dari class AudioPlayer
player = AudioPlayer()

# Menggunakan method volumeUp dan volumeDown
print("Initial volume:", player.volume)
player.volumeUp()  # Menaikkan volume
player.volumeUp()  # Menaikkan volume
player.volumeDown()  # Menurunkan volume
player.volumeDown()  # Menurunkan volume
player.volumeDown()  # Menurunkan volume
