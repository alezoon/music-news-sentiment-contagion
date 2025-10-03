import mesa
import random

class MusicAgent(mesa.Agent):
    def __init__(self, unique_id, model, music_preference=None):
        super().__init__(unique_id, model)

        # Assign music preference
        if music_preference:
            self._music_preference = music_preference
        else:
            self._music_preference = random.choice(['pop', 'rnb', 'rock', 'country', 'edm'])

        # Stats
        self._emotional_state = "neutral"
        self._openness = random.uniform(0,1)
    
    # Add methods