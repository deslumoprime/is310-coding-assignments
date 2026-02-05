#!/bin/bash

clear
echo "You've found a tool lying around!"
echo " "
sleep 1

echo "This will help us see the filepath clue better!"
echo " "
sleep 1

pwd | sed 's|.*mazeEntrance/||'
sleep 1
echo " "
echo "Got it? Type anything when you're ready to return to the entrance:"
read returnentrance

clear

cd ..
source .gotobeginning.sh

echo "Woosh you have been teleported back to the maze entrance!"
echo "You know where to go from here!"