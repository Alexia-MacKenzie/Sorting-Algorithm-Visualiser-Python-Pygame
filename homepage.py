import pygame
pygame.font.init()
screen = pygame.display.set_mode((1250, 680))
list_sorts = ["Bubble", "Insertion", "Merge"]
Buttonfont = pygame.font.SysFont("Optima", 20) #font type for the button


def drawButton(label, x, y, width, height):
        button = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, "white", button, 3, border_radius=20)  # Draw rectangle
        text_surf = Buttonfont.render(label, True, "black") #draw the text surface with appropriate text from the dictionary
        screen.blit(text_surf, (button.x + (button.width - text_surf.get_width()) // 2, button.y + (button.height - text_surf.get_height()) // 2))
            #blit button onto the screen
        return button


def HomeScreen():
    screen.fill((137, 207, 240))
    bubbleButton = drawButton("Bubble", 450, 200, 390, 70)
    insertionButton = drawButton("Insertion", 450, 290, 390, 70)
    mergeButton = drawButton("Merge", 450, 380,390, 70)
    return bubbleButton, insertionButton, mergeButton

