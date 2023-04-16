import pygame,sys,random
class SpaceShip(pygame.sprite.Sprite): # A spaceship sprite is created by inheriting the sprite class in pygame library
    
    def __init__(self,path,x_pos,y_pos):#declares the position and loads the image of the spaceship
        super().__init__()
        self.uncharged=pygame.image.load(path)
        self.charged=pygame.image.load('spaceship_charged.png')
        self.image = self.uncharged
        self.rect = self.image.get_rect(center = (x_pos,y_pos))
        self.shield_surface=pygame.image.load('shield.png')
        self.health=5
    
    def update(self):
        self.rect.center=pygame.mouse.get_pos() # makes sure that the spaceship moves with the movement of the mouse
        self.screen_constraint() 
        self.display_health() 
    
    def screen_constraint(self): # makes sure that parts of the spaceship doesn't goes beyond the screen
        if self.rect.right>=1200:
            self.rect.right=1280
        if self.rect.left<=0:
            self.rect.left=0
    
    def display_health(self): # displays the health in the top left hand corner of the screen
        for index,shield in enumerate(range(self.health)):
            screen.blit(self.shield_surface,(10+index*40,10))
    
    def get_damage(self,damage_amount): # reduces the health by the damage amount which is 1
        self.health-=damage_amount
        
    def charge(self): # shows that the spaceship is charged by the yellow outline around it
        self.image=self.charged
        
    def discharge(self): # shows that the spaceship is uncharged 
        self.image=self.uncharged
        
class Meteor(pygame.sprite.Sprite): #  A meteor sprite is created by inheriting the sprite class in pygame library
    
    def __init__(self,path,x_pos,y_pos,x_speed,y_speed): # The position and speed of the meteor in x and y directions is assigned here
        super().__init__()
        self.image=pygame.image.load(path)
        self.rect=self.image.get_rect(center=(x_pos,y_pos))
        self.x_speed=x_speed
        self.y_speed=y_speed
        
    def update(self): # This tells how the meteor is will move according to the speed given in earlier function
        self.rect.centerx+=self.x_speed
        self.rect.centery+=self.y_speed
        
        if self.rect.centery>=800: # once the meteor goes below the screen, it is omitted to prevent lag of the game
            self.kill()
            
class Laser(pygame.sprite.Sprite): #  A meteor sprite is created by inheriting the sprite class in pygame library
    
    def __init__(self,path,pos,speed): # The image of the laser , position and speed is assigned to the laser
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = pos)
        self.speed=speed
        
    def update(self): # The movement of the laser upwards is given by this method
        self.rect.centery-=self.speed
        if self.rect.centery<=-100: # Once the laser goves above the screen , it is omitted to prevent lag of the game
            self.kill()
            
def main_game(): # This is the main game of the function where everything is taking place
        global laser_active
        global score
        screen.fill((42,43,51)) # the background is filled with a dark purple colour
        
        # different elements are placed on the screen and their movements are updated 
        laser_group.draw(screen)
        spaceship_group.draw(screen)
        meteor_group.draw(screen)
        laser_group.update()
        meteor_group.update()
        spaceship_group.update()
        
        if pygame.sprite.spritecollide(spaceship_group.sprite,meteor_group,True): # if spaceship collides with meteor then get_damage() function is called 
            spaceship_group.sprite.get_damage(1)
            
        for laser in laser_group:
            if pygame.sprite.spritecollide(laser,meteor_group,True): # if the lasers in the group of lasers collide then score is increased by 1
                score+=1
                
        if pygame.time.get_ticks()-laser_timer>=500: # Denotes that after laser is shooted there should be 0.5 sec gap before shooting again
            laser_active=True
            spaceship_group.sprite.charge()
        
