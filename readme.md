# Last Pencil - JBA Project

## 1st step: Empty the pencil case
You and your friend decided to play a simple pen-and-paper game. There's one catch — you have only pencils but no paper; the last piece of paper is gone for your beautiful drawings. As a joke, your friend pulls all the pencils out of the case onto the table and says: "Your turn!"

## 2nd step: New rules
Your friend's suggestion surprised you a little bit. After a couple of "No, you" retaliations, you decided that it would be more convenient to input the initial conditions to determine who goes first, and how many pencils there are on the table.

## 3rd step: Working on the gameplay
An interesting idea has come to your mind. Let's change the rules of game. Players take turns taking X pencils until none of them remain.

## 4th step: Fair play
The game was interesting, but it went sour. No one was playing a fair game! You've taken 10 pencils, your friend decided that it is unfair and somehow took a negative number! Moreover, you both can't decide which of you won. Maybe, it's time to add new rules to the game?

## 5th step: The right strategy
You've played a couple of games with your friend. After a while, you both found out that if there are 2, 3, or 4 pencils left on the table, you automatically win. It happens because a player can take 1, 2, or 3 pencils and leave the other player with only one. The other player has nothing left but to take the last pencil and lose the game.

On the other hand, if you have 5 pencils on the table, you lose. It will again lead to the situation described above but vice-versa.

The same thing happens when there are 6, 7, or 8 pencils left on the table. It will eventually repeat all over again.

It's easier to get a grasp of it with a line of 10 red-green pencils. In this example, we can be sure that if both players know the winning strategy, the first one will be the winner. Here is a game process:

||||||||||

The first player has an advantage and takes 1 pencil:

|||||||||

The second player has a disadvantage, so if the second player takes any number of pencils from 1 to 3, the first player is left with a winning strategy:

    1: ||||||||
    2: |||||||
    3: ||||||

The first player stands in a winning position and takes that number. It will lead to a losing position for the second player:

|||||

The second player stands in a losing position — if the second player takes any number of pencils from 1 to 3, the first player will be left in a winning position:

    1: ||||
    2: |||
    3: ||

The first player stands in a winning position and takes the right number of pencils. It leaves the second player with one pencil:

|

Your friend came up with the idea of creating a bot for the game a bit more replayable. Instead of taking input from two players, you need to program a bot that follows a winning strategy. If the bot's position isn't the winning one, you can program it to take any number of pencils (1, 2, or 3) at random. You can also come up with any pattern of your own for the losing position.
