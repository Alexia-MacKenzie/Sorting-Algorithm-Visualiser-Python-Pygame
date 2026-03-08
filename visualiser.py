import pygame
import random
import homepage
import time
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
merge_logic_time = 0 
b_gen = i_gen = None
h_bubble = h_insert = []
b_done = i_done = False
bubble_stats = {"comparisons" : 0, "swaps" : 0}
insertion_stats = {"comparisons": 0, "swaps" : 0}
run = True
execute = False


run = True

def create_array(num, scene):
    height = []
    if scene == "compare":
        for i in range(num):
            height.append(random.randint(20,100))
    else:
        for i in range(num):
            height.append(random.randint(100,600))
    return height


def show(height, sorted_done, sorted_index= None, reverse = False, active_range=None):
    if sorted_index == None:
        if reverse:
            sorted_index = len(height)
        else:
            sorted_index = 0

    for i in range(len(height)):
        if sorted_done:
            colour = "green"
        elif active_range and active_range[0] <= i <= active_range[1]:
            colour = "yellow"
        else: 
            if reverse:
                colour = "green" if i >= sorted_index else "red"
            else:
                colour = "green" if i < sorted_index else "red"
        pygame.draw.rect(screen, colour, (x + 30 * i, y + 40, width, height[i]))

def compare_show(heights, box_idx, individual_done=False):
    n = len(heights)
    if n <= 0:
        return
    box_x_starts = [100, 500, 900]
    base_x = box_x_starts[box_idx]
    base_y = 500  
    

    bar_width = (280 // n)
    
    for i in range(n):
        colour = "green" if individual_done else "red"
        pygame.draw.rect(screen, colour, (base_x + 10 + (i * bar_width), base_y - heights[i], bar_width - 2, heights[i]))


def sort_page(sort_type="None"):
    if sort_type == "None":
        text = TitleFont.render(f"Comparison Page", True, "black")
        int_text1 = Buttonfont.render("Enter and integer between 5 and 10", True, "black")
    else:
        text = TitleFont.render(f"{sort_type.upper()} SORT", True, "black") 
        int_text1 = Buttonfont.render("Enter and integer between 5 and 30", True, "black")
    textRect = text.get_rect()
    textRect.center = (1100, 100)
    screen.blit(text, textRect)
    input_rect = pygame.Rect(1100, 150, 140, 32)
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
    total_logic_time = 0
    n = len(height)
    for i in range(n - 1):
        for j in range(len(height) - i - 1):
            if height[j] > height[j + 1]:
                bubble_time = time.perf_counter()
                temp = height[j]
                height[j] = height[j + 1]
                height[j + 1] = temp
                total_logic_time += (time.perf_counter() - bubble_time)
                screen.fill((137, 207, 240))
                show(height, False, n-i, True)
                pygame.time.delay(50)
                pygame.display.update()
    bubble_results = {"Number of items" : n, "Time taken" : total_logic_time}

    return height, bubble_results

def insertion_sort(height):
    total_logic_time = 0
    n = len(height)
    for i in range(1,n):
        insertion_time = time.perf_counter()
        key = height[i]
        j = i - 1
        while j >= 0 and key < height[j]:
            height[j + 1] = height[j]
            j -= 1
        height[j + 1] = key
        total_logic_time += (time.perf_counter() - insertion_time)
        screen.fill((137, 207, 240))
        show(height, False, i)
        pygame.time.delay(50)
        pygame.display.update()
    insertion_results = {"Number of items" : n, "Time taken" : total_logic_time}
    return height, insertion_results

def merge_sort(height, index=0):
    global merge_logic_time
    start_time = time.perf_counter()
    if len(height) <= 1:
        return height
    mid = len(height) // 2
    left = height[:mid]
    right = height[mid:]
    merge_logic_time += (time.perf_counter() - start_time)

    sorted_left = merge_sort(left, index)
    sorted_right = merge_sort(right, index + mid)

    return merge(sorted_left, sorted_right, index)


def merge(left, right, offset):
    global merge_logic_time
    result = []
    i = j = 0
    active_range = (offset, offset + len(left) + len(right) - 1)

    while i < len(left) and j < len(right):
        start_time = time.perf_counter()

        if left[i] < right[j]:
            result.append(left[i])
            height[offset + len(result) - 1] = left[i]
            i += 1
        else:
            result.append(right[j])
            height[offset + len(result) - 1] = right[j]
            j += 1
        merge_logic_time += (time.perf_counter() - start_time)

        screen.fill((137, 207, 240))
        show(height, False, active_range=active_range)
        pygame.time.delay(50)
        pygame.display.update()
    while i < len(left):
            result.append(left[i])
            height[offset + len(result) - 1] = left[i]
            i += 1
            screen.fill((137, 207, 240))
            show(height, False, active_range=active_range)
            pygame.display.update()
            pygame.time.delay(50)

    while j < len(right):
        result.append(right[j])
        height[offset + len(result) - 1] = right[j]
        j += 1
        screen.fill((137, 207, 240))
        show(height, False, active_range=active_range)
        pygame.display.update()
        pygame.time.delay(50)

    return result

def run_merge_sort(height):
    global merge_logic_time
    merge_logic_time = 0  
    
    n = len(height)
    
    sorted_height = merge_sort(height, 0) 
    
    merge_results = {
        "Number of items": n, 
        "Time taken": merge_logic_time
    }
    
    return sorted_height, merge_results


def bubble_sort_comp(height):
    n = len(height)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            yield {"done": False, "comparisons" : comparisons, "swaps" : swaps} 
            if height[j] > height[j + 1]:
                temp = height[j]
                height[j] = height[j + 1]
                height[j + 1] = temp
                swaps += 1     
    yield {"done": True, "comparisons" : comparisons, "swaps" : swaps}  

def insertion_sort_comp(height):
    comparisons = 0
    swaps = 0
    for i in range(1, len(height)):
        key = height[i]
        j = i - 1
        while j >= 0 and key < height[j]:
            comparisons += 1
            height[j + 1] = height[j]
            j -= 1
            yield {"done": False, "comparisons" : comparisons, "swaps" : swaps} 
        height[j + 1] = key
        swaps += 1
        yield {"done": False, "comparisons" : comparisons, "swaps" : swaps} 
    yield {"done": True, "comparisons" : comparisons, "swaps" : swaps} 


def display_stats(bubble, insertion):
    b_text = Buttonfont.render(f"Comps: {bubble['comparisons']} | Swaps: {bubble['swaps']}", True, "black")
    screen.blit(b_text, (100, 520))
    
    
    i_text = Buttonfont.render(f"Comps: {insertion['comparisons']} | Swaps: {insertion['swaps']}", True, "black")
    screen.blit(i_text, (500, 520))

while run:
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
                height = []

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
            if scene == "bubble" or scene == "insertion" or scene == "merge" or scene == "compare":
                if input_rect.collidepoint(event.pos):
                    user_input = True

        if user_input and event.type == pygame.KEYDOWN:  
            invalidInput = False 
            if user_input and event.key == pygame.K_BACKSPACE:
                user_choice = user_choice[:-1]
            elif event.key == pygame.K_SPACE:
                if scene == "compare" and height:
                    execute = True
            elif event.key == pygame.K_RETURN:
                if scene == "compare":
                    if int(user_choice) < 5 or int(user_choice) > 10:
                        invalidInput = True 
                        sorted_done = False
                else:
                    if int(user_choice) < 5 or int(user_choice) > 30:
                        invalidInput = True 
                        sorted_done = False
                
                if not invalidInput:
                    invalidInput = False
                    sorted_done = False
                    height = create_array(int(user_choice), scene)
                    user_choice = ""
                    if scene == "compare":
                        b_gen = i_gen = None
                        execute = True
                    else:
                        sorted_done = False
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
                height, merge_results = run_merge_sort(height)
            elif scene == "bubble":
                height, bubble_results = bubble_sort(height)
            elif scene == "insertion":
                height, insertion_results = insertion_sort(height)
         
            execute = False
            sorted_done = True
            
            show(height, sorted_done)

    if scene == "compare":
        homeButton, compareButton = homepage.StandardScreen()
        input_rect = sort_page()
        homepage.comparePage()

        if height and b_gen is None and execute:
            h_bubble = list(height)
            h_insert = list(height)
            b_gen = bubble_sort_comp(h_bubble)
            i_gen = insertion_sort_comp(h_insert)
            b_done = i_done = False
            



        if execute:
            pygame.time.delay(50)
            if not b_done:
                try: 
                    status = next(b_gen)
                    bubble_stats["comparisons"], bubble_stats["swaps"] = status["comparisons"], status["swaps"]
                    if status["done"] == True:
                        b_done = True
                except (StopIteration, TypeError): 
                    b_done = True
            
        
            if not i_done:
                try: 
                    status = next(i_gen)
                    insertion_stats["comparisons"], insertion_stats["swaps"] = status["comparisons"], status["swaps"]
                    if status["done"] == True:
                        i_done = True
                except (StopIteration, TypeError):
                    i_done = True
            
            if b_done and i_done:
                execute = False
                sorted_done = True

        if b_gen is not None:
            compare_show(h_bubble, 0, b_done or sorted_done)
            compare_show(h_insert, 1, i_done or sorted_done)

            if b_done and not i_done:
                winner_text = Buttonfont.render("Bubble Wins!", True, "Green")
                screen.blit(winner_text, (150, 250))
            elif i_done and not b_done:
                winner_text = Buttonfont.render("Insertion Wins!", True, "Green")
                screen.blit(winner_text, (550, 250))
        elif sorted_done:
            compare_show(h_bubble, 0, True)
            compare_show(h_insert, 1, True)
        

        
        else:
            if invalidInput:
                invalid_input()
        display_stats(bubble_stats, insertion_stats)





    pygame.display.update()


pygame.quit()