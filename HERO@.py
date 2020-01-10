import random
import pygame
import pygame.locals
pygame.init()

MONITOR=pygame.display.set_mode((800, 800))
clock=pygame.time.Clock()

dimension=pygame.display.set_caption('Defence Of The Pudge')

WHITE = (255, 255, 255)



class building(pygame.sprite.Sprite):
    def __init__(self, hp, building_hp_regen,armour, team, placeX, placeY, imagepath):
        pygame.sprite.Sprite.__init__(self)
        self.hp=hp
        self.building_hp_regen=building_hp_regen
        self.armour=armour
        self.team=team
        self.placeX=placeX
        self.placeY=placeY
        self.image =  pygame.image.load(imagepath).convert_alpha()
        self.rect = self.image.get_rect(center=(self.placeX, self.placeY))


class tower(building):
    def __init__(self, tower_damage, hp, building_hp_regen, armour, team, Tier, placeX, placeY, surf, image):
        self.tower_damage=tower_damage
        self.team=team
        self.Tier=Tier
        self.surf=surf
        
        super().__init__(hp, building_hp_regen, armour, team, placeX, placeY, image)

    def attack(self, target_name):
        if (int( self.placeX - target_name.placeX )**2 + int(self.placeY - target_name.placeY)**2)**(1/2) <= 150 and target_name.team != self.team :
            target_name.hp-=self.tower_damage
        





class Soldier(pygame.sprite.Sprite):
    def __init__(self, team, damage, hp, placeX, placeY, imagepath, Line):
        pygame.sprite.Sprite.__init__(self)

        self.team=team
        self.damage=damage
        self.hp=hp
        self.placeX = placeX
        self.placeY = placeY
        self.image =  pygame.image.load(imagepath).convert_alpha()
        self.rect = self.image.get_rect(center=(self.placeX, self.placeY))
        self.Line=Line
    
    def creep_attack(self):
        for i in list_of_soldiers:
            if (int( self.placeX - i.placeX )**2 + int(self.placeY - i.placeY)**2)**(1/2) <=10 and i.team != self.team:
                i.hp-=self.damage
                return
            else:
                if self.Line=='Bottom' and self.team=='radiant':
                    if self.placeX<775:
                        self.placeX+=2
                        self.rect.move_ip(2, 0)
                    else:
                        self.rect.move_ip(0, -2)
                        self.placeY-=2
                elif self.Line=='Middle' and self.team=='radiant':
                    self.placeX+=2
                    self.placeY+=2
                    self.rect.move_ip(2, 2)
                elif self.Line=='Top' and self.team=='radiant':
                    if self.placeY<=775:
                        self.placeX+=2
                        self.rect.move_ip(2, 0)
            
        for i in creepsradiant:
            if (int( self.placeX - i.placeX )**2 + int(self.placeY - i.placeY)**2)**(1/2) <=10 and i.team != self.team:
                i.hp-=self.damage
                return
            else:
                if self.Line=='Top' and self.team=='dire':
                    if self.placeX>775:
                        self.placeX-=2
                        self.rect.move_ip(-2, 0)
                    else:
                        self.rect.move_ip(0, 2)
                        self.placeY+=2
                elif self.Line=='Middle' and self.team=='dire':
                    self.placeX-=2
                    self.placeY-=2
                    self.rect.move_ip(-2, -2)
                elif self.Line=='Bottom' and self.team=='dire':
                    if self.placeY<=775:
                        self.placeY+=2
                        self.rect.move_ip(0, 2)
                    else:
                        self.placeX-=2
                        self.rect.move_ip(-2, 0)
        for i in list_of_towers:
            if (int( self.placeX - i.placeX )**2 + int(self.placeY - i.placeY)**2)**(1/2) <=10 and i.team != self.team:
                i.hp-=self.damage
            else:
                for c in creepsradiant:
                    if (int( self.placeX - i.placeX )**2 + int(self.placeY - i.placeY)**2)**(1/2) <=10 and i.team != self.team:
                        return
                
                for c in list_of_soldiers:
                    if (int( self.placeX - i.placeX )**2 + int(self.placeY - i.placeY)**2)**(1/2) <=10 and i.team != self.team:
                        return
                if self.Line=='Bottom' and self.team=='radiant':
                    if self.placeX<775:
                        self.placeX+=2
                        self.rect.move_ip(2, 0)
                    else:
                        self.rect.move_ip(0, -2)
                        self.placeY-=2
                elif self.Line=='Middle' and self.team=='radiant':
                    self.placeX+=2
                    self.placeY+=2
                    self.rect.move_ip(2, 2)
                elif self.Line=='Top' and self.team=='radiant':
                    if self.placeY<=775:
                        self.placeX+=2
                        self.rect.move_ip(2, 0)
    def creep_check_hp(self):
        if self.hp<=0 and self.team=='dire':
            list_of_soldiers.remove(self)
        elif self.hp<=0 and self.team=='radiant':
            creepsradiant.remove(self)

            



        



# Return the number of the current active tower
def checkTowers(list_of_towers):
    current = 1
    for tower in list_of_towers:
        if tower.hp < 1:
            current += 1

    return current


 #class ANCIENT(building):
     #pass


        
class shrine(building):
     def restore(self, teammate):
         teammate.hp=teammate.max_hp


class barrack(building):
     pass
    

class melee_barrack(barrack):
     def destroyed(self, enemy_team):
         if self.hp==0:
             if self.team=='radiant':
                 t2.HeroDire.hp*=2
             elif self.team=='dire':
                 t1.HeroRadiant.hp*=2