def end_game(): # THe screen of end game is displayed through here
    
    screen.fill((42,43,51)) # THe screen is again filled with the same background colour
    
    #The text game over is shown in white by creating a rectangle surface and placing the text at it's center
    text_surface=game_font.render('Game Over',True,(255,255,255))
    text_Rect=text_surface.get_rect(center=(640,380))
    screen.blit(text_surface,text_Rect)\
    
    #The Score is printed in white and the desired font by creating a rectangle surface and placing the text at it's center
    score_surface=game_font.render(f'Score:{score}',True,(255,255,255))
    score_Rect=score_surface.get_rect(center=(640,420))
    screen.blit(score_surface,score_Rect)
    
pygame.init() # THe pygame library is initiated
screen= pygame.display.set_mode((1280,720)) # Sets the dimensions of the game screen
clock = pygame.time.Clock() # Helps in determining the frame rate of the game
pygame.mouse.set_visible(False) # Vanishes the cursor button on the screen

game_font=pygame.font.Font('LazenbyCompSmooth.ttf',40) # font and size of any text on the game is initialised in this variable

#initial score and laser_timer is initialised to 0
score=0
laser_timer=0

spaceship= SpaceShip('spaceship.png',640,500) # the spaceship image is created along with it's initial positions
spaceship_group=pygame.sprite.GroupSingle() # a group which can contain only one sprite is created
spaceship_group.add(spaceship) # the sprite spaceship created in line 112 is added to the group

meteor_group=pygame.sprite.Group() # a group which can contain multiple sprites is created
METEOR_EVENT=pygame.USEREVENT # this event is trigerred by a timer
pygame.time.set_timer(METEOR_EVENT,100) # the meteor_event will be repeated every 100 milliseconds

laser_group=pygame.sprite.Group() # laser group is created where multiple sprites can be added

#game loop to repeat the frames of game until the player quits
while True:
    for event in pygame.event.get(): # loops over every event that a user can input
        
        if event.type== pygame.QUIT: # if the user clicks the cross button to quit the game 
            
            pygame.quit() # the pygame library is closed
            sys.exit() # the entire program is closed
            
        if event.type==METEOR_EVENT: # once the meteor event is started
            meteor_path=random.choice(('Meteor1.png','Meteor2.png','Meteor3.png')) # randomly chooses one of the three meteor images
            
            # randomly generates the position and speed in the x and y direction in the given range
            random_x_pos=random.randrange(0,1280) 
            random_y_pos=random.randrange(-500,-50)
            random_x_speed=random.randrange(-1,1)
            random_y_speed=random.randrange(4,10)
            
            meteor=Meteor(meteor_path,random_x_pos,random_y_pos,random_x_speed,random_y_speed) #a meteor sprite with the above specifications is created
            meteor_group.add(meteor) # the meteor sprite is added to the meteor group
            
        if event.type==pygame.MOUSEBUTTONDOWN and spaceship_group.sprite.health<=0: # if the game is over and health becomes 0 and the user clicks any mouse button
            spaceship_group.sprite.health=5 # the health is renewed
            meteor_group.empty() # the entire meteor group created in previous game is emptied
            score=0 # score is set to 0 again
            
        if event.type==pygame.MOUSEBUTTONDOWN and laser_active: # if the user clicks a mouse button during a game and the laser is still active
            new_laser=Laser('laser.png',event.pos,15) # a laser sprite is created at the position of the laser with speed 15
            laser_group.add(new_laser) # the laser sprite is added to laser group
            laser_active=False # the laser is discharged
            laser_timer=pygame.time.get_ticks() # the laser timer is calculated when it is shot so that after 0.5s it can be recharged
            spaceship_group.sprite.discharge() # the discharge function is called to change the image of spaceship
            
    if spaceship_group.sprite.health > 0:
        main_game() # if the health is greater than 0 then the main game function is called and the game goes on as follows 
    else:
        end_game() # if health is less than 0 then all the operations in end game function is followed
        
    pygame.display.update() # the display is updated
    clock.tick(120) # the frame rate is set to 120fps

