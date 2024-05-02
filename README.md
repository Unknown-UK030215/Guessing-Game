# Guessing Game (Improved)

This is a guessing game in which clients connect to a server in order to play. The server selects a random number based on the player’s level of difficulty choice, and the player attempts to guess that number within a certain number of tries. A leaderboard shows the score, calculated from these attempts.


steps on how to upload on github
1. ***cd desktop***
---- Navigate to the Desktop directory: Move to the Desktop folder using the command line. ----

2. ***cd Enhanced-Guessing-Game***
---- Access the Enhanced-Guessing-Game folder: Change directory to the folder containing the project files. ----

3. ***git clone "https://github.com/Unknown-UK030215/Guessing-Game"***
---- Clone the GitHub repository: Copy the repository from GitHub to your local machine using the provided URL. ----

4. ***cd Guessing-Game***
---- Enter the Guessing-Game directory: Move into the directory where the cloned repository resides. ----

5. ***git add server.py***
---- Stage changes for server.py: Prepare the modifications made to the server.py file to be included in the next commit. ----

6. ***git commit -m "text you want to write"***
---- Commit changes with a descriptive message: Document the changes made to the server.py file with a clear and informative message. ----

7. ***git add client.py***
---- Stage changes for client.py: Prepare the alterations made to the client.py file to be added to the next commit. ----

8. ***git commit -m "text you want to write"***
---- Commit changes with a descriptive message: Record the adjustments made to the client.py file with a descriptive message summarizing the modifications. ----

9. ***git push origin master***
---- Push changes to the GitHub repository: Send the committed changes from your local repository to the GitHub repository's master branch. ----


*** How the server script works: ***

----- Initialization: The socket is initialized and it waits for connection.

----- Handling clients: When a client connects, they are asked to input their name and choose the level of difficulty(easy, medium or hard). It then enters into a loop where random number is generated based on chosen difficulty and client has to guess the number.

----- Calculating score: After receiving guess from client, it checks whether the guess is right. If yes, then player’s score is calculated according to tries made by him/her and leaderboard gets updated accordingly.

----- Displaying Leader board: Display leaderboard after each correct guess sorted by score then number of tries.

----- Data Persistence: User data (scores & leaderboard) is loaded/saved to JSON file (user_data.json).

----- The client script (client.py) connects to server and enables user playing game where guesses are sent by user while feedbacks about correctness of those guesses are received from server with leaderboards displayed after every correct answer.

 ***how the client script works:***

----- Initialization: It connects to the server using a socket.

----- Gameplay Loop: It enters a loop where it prompts the user to input guesses and sends them to the server. It receives feedback from the server and displays it to the user.

----- Leaderboard Display: After a correct guess, it receives and displays the updated leaderboard from the server.

----- Repeat Option: After each game, it prompts the user if they want to play again. If not, the loop breaks, and the client program exits.