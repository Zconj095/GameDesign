"""a Python class that implements an adaptive music system. The class has an init method that initializes the class attributes tracks (a dictionary that maps track names to tracks) and current_track (a reference to the currently playing track). It also has two other methods: add_track, which adds a new track to the system, and change_track, which changes the currently playing track.

The class also has an update_music method that is responsible for updating the currently playing track based on the current game state. The method uses an if-elif chain to check the current game state and change the track accordingly. For example, if the game state is "combat", the method will change the track to "combat_theme".

Finally, the class includes a commented-out section that shows how to use the music system. In this example, two tracks are added to the system ("combat_theme" and "exploration_theme") and the update_music method is called with two different game states ("combat" and "exploration") to demonstrate how the system changes tracks based on the game state."""
class AdaptiveMusicSystem:
    def __init__(self):
        self.tracks = {}
        self.current_track = None

    def add_track(self, name, track):
        self.tracks[name] = track

    def change_track(self, name):
        if name in self.tracks:
            self.current_track = self.tracks[name]
            print(f"Now playing: {name}")
        else:
            print(f"Track {name} not found.")

    def update_music(self, game_state):
        if game_state == "combat":
            self.change_track("combat_theme")
        elif game_state == "exploration":
            self.change_track("exploration_theme")
        # Add more conditions as needed

# Example Usage
music_system = AdaptiveMusicSystem()
music_system.add_track("combat_theme", "combat_music.mp3")
music_system.add_track("exploration_theme", "exploration_music.mp3")

# Simulating game state changes
music_system.update_music("combat")
music_system.update_music("exploration")