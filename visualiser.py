import pygame
pygame.init()

win = pygame.display.set_mode((500, 400))

pygame.display.set_caption("Sorting Visualiser")

x = 40
y = 40

width = 20

height =  [200, 50, 130, 90, 250, 61, 110, 88, 33, 80, 70, 159, 180, 20]

run = True

def show(height):
    for i in range(len(height)):
        pygame.draw.rect(win, "red", (x + 30 * i, y, width, height[i]))

def bubble_sort(height):
    for i in range(len(height) - 1):
        for j in range(len(height) - i - 1):
            if height[j] > height[j + 1]:
                temp = height[j]
                height[j] = height[j + 1]
                height[j + 1] = temp
                win.fill((0,0,0))
                show(height)
                pygame.time.delay(50)
                pygame.display.update()

def insertion_sort(height):
    n = len(height)
    for i in range(1,n):
        key = height[i]
        j = i - 1
        while j >= 0 and key < height[j]:
            height[j + 1] = height[j]
            j -= 1
        height[j + 1] = key
        win.fill((0,0,0))
        show(height)
        pygame.time.delay(50)
        pygame.display.update()

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
        win.fill((0,0,0))
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
    
    if keys[pygame.K_SPACE]:
        execute = True
    

    if execute == False:
        win.fill((0,0,0))
        show(height)
        pygame.display.update()

    else:
        height = merge_sort(height)
        execute = False


pygame.quit()