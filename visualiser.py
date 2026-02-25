import pygame
import random
import homepage
pygame.init() # initialises pygame modules which are imported
pygame.font.init()

screen = pygame.display.set_mode((1250, 680))
scene = "menu"
background_colour = (137, 207, 240)



pygame.display.set_caption("Sorting Visualiser")

x = 40
y = 40
TitleFont = pygame.font.SysFont("Optima", 50)
Buttonfont = pygame.font.SysFont("Optima", 20)

width = 20
user_choice = ''
user_input = False
height = [] 
input_rect = pygame.Rect(1100, 100, 140, 32)
invalidInput = False
sorted_done = False



run = True

def create_array(num):
    height = []
    for i in range(num):
        height.append(random.randint(100,600))
    return height


def show(height, sorted_done, sorted_index= None, reverse = False):
    if sorted_index == None:
        if reverse:
            sorted_index = len(height)
        else:
            sorted_index = 0

    for i in range(len(height)):
        if sorted_done:
            colour = "green"
        else: 
            if reverse:
                colour = "green" if i >= sorted_index else "red"
            else:
                colour = "green" if i < sorted_index else "red"
        pygame.draw.rect(screen, colour, (x + 30 * i, y + 40, width, height[i]))


def sort_page(sort_type):
     text = TitleFont.render(f"{sort_type.upper()} SORT", True, "black") 
     textRect = text.get_rect()
     textRect.center = (1100, 100)
     screen.blit(text, textRect)
     input_rect = pygame.Rect(1100, 150, 140, 32)
     int_text1 = Buttonfont.render("Enter and integer between 5 and 30", True, "black")
     int_text_rect1 = int_text1.get_rect()
     int_text_rect1.center = (1100, 130)
     screen.blit(int_text1, int_text_rect1)
     int_text2 = Buttonfont.render("for the number of items you want to sort", True, "black")
     int_text_rect2 = int_text2.get_rect()
     int_text_rect2.center = (1100, 140)
     screen.blit(int_text2, int_text_rect2)
     pygame.draw.rect(screen, "white", input_rect)
     text_surface = Buttonfont.render(user_choice, True, "black")
     screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
     return input_rect

def invalid_input():
    text = Buttonfont.render("Invalid Input. Try Again", True, "black")
    textRect = text.get_rect()
    textRect.center = (1100, 200)
    screen.blit(text, textRect)

def bubble_sort(height):
    n = len(height)
    for i in range(n - 1):
        for j in range(len(height) - i - 1):
            if height[j] > height[j + 1]:
                temp = height[j]
                height[j] = height[j + 1]
                height[j + 1] = temp
                screen.fill((137, 207, 240))
                show(height, False, n-i, True)
                pygame.time.delay(50)
                pygame.display.update()
    return height

def insertion_sort(height):
    n = len(height)
    for i in range(1,n):
        key = height[i]
        j = i - 1
        while j >= 0 and key < height[j]:
            height[j + 1] = height[j]
            j -= 1
        height[j + 1] = key
        screen.fill((137, 207, 240))
        show(height, False, i)
        pygame.time.delay(50)
        pygame.display.update()
    return height

def merge_sort(height):
    if len(height) <= 1:
        return height
    mid = len(height) // 2
    left = height[:mid]
    right = height[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result. append(right[j])
            j += 1
        screen.fill((137, 207, 240))
        show(result)
        pygame.time.delay(50)
        pygame.display.update()
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result


while run:
    execute = False
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if homeButton.collidepoint(event.pos):
                scene = "menu"

            elif compareButton.collidepoint(event.pos):
                scene = "compare"

            if scene == "menu":
                if bubbleButton.collidepoint(event.pos):
                    scene = "bubble"
                    height = []
                elif insertionButton.collidepoint(event.pos):
                    scene = "insertion"
                    height = []
                elif mergeButton.collidepoint(event.pos):
                    scene = "merge"
                    height = []
            if scene == "bubble" or scene == "insertion" or scene == "merge":
                if input_rect.collidepoint(event.pos):
                    user_input = True

        if user_input and event.type == pygame.KEYDOWN:   
            if user_input and event.key == pygame.K_BACKSPACE:
                user_choice = user_choice[:-1]
            elif event.key == pygame.K_RETURN:
                if int(user_choice) < 5 or int(user_choice) > 30:
                    invalidInput = True 
                    sorted_done = False
                else:
                    invalidInput = False
                    sorted_done = False
                    height = create_array(int(user_choice))
                    user_choice = ""
            else:
                if event.unicode.isdigit():
                    user_choice += event.unicode
        
        


    if scene == "menu":
        bubbleButton, insertionButton, mergeButton, homeButton, compareButton = homepage.HomeScreen()
    
    if scene == "merge" or scene == "insertion" or scene == "bubble":
        homeButton, compareButton = homepage.StandardScreen()
        if keys[pygame.K_SPACE]:
            execute = True        
        if execute == False:
            
            
            input_rect = sort_page(scene)
            if invalidInput:
                invalid_input()
            
            if sorted_done:
                show(height, sorted_done)
            else:
                show(height, False)
                
            

        else:
            if scene == "merge":
                height = merge_sort(height)
            elif scene == "bubble":
                height = bubble_sort(height)
            elif scene == "insertion":
                height = insertion_sort(height)
         
            execute = False
            sorted_done = True
            
            show(height, sorted_done)

    if scene == "compare":
        homeButton, compareButton = homepage.StandardScreen()

    pygame.display.update()


pygame.quit()