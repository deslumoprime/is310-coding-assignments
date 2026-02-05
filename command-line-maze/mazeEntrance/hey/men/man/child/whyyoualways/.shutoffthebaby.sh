#!/bin/bash

sleep 1
clear
echo "With the baby subdued, all you need is to do is to say the right song name (all lowercase, no spaces)."
sleep 2
echo " " 
echo "Type [ready] when you know the song name:" 
read ready

clear

echo "Enter the song name:"
read userentry
while [[ "$userentry" != "comerunningtome" ]]
do
    echo "Enter the song name:"
    read userentry
    echo userentry
done 

cd .comerunningtome

clear

echo "The baby drops to the floor like a mop in a Taco Bell lavatory."
echo " "
sleep 1

echo "Hey! I think the filepath might have something important for the next step!" 
echo " "
sleep 1

echo "Try searching around your current directory to see if there's something you can use."
echo " "
echo "Hint: To use it, run: source filename"
echo " " 