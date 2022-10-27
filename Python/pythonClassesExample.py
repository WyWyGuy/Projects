# Write your code here
global fight
fight = True

class Hero():
  name = ""
  weaponName = ""
  weaponDamage = 0
  health = 0
  alive = True
  potion = 1
  
  def __init__(self, name, weaponName, weaponDamage, health):
    self.name = name
    self.weaponName = weaponName
    self.weaponDamage = weaponDamage
    self.health = health
  
  def attack(self, enemy):
    enemy.hurt(self.weaponDamage)
  
  def hurt(self, damage):
    self.health -= damage
    print(self.name + " lost " + str(damage) + " HP!")
    if self.health <= 0:
      print(self.name + " died!")
      global fight
      fight = False
  
  def usePotion(self):
    if self.potion >= 1:
      self.potion -= 1
      self.health += 5
      print(self.name + " used a potion to regain 5 HP!")
    
  
class Monster():
  name = ""
  strength = 0
  health = 0
  
  def __init__(self, name, strength, health):
    self.name = name
    self.strength = strength
    self.health = health
  
  def roar(self):
    print("The monster roars!")
    
  def attack(self, enemy):
    enemy.hurt(self.strength)
    
  def hurt(self, damage):
    self.health -= damage
    print(self.name + str(" lost ") + str(damage) + " HP!")
    if self.health <= 1:
      print(self.name + " ran away!")
      global fight
      fight = False

link = Hero("Link", "Master Sword", 8, 25)
boko = Monster("Bokoblin", 12, 15)

link.attack(boko)
boko.roar()

while fight == True:
  boko.attack(link)
  if link.health <= (boko.strength + 1):
    link.usePotion()
  link.attack(boko)