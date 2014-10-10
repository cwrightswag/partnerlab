import random

print "A monster approaches! Prepare to fight!"

playerHealth = 100
monsterHealth = 100
punchDmg = 5
swordDmg = 10
fireballDmg = 30

damageByMonster = random.randint(1,35)

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "You have 100 health"
print "The monster has 100 health"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"




while(monsterHealth > 0 and playerHealth > 0):
    print "What attack do you wish to use?"
    print "1 - Punch (5 damage)2 - Sword (10 damage) 3 - Fireball (30 damage)"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    userInput = int(raw_input())
    if userInput == 1:
        monsterHealth = monsterHealth - 5
        print "You punch the monster!"
    if userInput == 2:
        monsterHealth = monsterHealth - 10
        print "You swing at the monster with your sword!"
    if userInput == 3:
        monsterHealth = monsterHealth - 30
        print "You cast a fireball and set the monster ablaze!"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    if monsterHealth > 0:
        print "The monster attacks you for"
        playerHealth = playerHealth - damageByMonster
        print damageByMonster
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "The monster's health is"
    print monsterHealth
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Your health is"
    print playerHealth
    if monsterHealth <= 0:
        print "You defeat the evil monster!!"
    if playerHealth <= 0:
        print "You are dead"
       
    

    