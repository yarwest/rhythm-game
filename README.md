# rhythm-game
A procedurally generated rhythm game made in pygame.

I made this as a fun side project to test out how I would set up a pygame based game.

The `EventWatcher` in the gameMaster.py file is the root of the publish subscribe pattern used for updating game components every tick and delegating events that are received by the pygame library.

The `UIController` in the uiController.py file functions in a similar fashion in making sure all the visual components are drawn to the screen.
