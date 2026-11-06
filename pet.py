import pygame

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50      # 0 = full, 100 = starving
        self.energy = 50      # 0 = exhausted, 100 = fully rested
        self.happiness = 50   # 0 = sad, 100 = delighted
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        if self.hunger <= 0:
            print(f"{self.name} is already completely full!")
            return

        self.hunger = max(0, self.hunger - 20)
        print(f"You fed {self.name}! Hunger is now {self.hunger}.")

    def play(self):
        if self.energy < 15:
            print(f"{self.name} is too exhausted to play!")
            return

        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 15)
        self.hunger = min(100, self.hunger + 10)
        print(f"You played with {self.name}!")

    def sleep(self):
        if self.energy >= 100:
            print(f"{self.name} is not tired right now!")
            return

        self.energy = min(100, self.energy + 40)
        self.hunger = min(100, self.hunger + 15)
        print(f"{self.name} took a nice nap!")

    def draw(self, screen, center_x, center_y):
            # Ears
            pygame.draw.circle(screen, (220, 150, 100), (center_x - 45, center_y - 65), 25)
            pygame.draw.circle(screen, (220, 150, 100), (center_x + 45, center_y - 65), 25)

            # Body
            pygame.draw.circle(screen, (245, 180, 130), (center_x, center_y), 70)

            # Eyes
            pygame.draw.circle(screen, (20, 20, 20), (center_x - 25, center_y - 15), 8)
            pygame.draw.circle(screen, (20, 20, 20), (center_x + 25, center_y - 15), 8)

            # Cheeks if happy
            if self.happiness > 40:
                pygame.draw.circle(screen, (255, 160, 160), (center_x - 40, center_y + 5), 10)
                pygame.draw.circle(screen, (255, 160, 160), (center_x + 40, center_y + 5), 10)
