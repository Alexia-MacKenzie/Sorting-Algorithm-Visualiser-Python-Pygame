import pygame
pygame.font.init()
screen = pygame.display.set_mode((1250, 680))
list_sorts = ["Bubble", "Insertion", "Merge"]
Buttonfont = pygame.font.SysFont("Optima", 20) #font type for the button
TitleFont = pygame.font.SysFont("Optima", 50) #constant for title sized text



def drawButton(label, x, y, width, height):
        button = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, "white", button, 3, border_radius=20)  # Draw rectangle
        text_surf = Buttonfont.render(label, True, "black") #draw the text surface with appropriate text from the dictionary
        screen.blit(text_surf, (button.x + (button.width - text_surf.get_width()) // 2, button.y + (button.height - text_surf.get_height()) // 2))

        return button

def StandardScreen():
    screen.fill((137, 207, 240))
    pygame.draw.line(screen, "black", (0, 70), (1250, 70)) 
    title_text = TitleFont.render("Sorting Visualiser", True, "black") 
    text_rect = title_text.get_rect()
    text_rect.center = (615, 40)    
    pygame.draw.rect(screen,((137, 207, 240)), text_rect)
    screen.blit(title_text,(text_rect.x+5, text_rect.y+5)) 
    home_button_surf = TitleFont.render("HOME", True, "black")
    homeButton = home_button_surf.get_rect()
    homeButton.center = (60, 40)
    pygame.draw.rect(screen,((137, 207, 240)), homeButton)
    screen.blit(home_button_surf, (homeButton.x+5, homeButton.y+5))
    compare_button_surf = TitleFont.render("Compare", True, "black")
    compareButton = compare_button_surf.get_rect()
    compareButton.center = (1150, 40)
    pygame.draw.rect(screen,((137, 207, 240)), compareButton)
    screen.blit(compare_button_surf, (compareButton.x+5, compareButton.y+5))

    return homeButton, compareButton
 


def HomeScreen():
    homeButton, compareButton = StandardScreen()
    bubbleButton = drawButton("Bubble", 450, 200, 390, 70)
    insertionButton = drawButton("Insertion", 450, 290, 390, 70)
    mergeButton = drawButton("Merge", 450, 380,390, 70)
    return bubbleButton, insertionButton, mergeButton, homeButton, compareButton

