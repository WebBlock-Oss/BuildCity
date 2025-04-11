import pygame

pygame.font.init()
pygame.init()
running = True

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("BuildCity Alpha Build")

buildings = []
buildtype = "road"
mouseColour = (0, 0, 0)
writeFont = pygame.font.SysFont('Comic Sans MS', 30)
workDemand = 10
i = 0
baseWorkDemand = 10

while running:
    i += 1
    if i == 10000:
        baseWorkDemand += 1
        i = 0

    mousePos = pygame.mouse.get_pos()

    mouseX, mouseY = mousePos

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
          buildValue = buildtype + ", " + str(50*round((mouseX-25)/50)) + ", " + str(50*round((mouseY-25)/50))
          buildings.append(buildValue)
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_r:
              buildtype = "road"
          if event.key == pygame.K_g:
              buildtype = "grass"
          if event.key == pygame.K_e:
              buildtype = "erase"
          if event.key == pygame.K_l:
              buildtype = "lowResid"
          if event.key == pygame.K_c:
              buildtype = "commercial"
          if event.key == pygame.K_o:
              buildtype = "office"
          if event.key == pygame.K_h:
              buildtype = "highResid"
          if event.key == pygame.K_i:
              buildtype = "industrial"

    screen.fill((26, 138, 56))

    if buildtype == "road":
        mouseColour = (84, 84, 84)
    if buildtype == "grass" or buildtype == "erase":
        mouseColour = (26, 138, 56)
    if buildtype == "lowResid":
        mouseColour = (0, 225, 30)
    if buildtype == "commercial":
        mouseColour = (0, 30, 255)
    if buildtype == "office":
        mouseColour = (255, 0, 255)
    if buildtype == "highResid":
        mouseColour = (0, 80, 5)
    if buildtype == "industrial":
        mouseColour = (255, 250, 0)

    pygame.draw.rect(screen, mouseColour, ((50*(round((mouseX-25)/50)), 50*(round((mouseY-25)/50))), (50, 50)))

    population = 0
    workDemand = baseWorkDemand

    for value in buildings:
        out = value.split(", ")
        build, x, y = out

        if build == "road":
            pygame.draw.rect(screen, (84, 84, 84), ((int(x), int(y)), (50, 50)))

        if build == "erase" or build == "grass":
            pygame.draw.rect(screen, (26, 138, 56), ((int(x), int(y)), (50, 50)))

        if build == "lowResid":
            pygame.draw.rect(screen, (0, 225, 30), ((int(x), int(y)), (50, 50)))
            population += 3

        if build == "commercial":
            pygame.draw.rect(screen, (0, 30, 225), ((int(x), int(y)), (50, 50)))
            workDemand -= 1
            if workDemand == -1:
                workDemand = 0

        if build == "office":
            pygame.draw.rect(screen, (255, 0, 255), ((int(x), int(y)), (50, 50)))
            workDemand -= 1
            if workDemand == -1:
                workDemand = 0

        if build == "highResid":
            pygame.draw.rect(screen, (0, 80, 0), ((int(x), int(y)), (50, 50)))
            population += 93

        if build == "industrial":
            pygame.draw.rect(screen, (255, 250, 0), ((int(x), int(y)), (50, 50)))
            workDemand -= 1
            if workDemand == -1:
                workDemand = 0

    populationText = writeFont.render("Population: "+str(population), False, (255, 255, 255))
    workDemandText = writeFont.render("Work Demand: "+str(workDemand), False, (255, 255, 255))

    pygame.draw.line(screen, (0, 0, 0), (50, 0), (50, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (150, 0), (150, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (250, 0), (250, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (350, 0), (350, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (450, 0), (450, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (500, 0), (500, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (550, 0), (550, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (600, 0), (600, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (650, 0), (650, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (700, 0), (700, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (750, 0), (750, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (800, 0), (800, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (850, 0), (850, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (900, 0), (900, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (950, 0), (950, 600), 5)

    pygame.draw.line(screen, (0, 0, 0), (0, 50), (1000, 50), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 100), (1000, 100), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 150), (1000, 150), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (1000, 200), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 250), (1000, 250), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (1000, 300), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 350), (1000, 350), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 400), (1000, 400), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 450), (1000, 450), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 500), (1000, 500), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 550), (1000, 550), 5)

    screen.blit(populationText, (15, 0))
    screen.blit(workDemandText, (15, 50))

    pygame.display.flip()

pygame.quit()
