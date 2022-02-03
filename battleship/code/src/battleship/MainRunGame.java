/*
 * MAIN - This is the Main program which starts the game
 */

package battleship;

import javax.swing.UIManager;

// Main Run Game Class - Starts the game
public class MainRunGame {
	
	// Implements the default platform feel and look (in my case - MacOS)
	public static void main(String[] args) {
		try {
		    UIManager.setLookAndFeel( UIManager.getCrossPlatformLookAndFeelClassName() );
		 } catch (Exception e) {
		            e.printStackTrace();
		 }
		
		// Starting of the game
		// Call the "Start Game" Button on the Initial Game Panel which initiates the play
		StartButton startTheGame = new StartButton();
		startTheGame.initiatePlay();
				
	}

}