class range_barrack(barrack):
    def destroyed(self, enemy_team):
        if self.hp==0:
            if self.team=='radiant':
                t2.HeroDire.damage*=2
            elif self.team=='dire':
                t1.HeroRadiant.damage*=2


class item:
    def __init__(self, cost, Item_damage):
        self.cost=cost
        self.Item_damage=Item_damage
    



class Hero:
    def __init__(self, lvl, team, damage, hp, gold, Item_slots, stash, max_hp, placeX, placeY, movespeed):

         self.lvl=lvl
         self.damage=damage
         self.hp=hp
         self.gold=gold
         self.Item_slots=Item_slots
         self.stash=stash
         self.max_hp=max_hp
         self.placeX=placeX
         self.placeY=placeY
         # self.place=place,
         self.movespeed=movespeed

    def farm(self, team):
        if team==radiant():
            dire.countD-=1
        elif team==dire():
            radiant.countR-=1

        if  dire.countD==0:
            radiant.HeroRadiant.lvl+=1
        elif radiant.countR==0:
            dire.HeroDire.lvl+=1
        else:
            pass

    def attack(self, target_name):
        target_name.hp-=self.damage*(target_name.armour/100)

    def buy_Item(self, desired_Item):
        if self.gold>=desired_Item.cost:
            if self.Item_slots>0:
                self.damage+=desired_Item.Item_damage
                self.gold-=desired_Item.cost
            else:
                pass
        else:
            pass

    def move(self, ):
        pass    






class radiant:
    #if time==30:
        #time=0
        #for N in range(1, 5):
            #creepsradiant.append(Soldier('radiant', 10, 1000, 500, 500, 'rogue.png'))
        
    HeroRadiant=Hero(1, 'radiant', 55, 600, 1000, 6, 3, 600, 5, 100, 27)
    countR=0

map_surf=pygame.image.load('DOTAMAP.jpg').convert_alpha()
map_rect = map_surf.get_rect(center=(300, 200))

class dire:
    #creepsdire=[]
    #for N in range(6, 11):
        #creepsdire.append(Soldier('dire', 10, 1000, 500, 500, 'knight.png'))
        
    HeroDire=Hero(1, 'dire', 60, 560, 0, 6, 3, 560, 70, 502, 32)
    T1TowerDire=tower(100, 1000, 50, 50, 'dire', 1, 350, 450, map_surf, 'DOTATOWERDIRE.png')
    


Daedalus=item(200, 80)
t1=radiant()
t2=dire()



# map image




tower1 = tower(100, 1000, 50, 50, 'radiant', 1, 350, 450, map_surf, 'DOTATOWERDIRE.png')
tower2 = tower(100, 1000, 50, 50, 'radiant', 2, 250, 550, map_surf, 'DOTATOWERDIRE.png')
tower3 = tower(100, 5000, 50, 50, 'radiant', 3, 150, 650, map_surf, 'DOTATOWERDIRE.png')
tower4 = tower(100, 10000, 50, 50, 'radiant', 4, 50, 750, map_surf, 'DOTATOWERDIRE.png')
shrine1 = shrine(500, 5, 5, 'radiant', 700, 700, 'SHRINERADIANT.png' )
shrine2 = shrine(500, 5, 5, 'dire', 150, 150, 'SHRINEDIRE.png' )

# list of Tower objects
list_of_towers = [tower1, tower2, tower3, tower4]
list_of_shirnes = [shrine1, shrine2]
creepsradiant=[]
list_of_soldiers = []

# list of Soldier objects


print(f'Current tower: {checkTowers(list_of_towers)}')
print(f'Overlapping soldiers with such indexes: {tower1.rect.collidelistall(list_of_soldiers)}')


# Make the map smaller
scale = pygame.transform.scale(map_surf, (map_surf.get_width()*4, 
                                          map_surf.get_height()*4))
scale_rect = scale.get_rect(center=(400, 400))


PLACEXR=300
PLACEYR=775

PLACEXD=775
PLACEYD=300


while 1:
    clock.tick(5)
    MONITOR.blit(scale, scale_rect) 
    pressed_key=pygame.key.get_pressed()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:exit

    if pressed_key[pygame.K_LALT]:
            for tower in list_of_towers:
                    pygame.draw.circle(MONITOR, (0, 70, 225), (tower.placeX, tower.placeY), 50, 2)



    if len(creepsradiant)<5:
        creepsradiant.append(Soldier('radiant', 10, 1000, PLACEXR, PLACEYR, 'rogue.png', 'Bottom'))
        PLACEXR+=1
        PLACEYR+=1
    else:
        PLACEXR=300
        PLACEYR=775


    
    if len(list_of_soldiers)<5:
        list_of_soldiers.append(Soldier('dire', 10, 1000, PLACEXD, PLACEYD, 'knight.png', 'Bottom'))
        PLACEXD-=1
        PLACEYD-=1
    else:
        PLACEXD=775
        PLACEYD=300

        



                   
    # Draw each tower
    for tower in list_of_towers:
        MONITOR.blit(tower.image, tower.rect)

    # Draw each soldier
    for soldier in list_of_soldiers:
        MONITOR.blit(soldier.image, soldier.rect)

    for shrine in list_of_shirnes:
         MONITOR.blit(shrine.image, shrine.rect)
    #releaze creeps attack
    for creep in creepsradiant:
        MONITOR.blit(creep.image, creep.rect)
    for s in creepsradiant:
        s.creep_attack()
        print(s.hp)
    for s in list_of_soldiers:
        s.creep_attack()
    for i in list_of_soldiers:
        i.creep_check_hp()
    for i in creepsradiant:
        i.creep_check_hp()
    


    pygame.display.update()

print('SLAVA UKRAINI')