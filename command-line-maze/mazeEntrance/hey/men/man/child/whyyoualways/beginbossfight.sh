#!/bin/bash
clear

echo "...The boss fight begins soon..."
sleep 2

echo "3"
sleep 0.5
echo "2"
sleep 0.5
echo "1"
sleep 0.5
echo "FIGHT!!!"
echo " "

sleep 0.5

bosshealth=100
turnstaken=0
while (( bosshealth > 0 ))
do 
  clear
  (( turnstaken+= 1 ))

  if (( turnstaken >= 7 ))
  then
    echo "You're taking too long to fight this thing."
    sleep 2
    echo "The baby sends you back to the maze entrance using his powers."
    echo " "
    sleep 5
    source .gotobeginning.sh
    clear
    echo "You will now need to return to the boss fight and fight the baby quicker to pass."
    return
  fi

  echo "Boss Health: $bosshealth / 100"
  echo "Fight the baby! Use punch, kick, channel_negative_aura, or weak_magic_attack!"
  read attack

  if [ "$attack" = "punch" ]
  then
    echo "You punched the baby!"
    sleep 0.5
    (( bosshealth-=10 ))

  elif [ "$attack" = "kick" ]
  then
    echo "You kicked the baby!"
    sleep 0.5
    (( bosshealth-=25 ))

  elif [ "$attack" = "channel_negative_aura" ]
  then
    echo "You channeled your negative aura and feelings towards the baby!"
    sleep 0.5
    (( bosshealth-=1 ))

  elif [ "$attack" = "weak_magic_attack" ]
  then
    echo "You waved your hand, said a flurry of obsceneties, and a weak magic appears to smite the baby. The baby seems to have healed."
    sleep 0.5
    (( bosshealth+=5 ))

  elif [ "$attack" = "supersecret" ]
  then
    echo "Admin override, max damage!"
    sleep 0.5
    (( bosshealth-=100))

  else
    echo "That didn't do any damage."
    sleep 0.5
  fi

  if (( bosshealth < 0 ))
  then
    clear
    echo "Boss Health: 0 / 100"
    echo " "
    break
  else
    echo " "
  fi

done

sleep 1

clear

echo "The baby stops resisting your efforts to shut it down." 
sleep 1

source .shutoffthebaby.sh