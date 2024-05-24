Python Card Game Simulator: Four-Player Battle Royale

This project simulates a card game where four players compete in multiple rounds. Players are dealt 13 cards each, and in each round, they play one card simultaneously. The player with the highest-ranked card wins the round and earns a point. The game continues until all cards are played, and the player with the most points wins the game.

Features
Random Card Dealing: Fair distribution of cards to each player using a shuffled deck.
Card Comparison Logic: Accurate determination of the winning card based on rank and suit.
Round-based Scoring: Tracks points for each player and displays the winner of each round.
Game Statistics: Visualizes the final scores and win distribution using bar charts and pie charts.

Observe the output:

The console will display the results of each round, including the played cards, the winner, and updated scores.
At the end of the game, you'll see the final scores for each player and graphical representations of the results.

Code Structure
Card class: Represents a single playing card with a suit and rank.
Deck class: Manages the deck of cards, including shuffling and dealing.
Hand class (inherits from Deck): Represents a player's hand of cards.
Main script: Handles the game logic, player interactions, and result display.
