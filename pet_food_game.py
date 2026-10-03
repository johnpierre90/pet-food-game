import pygame

# Start Pygame
pygame.init()

# Game window
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pet Food Collection Game")

# Fonts
font = pygame.font.Font(None, 30)
win_font = pygame.font.Font(None, 90)

# Pet
pet = pygame.Rect(100, 250, 60, 60)
pet_speed = 4

# Food Sprite
class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 180, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create food group
food_group = pygame.sprite.Group()

food_group.add(Food(500, 300))
food_group.add(Food(250, 150))
food_group.add(Food(650, 450))
food_group.add(Food(400, 500))
food_group.add(Food(700, 150))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move pet only while food remains
    if len(food_group) > 0:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pet.x -= pet_speed
        if keys[pygame.K_RIGHT]:
            pet.x += pet_speed
        if keys[pygame.K_UP]:
            pet.y -= pet_speed
        if keys[pygame.K_DOWN]:
            pet.y += pet_speed

    # Keep pet inside screen
    pet.clamp_ip(screen.get_rect())

    # Collect food
    for food in food_group:
        if pet.colliderect(food.rect):
            food.kill()

    # Background
    screen.fill((100, 180, 255))

    # Draw pet
    pygame.draw.rect(screen, (150, 80, 40), pet)

    # Write PET on the brown object
    pet_text = font.render("PET", True, (255, 255, 255))
    text_rect = pet_text.get_rect(center=pet.center)
    screen.blit(pet_text, text_rect)

    # Draw food
    food_group.draw(screen)

    # Display YOU WIN when all food is collected
    if len(food_group) == 0:
        win_text = win_font.render("YOU WIN!", True, (0, 200, 0))
        win_rect = win_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )

        screen.blit(win_text, win_rect)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

