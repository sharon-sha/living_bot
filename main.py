import pygame
from pet import Pet


def draw_bar(screen, x, y, width, height, current_val, max_val, bar_color):
    # Background (gray container)
    pygame.draw.rect(screen, (200, 200, 200), (x, y, width, height), border_radius=4)
    # Filled bar
    fill_width = int((current_val / max_val) * width)
    if fill_width > 0:
        pygame.draw.rect(screen, bar_color, (x, y, fill_width, height), border_radius=4)
    # Dark border outline
    pygame.draw.rect(screen, (50, 50, 50), (x, y, width, height), 2, border_radius=4)


def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Virtual Pet")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 26)

    my_pet = Pet("Pixel")

    # Load audio (safe with fallback if files don't exist yet)
    try:
        pygame.mixer.music.load("assets/sounds/bg_music.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
    except pygame.error:
        print("Note: bg_music.mp3 not found. Continuing silently.")

    try:
        feed_sound = pygame.mixer.Sound("assets/sounds/eat.mp3")
        play_sound = pygame.mixer.Sound("assets/sounds/meow.mp3")
    except pygame.error:
        feed_sound = None
        play_sound = None

    # Custom timer: pass time every 3 seconds (3000 ms)
    TICK_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TICK_EVENT, 3000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == TICK_EVENT:
                my_pet.hunger = min(100, my_pet.hunger + 5)
                my_pet.happiness = max(0, my_pet.happiness - 5)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    my_pet.feed()
                    if feed_sound:
                        feed_sound.play()
                elif event.key == pygame.K_p:
                    my_pet.play()
                    if play_sound:
                        play_sound.play()
                elif event.key == pygame.K_s:
                    my_pet.sleep()

        # --- DRAWING SECTION ---
        # 1. Wall background
        screen.fill((235, 240, 245))

        # 2. Wooden floor
        pygame.draw.rect(screen, (205, 165, 120), (0, 330, 640, 150))
        pygame.draw.line(screen, (140, 100, 70), (0, 330), (640, 330), 4)

        # 3. Controls guide text
        info_text = font.render(
            "Press: [F] Feed  |  [P] Play  |  [S] Sleep", True, (40, 40, 40)
        )
        screen.blit(info_text, (20, 20))

        # 4. Stat labels and graphical bars
        hunger_text = font.render(f"Hunger: {my_pet.hunger}", True, (40, 40, 40))
        energy_text = font.render(f"Energy: {my_pet.energy}", True, (40, 40, 40))
        happy_text = font.render(f"Happiness: {my_pet.happiness}", True, (40, 40, 40))

        screen.blit(hunger_text, (20, 70))
        draw_bar(screen, 160, 72, 130, 16, my_pet.hunger, 100, (220, 70, 70))

        screen.blit(energy_text, (20, 105))
        draw_bar(screen, 160, 107, 130, 16, my_pet.energy, 100, (60, 180, 80))

        screen.blit(happy_text, (20, 140))
        draw_bar(screen, 160, 142, 130, 16, my_pet.happiness, 100, (70, 120, 220))

        # 5. Draw Pet
        my_pet.draw(screen, 460, 280)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
