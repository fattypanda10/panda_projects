/*
STARTING SCREEN/PANEL - Makes the Starting Panel or the Initial Screen of the Game 
where multiple Settings are presented to the player(s). 
*/

package battleship;

import java.awt.BorderLayout;
import java.awt.Color;
import javax.swing.*;

// Forms the Initial Screen - Starting Game Panel
public class StartPanel {
	
	// Forms the components to be added later
	// Panel 0
	GUIMenu Panel1 = new GUIMenu();
	JFrame startFrame = Panel1.frame(250, 600, "Battleship Game: Selection Screen", 3, false);
	JPanel startPanel0 = Panel1.panel(Color.lightGray);
	
	//Panel 1
	JPanel startPanel1 = Panel1.panel(Color.lightGray);
	JLabel welcomeMsg1 = Panel1.label("Welcome to Battleship.", 20);
	
	//Panel 2
	JPanel startPanel2 = Panel1.panel(Color.lightGray);
	JLabel welcomeMsg2 = Panel1.label("Please Select your Options and Get Started.", 18);
	
	// Panel 3
	JPanel startPanel3 = Panel1.panel(Color.lightGray);
	JButton shipPlacement = Panel1.button(50, 20, "Choose Ship Placement");
	JButton scoringSystem = Panel1.button(50, 20, "Choose Scoring System");
	
	// Panel 3_1 (Panel within another panel - (here inside Panel 3)
	JPanel startPanel3_1 = Panel1.panel(Color.lightGray);
	JLabel boardSizeMsg = Panel1.label("Choose the Board Size", 14);
	JSpinner rowSpinner = Panel1.spinner(8, true);
	JLabel rowLabel = Panel1.label("Rows (Default: 8)", 14);
	JSpinner colSpinner = Panel1.spinner(8, true);
	JLabel colLabel = Panel1.label("Columns (Default: 8)", 14);
	
	// Panel 4
	JPanel startPanel4 = Panel1.panel(Color.lightGray);
	JButton startGame = Panel1.button(40, 20, "Start Game");
	
	// Panel 5
	JPanel startPanel5 = Panel1.panel(Color.lightGray);
	JButton rules = Panel1.button(40, 20, "Rules");
	JButton highScores = Panel1.button(40, 20, "High Scores");
	JButton exit = Panel1.button(40, 20, "Exit");
	
	// Forms the Panel
	public void makeStartPanel() {
		
		rowSpinner.add(rowLabel);
		colSpinner.add(colLabel);
		JComponent[] components = {welcomeMsg1, 
				welcomeMsg2, 
				shipPlacement, 
				scoringSystem, 
				boardSizeMsg, 
				rowLabel, 
				rowSpinner, 
				colLabel, 
				colSpinner,
				startGame,
				rules,
				highScores,
				exit
				};
		
		// Add the components to the Panel and Set the Layout
		startFrame.getContentPane().add(startPanel0);
		
		// Panel 1
		startPanel1.add(components[0], BorderLayout.NORTH);
		
		// Panel 2
		startPanel2.setLayout(new BoxLayout(startPanel2, 2));
		startPanel2.add(components[1]);
		
		// Panel 3 (Including Panel 3_1)
		startPanel3.setLayout(new BoxLayout(startPanel3, 2));
		for (int i = 2; i < 4; i++) {
			startPanel3.add(components[i]);
		}
		startPanel3_1.setLayout(new BoxLayout(startPanel3_1, 1));
		for (int i = 4; i < 9; i++) {
			startPanel3_1.add(components[i]);
		}
		startPanel3.add(startPanel3_1);
		
		// Panel 4
		startPanel4.setLayout(new BoxLayout(startPanel4, 2));
		startPanel4.add(components[9]);
		
		// Panel 5
		startPanel5.setLayout(new BoxLayout(startPanel5, 2));
		for (int i = 10; i < 13; i++) {
			startPanel5.add(components[i]);
		}
		
		// Add Panels 1-5 to Panel 0
		startPanel0.setLayout(new BoxLayout(startPanel0, 1));
		startPanel0.add(startPanel1);
		startPanel0.add(startPanel2);
		startPanel0.add(startPanel3);
		startPanel0.add(startPanel4);
		startPanel0.add(startPanel5);
		startFrame.setVisible(true);
	}

}
