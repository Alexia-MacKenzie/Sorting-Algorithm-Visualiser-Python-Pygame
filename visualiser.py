import pygame
import random
import homepage
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1250, 680))
scene = "menu"
background_colour = (137, 207, 240)
current_action = ""



pygame.display.set_caption("Sorting Visualiser")

x = 40
y = 40
TitleFont = pygame.font.SysFont("Optima", 50)
CompareFont = pygame.font.SysFont("Optima", 35)
Buttonfont = pygame.font.SysFont("Optima", 20)

width = 20
user_choice = ''
user_input = False
height = [] 
input_rect = pygame.Rect(1100, 100, 140, 32)
plus_rect = pygame.Rect(0, 0, 0, 0)
minus_rect = pygame.Rect(0, 0, 0, 0)
invalidInput = False
sorted_done = False 
b_gen = i_gen = None
h_bubble = h_insert = []
b_done = i_done = False
bubble_stats = {"comparisons" : 0, "swaps" : 0}
insertion_stats = {"comparisons": 0, "swaps" : 0}
run = True
execute = False
sort_delay = 50


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
    global current_action
    action_surf = CompareFont.render(current_action, True, (0, 0, 0))
    screen.blit(action_surf, (950, 500))

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


def draw_speed_controls():
    
    plus_rect = pygame.Rect(1100, 400, 30, 30)
    minus_rect = pygame.Rect(1150, 400, 30, 30)
    
    
    pygame.draw.rect(screen, (200, 200, 200), plus_rect)
    pygame.draw.rect(screen, (200, 200, 200), minus_rect)
    
    
    plus_text = Buttonfont.render("+", True, "black")
    minus_text = Buttonfont.render("-", True, "black")
    speed_label = Buttonfont.render(f"Delay: {sort_delay}ms", True, "black")
    
    screen.blit(plus_text, (plus_rect.x + 10, plus_rect.y + 5))
    screen.blit(minus_text, (minus_rect.x + 12, minus_rect.y + 5))
    screen.blit(speed_label, (1100, 370))
    
    return plus_rect, minus_rect

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
    instruction_text1 = Buttonfont.render("Press the white square to enter your value", True, "black")
    instruction_rect1 = instruction_text1.get_rect()
    instruction_rect1.center = (1100, 200)
    screen.blit(instruction_text1, instruction_rect1)
    instruction_text2 = Buttonfont.render("Press the enter key to submit your value", True, "black")
    instruction_rect2 = instruction_text2.get_rect()
    instruction_rect2.center = (1100, 250)
    screen.blit(instruction_text2, instruction_rect2)
    instruction_text3 = Buttonfont.render("Press the space button to start the sort", True, "black")
    instruction_rect3 = instruction_text3.get_rect()
    instruction_rect3.center = (1100, 300)
    screen.blit(instruction_text3, instruction_rect3)
    plus_rect, minus_rect = draw_speed_controls() 
    return input_rect, plus_rect, minus_rect



def invalid_input():
    text = Buttonfont.render("Invalid Input. Try Again", True, "black")
    textRect = text.get_rect()
    textRect.center = (1100, 200)
    screen.blit(text, textRect)



def bubble_sort(height):
    global current_action
    n = len(height)
    for i in range(n - 1):
        for j in range(len(height) - i - 1):
            current_action = f"Comparing {height[j]} and {height[j+1]}"
            if height[j] > height[j + 1]:
                temp = height[j]
                height[j] = height[j + 1]
                height[j + 1] = temp
                screen.fill((137, 207, 240))
                show(height, False, n-i, True)
                pygame.time.delay(sort_delay)
                pygame.display.update()

    return height

def insertion_sort(height):
    global current_action
    n = len(height)
    for i in range(1,n):
        key = height[i]
        j = i - 1
        while j >= 0 and key < height[j]:
            current_action = f"Comparing {height[j]} and {height[j+1]}"
            height[j + 1] = height[j]
            j -= 1
        height[j + 1] = key
        screen.fill((137, 207, 240))
        show(height, False, i)
        pygame.time.delay(sort_delay)
        pygame.display.update()
    return height

def merge_sort(current_chunk, index, original_list):
    if len(current_chunk) <= 1:
        return current_chunk
    mid = len(current_chunk) // 2
    left = current_chunk[:mid]
    right = current_chunk[mid:]

    sorted_left = merge_sort(left, index, original_list)
    sorted_right = merge_sort(right, index + mid, original_list)

    return merge(sorted_left, sorted_right, index, original_list)


def merge(left, right, offset, original_list):
    global current_action
    result = []
    i = j = 0
    active_range = (offset, offset + len(left) + len(right) - 1)

    while i < len(left) and j < len(right):
        current_action = f"Merging {left[i]} and {right[j]}"
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        # CRITICAL FIX: Update the actual original list at the correct offset
        original_list[offset + len(result) - 1] = result[-1]

        screen.fill(background_colour)
        show(original_list, False, active_range=active_range)
        pygame.time.delay(sort_delay)
        pygame.display.update()

    # Handle remaining elements
    while i < len(left):
        current_action = f"Placing remaining {left[i]}"
        result.append(left[i])
        original_list[offset + len(result) - 1] = left[i]
        i += 1
        screen.fill(background_colour)
        show(original_list, False, active_range=active_range)
        pygame.display.update()
        pygame.time.delay(sort_delay)

    while j < len(right):
        result.append(right[j])
        original_list[offset + len(result) - 1] = right[j]
        j += 1
        screen.fill(background_colour)
        show(original_list, False, active_range=active_range)
        pygame.display.update()
        pygame.time.delay(sort_delay)

    return result

def run_merge_sort(arr):
    n = len(arr)
    sorted_height = merge_sort(arr, 0, arr) 
    
    return sorted_height


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
    
                if plus_rect.collidepoint(event.pos):
                    sort_delay = max(1, sort_delay - 10) 
                elif minus_rect.collidepoint(event.pos):
                    sort_delay = min(500, sort_delay + 10) 

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
            input_rect, plus_rect, minus_rect = sort_page(scene)
            if invalidInput:
                invalid_input()
            
            if sorted_done:
                current_action = "Sorting Completed"
                show(height, sorted_done)
            else:
                show(height, False)
                
            

        else:
            if scene == "merge":
                height = run_merge_sort(height)
            elif scene == "bubble":
                height = bubble_sort(height)
            elif scene == "insertion":
                height = insertion_sort(height)
         
            execute = False
            sorted_done = True
            
            show(height, sorted_done)


    if scene == "compare":
        homeButton, compareButton = homepage.StandardScreen()
        input_rect, plus_rect, minus_rect = sort_page()
        homepage.comparePage()

        if height and b_gen is None and execute:
            h_bubble = list(height)
            h_insert = list(height)
            b_gen = bubble_sort_comp(h_bubble)
            i_gen = insertion_sort_comp(h_insert)
            b_done = i_done = False
            



        if execute:
            pygame.time.delay(sort_delay)
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