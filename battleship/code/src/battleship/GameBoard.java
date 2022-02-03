/*
 * GAME BOARD - Similar to the Starting Panel, here the Game Board is formed with the 
 * main component being the grid of tiles (Buttons) with ships hidden behind them
 */

package battleship;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
import javax.swing.*;

// Different Components of the game board
public class GameBoard {
	
	GUIMenu Panel2 = new GUIMenu();
	JFrame gameFrame = Panel2.frame(600, 600, "Battleship", 3, true);
	
	// Panel 0
	JPanel playPanel0 = Panel2.panel(Color.lightGray);
	
	// Panel 1
	JPanel playPanel1 = Panel2.panel(Color.lightGray);
	JButton highScores = Panel2.button(50, 20, "High Scores");
	JLabel player1Score = Panel2.label("Player 1 Score:", 16);
	JLabel playerTurn = Panel2.label("Turn:", 16);
	JLabel player2Score = Panel2.label("Player 2 Score:", 16);
	JButton quitGame = Panel2.button(50, 20, "Quit Game");
	
	// Panel 2
	JPanel playPanel2 = Panel2.panel(Color.lightGray);
	JLabel[] scoresTurn = new JLabel[3];
	
	// Array of Labels for starting the game with the Player 1 Score, Turn and Player 2 Score
	public JLabel[] scoresTurn(String[] values) {
		scoresTurn[0] = Panel2.label(values[0], 16);
		scoresTurn[1] = Panel2.label(values[1], 16);
		scoresTurn[2] = Panel2.label(values[2], 16);
		return scoresTurn;
	}
	
	// Panel 3
	JPanel playPanel3 = Panel2.panel(Color.darkGray);
	
	// Make Game Panel - the "Heart" of the game
	public void makeGamePanel(JLabel[] valueLabels, int rows, int cols) {
		
		JComponent[] components = {highScores,
								player1Score,
								playerTurn,
								player2Score,
								quitGame, 
								};

		gameFrame.getContentPane().add(playPanel0);
		
		// Add to Panel 1
		playPanel1.setLayout(new BoxLayout(playPanel1, 2));
		for (int i = 0; i < components.length; i++) {
			playPanel1.add(components[i]);
			playPanel1.add(Box.createHorizontalGlue());
		}
		
		// Add to Panel 2
		playPanel2.setLayout(new BoxLayout(playPanel2, 2));
		playPanel2.add(valueLabels[0]);
		playPanel2.add(Box.createRigidArea(new Dimension(100,0)));
		playPanel2.add(valueLabels[1]);
		playPanel2.add(Box.createRigidArea(new Dimension(100,0)));
		playPanel2.add(valueLabels[2]);

		// Add to Panel 3
		JButton[] grids = new JButton[rows * cols];
		playPanel3.setLayout(new GridLayout(rows, cols));
		for (int i = 0; i < grids.length; i ++) {
			grids[i] = Panel2.gridButton(30, 30, Color.darkGray);
			grids[i].addActionListener(new ActionListener() {
				@Override
				public void actionPerformed(ActionEvent e) {
					if (e.getSource() instanceof JButton) {	
						((JButton) e.getSource()).setBackground(Color.blue);
					}
				}
			});
			playPanel3.add(grids[i]);
		}
//		
		// Add Panels 1-2 to Panel 0
		playPanel0.setLayout(new BoxLayout(playPanel0, 1));
		playPanel0.add(playPanel1);
		playPanel0.add(playPanel2);
		playPanel0.add(playPanel3);
		
	}
	
	// Overloaded Method with the option to change colours depending on the ship coordinates
	// Adds action listeners for each button in the grid to change colour on clicking
	public JButton[][] makeGamePanel(JLabel[] valueLabels, int rows, int cols, ArrayList<List<ArrayList<Integer>>> coordinates) {
		
		JComponent[] components = {highScores,
								player1Score,
								playerTurn,
								player2Score,
								quitGame, 
								};

		gameFrame.getContentPane().add(playPanel0);
		
		// Add to Panel 1
		playPanel1.setLayout(new BoxLayout(playPanel1, 2));
		for (int i = 0; i < components.length; i++) {
			playPanel1.add(components[i]);
			playPanel1.add(Box.createHorizontalGlue());
		}
		
		// Add to Panel 2
		playPanel2.setLayout(new BoxLayout(playPanel2, 2));
		playPanel2.add(valueLabels[0]);
		playPanel2.add(Box.createRigidArea(new Dimension(100,0)));
		playPanel2.add(valueLabels[1]);
		playPanel2.add(Box.createRigidArea(new Dimension(100,0)));
		playPanel2.add(valueLabels[2]);

		// Add to Panel 3 - Formation of the Grid of Tiles with the help of the coordinates
		JButton[][] grids = new JButton[rows][cols];
		playPanel3.setLayout(new GridLayout(rows, cols));
		Color[] shipColours = {Color.red, Color.magenta, Color.yellow, Color.black};
		
		//Different coordinates for different types of ships
		List<ArrayList<Integer>> carrier = coordinates.get(0);
		List<ArrayList<Integer>> battleship =coordinates.get(1);
		List<ArrayList<Integer>> submarine = coordinates.get(2);
		List<ArrayList<Integer>> destroyer = coordinates.get(3);
				
		for (int r = 0; r < rows; r++) {
			for (int s = 0; s < cols; s++) {
				grids[r][s] = Panel2.gridButton(30, 30, Color.darkGray);
				ArrayList<Integer> z = new ArrayList<Integer>();
				z.add(r);
				z.add(s);
				grids[r][s].addActionListener(new ActionListener() {
					@Override
					public void actionPerformed(ActionEvent e) {
						if (e.getSource() instanceof JButton) {
							
							// Colour change on clicking the tile depending on the ship hidden behind it
							if (carrier.contains(z)) {
								((JButton) e.getSource()).setBackground(shipColours[0]);

							} else if (battleship.contains(z)) {
								((JButton) e.getSource()).setBackground(shipColours[1]);
								
							} else if (submarine.contains(z)) {
								((JButton) e.getSource()).setBackground(shipColours[2]);
								
							} else if (destroyer.contains(z)) {
								((JButton) e.getSource()).setBackground(shipColours[3]);
								
							} else {
								((JButton) e.getSource()).setBackground(Color.blue);
							}
						}
					}
				});
				playPanel3.add(grids[r][s]);
			}
		}
				
		// Add Panels 1-2 to Panel 0
		playPanel0.setLayout(new BoxLayout(playPanel0, 1));
		playPanel0.add(playPanel1);
		playPanel0.add(playPanel2);
		playPanel0.add(playPanel3);
		return grids;
		
	}

}
