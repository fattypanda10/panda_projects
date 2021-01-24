/*
 * GAME EVENTS - Events that handle the main game playing and control the various buttons on 
 * the main game board, namely, high scores and quit game
 */

package battleship;


import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;


// Gaming Event class
public class GameEvents {
	GameBoard gamingPanel;
	int turnCounter = 0;
	int carCount = 0;
	int batCount = 0;
	int subCount = 0;
	int desCount = 0;
	int shipCount = 0;
	
	
	// Game Event class constructor which takes a GameBoard as its argument
	public GameEvents(GameBoard playingPanel) {
		gamingPanel = playingPanel;
	}
	
	// High Scores
	public void highScoresButton() {
		gamingPanel.highScores.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				File scoresFile = new File("HighScores.txt");
				Scanner scan;
				try {
					scan = new Scanner(scoresFile);
					while (scan.hasNextLine()) {
						System.out.println(scan.nextLine());
					}
				} catch (FileNotFoundException e1) {
					e1.printStackTrace();
				}
			}
			
		});
	}
		
	
	// Quit Game
	public void quitGameButton() {
		gamingPanel.quitGame.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				gamingPanel.gameFrame.dispose();
			}
		});
	}
	
	
	//Main GamePlay Logic - Executes the Game - Player Turns, Score Keeping, Game End Criteria, Final winner pop up, Append High Scores to File
	public void mainGamePlay(String scoringOption, int rows, int cols, JButton[][] grids, ArrayList<List<ArrayList<Integer>>> coordinates) {
		List<ArrayList<Integer>> carrier = coordinates.get(0);
		List<ArrayList<Integer>> battleship =coordinates.get(1);
		List<ArrayList<Integer>> submarine = coordinates.get(2);
		List<ArrayList<Integer>> destroyer = coordinates.get(3);
		
		// Labels displaying the player 1 score, Turn and Player 2 Score
		JLabel p1Score = gamingPanel.scoresTurn[0];
		JLabel turn = gamingPanel.scoresTurn[1];
		JLabel p2Score = gamingPanel.scoresTurn[2];
		
		for (int r = 0; r < rows; r++) {
			for (int s = 0; s < cols; s++) {
				ArrayList<Integer> z = new ArrayList<Integer>();
				ArrayList<ArrayList<Integer>> usedTiles = new ArrayList<ArrayList<Integer>>();
				z.add(r);
				z.add(s);
				grids[r][s].addActionListener(new ActionListener() {
					@Override
					public void actionPerformed(ActionEvent e) {
						if (e.getSource() instanceof JButton) {
							
							// To ensure that used tiles are discarded and do not count towards Turn and the score
							if (!usedTiles.contains(z)) {
								usedTiles.add(z);
								
								// Same Points per Hit
								if (scoringOption == "1") {
									
									if (carrier.contains(z)) {
										carCount++;
										
										// For deciding Player turn - Odd Moves - Player 2, Even moves- Player 1
										if (turnCounter % 2 != 0) {
											
											if (carCount == carrier.size()) {
												p2Score.setText(String.valueOf(2 * (Integer.valueOf("20")) + Integer.valueOf(p2Score.getText())));
											} else {
												p2Score.setText(String.valueOf(Integer.valueOf("20") + Integer.valueOf(p2Score.getText())));
											}
										turn.setText("Player 1");
										
										} else {
											
											if (carCount == carrier.size()) {
												p1Score.setText(String.valueOf((2 * Integer.valueOf("20")) + Integer.valueOf(p1Score.getText())));
											} else {
												p1Score.setText(String.valueOf(Integer.valueOf("20") + Integer.valueOf(p1Score.getText())));
											}
											
										turn.setText("Player 2");
										
										}
										
										
									} else if (battleship.contains(z)) {
										
										batCount++;
										
										if (turnCounter % 2 != 0) {
											
											if (batCount == battleship.size()) {
												p2Score.setText(String.valueOf((2 * Integer.valueOf("20")) + Integer.valueOf(p2Score.getText())));
											} else {
												p2Score.setText(String.valueOf(Integer.valueOf("20") + Integer.valueOf(p2Score.getText())));
											}
										turn.setText("Player 1");
										
										} else {
											
											if (batCount == battleship.size()) {
												p1Score.setText(String.valueOf((2 * Integer.valueOf("20")) + Integer.valueOf(p1Score.getText())));
											} else {
												p1Score.setText(String.valueOf(Integer.valueOf("20") + Integer.valueOf(p1Score.getText())));
											}
											
										turn.setText("Player 2");
										}
										
									} else if (submarine.contains(z)) {
										
										subCount++;
										
										if (turnCounter % 2 != 0) {
											if (subCount == submarine.size()) {
												p2Score.setText(String.valueOf((2 * Integer.valueOf("20")) + Integer.valueOf(p2Score.getText())));
											} else {
												p2Score.setText(String.valueOf(Integer.valueOf("20") + Integer.valueOf(p2Score.getText())));
											}
										
										turn.setText("Player 1");
										
										} else {
											if (subCount == submarine.size()) {
												p1Score.setText(String.valueOf((2 * Integer.valueOf("20")) + Integer.valueOf(p1Score.getText())));
											} else {
												p1Score.setText(String.valueOf(Integer.valueOf("20") + Integer.valueOf(p1Score.getText())));
											}
										
										turn.setText("Player 2");
										}
										
									} else if (destroyer.contains(z)) {
										
										desCount++;
										
										if (turnCounter % 2 != 0) {
											if (desCount == destroyer.size()) {
												p2Score.setText(String.valueOf((2 * Integer.valueOf("20")) + Integer.valueOf(p2Score.getText())));
											} else {
												p2Score.setText(String.valueOf(Integer.valueOf("20") + Integer.valueOf(p2Score.getText())));
											}
										
										turn.setText("Player 1");
										
										} else {
											if (desCount == destroyer.size()) {
												p1Score.setText(String.valueOf((2 * Integer.valueOf("20")) + Integer.valueOf(p1Score.getText())));
											} else {
												p1Score.setText(String.valueOf(Integer.valueOf("20") + Integer.valueOf(p1Score.getText())));
											}
										
										turn.setText("Player 2");
										}
										
									} else {
										
										if (turnCounter % 2 != 0) {
										p2Score.setText(String.valueOf(Integer.valueOf("0") + Integer.valueOf(p2Score.getText())));
										turn.setText("Player 1");
										
										} else {
										p1Score.setText(String.valueOf(Integer.valueOf("0") + Integer.valueOf(p1Score.getText())));
										turn.setText("Player 2");
										}
									}
									
								
								// Unique points per hit
								} else if (scoringOption == "2") {
									
									if (carrier.contains(z)) {
										
										carCount++;
										
										if (turnCounter % 2 != 0) {
											
											if (carCount == carrier.size()) {
												p2Score.setText(String.valueOf(2 * (Integer.valueOf("40")) + Integer.valueOf(p2Score.getText())));
											} else {
												p2Score.setText(String.valueOf(Integer.valueOf("40") + Integer.valueOf(p2Score.getText())));
											}
										turn.setText("Player 1");
										
										} else {
											
											if (carCount == carrier.size()) {
												p1Score.setText(String.valueOf((2 * Integer.valueOf("40")) + Integer.valueOf(p1Score.getText())));
											} else {
												p1Score.setText(String.valueOf(Integer.valueOf("40") + Integer.valueOf(p1Score.getText())));
											}
											
										turn.setText("Player 2");
										
										}
										
									} else if (battleship.contains(z)) {
										
										batCount++;
										
										if (turnCounter % 2 != 0) {
											
											if (batCount == battleship.size()) {
												p2Score.setText(String.valueOf((2 * Integer.valueOf("30")) + Integer.valueOf(p2Score.getText())));
											} else {
												p2Score.setText(String.valueOf(Integer.valueOf("30") + Integer.valueOf(p2Score.getText())));
											}
										turn.setText("Player 1");
										
										} else {
											
											if (batCount == battleship.size()) {
												p1Score.setText(String.valueOf((2 * Integer.valueOf("30")) + Integer.valueOf(p1Score.getText())));
											} else {
												p1Score.setText(String.valueOf(Integer.valueOf("30") + Integer.valueOf(p1Score.getText())));
											}
											
										turn.setText("Player 2");
										}
										
									} else if (submarine.contains(z)) {
										
										subCount++;
										
										if (turnCounter % 2 != 0) {
											if (subCount == submarine.size()) {
												p2Score.setText(String.valueOf((2 * Integer.valueOf("20")) + Integer.valueOf(p2Score.getText())));
											} else {
												p2Score.setText(String.valueOf(Integer.valueOf("20") + Integer.valueOf(p2Score.getText())));
											}
										
										turn.setText("Player 1");
										
										} else {
											if (subCount == submarine.size()) {
												p1Score.setText(String.valueOf((2 * Integer.valueOf("20")) + Integer.valueOf(p1Score.getText())));
											} else {
												p1Score.setText(String.valueOf(Integer.valueOf("20") + Integer.valueOf(p1Score.getText())));
											}
										
										turn.setText("Player 2");
										}
										
									} else if (destroyer.contains(z)) {
										
										desCount++;
										
										if (turnCounter % 2 != 0) {
											if (desCount == destroyer.size()) {
												p2Score.setText(String.valueOf((2 * Integer.valueOf("10")) + Integer.valueOf(p2Score.getText())));
											} else {
												p2Score.setText(String.valueOf(Integer.valueOf("10") + Integer.valueOf(p2Score.getText())));
											}
										
										turn.setText("Player 1");
										
										} else {
											if (desCount == destroyer.size()) {
												p1Score.setText(String.valueOf((2 * Integer.valueOf("10")) + Integer.valueOf(p1Score.getText())));
											} else {
												p1Score.setText(String.valueOf(Integer.valueOf("10") + Integer.valueOf(p1Score.getText())));
											}
										
										turn.setText("Player 2");
										}
										
									} else {
										
										if (turnCounter % 2 != 0) {
										p2Score.setText(String.valueOf(Integer.valueOf("0") + Integer.valueOf(p2Score.getText())));
										turn.setText("Player 1");
										
										} else {
										p1Score.setText(String.valueOf(Integer.valueOf("0") + Integer.valueOf(p1Score.getText())));
										turn.setText("Player 2");
										}
									}
									
								}
								
								// Increasing the turn counter and also the used coordinates
								turnCounter++;
								shipCount = carCount + batCount + subCount + desCount;
								
						}
							// Once all ships have sunk
							if (shipCount == carrier.size() + battleship.size() + submarine.size() + destroyer.size()) {
								
								// Append Game Results to the File - "HighScores.txt"
								try {
									FileWriter gameResult = new FileWriter("HighScores.txt", true);
									if (Integer.valueOf(p1Score.getText()) > Integer.valueOf(p2Score.getText())) {
										gameResult.append("\n");
										gameResult.append("Player 1: " + p1Score.getText());
									} else if (Integer.valueOf(p1Score.getText()) < Integer.valueOf(p2Score.getText())) {
										gameResult.append("\n");
										gameResult.append("Player 2: " + p2Score.getText());
									} else {
										gameResult.append("\n");
										gameResult.append("Draw: " + p1Score.getText());
									}
									gameResult.close();
								} catch (IOException e1) {
									e1.printStackTrace();
								}
								
								// Final PopUp announcing the winner and ending the game with "Ok"
								GUIMenu finalResult = new GUIMenu();
								String winner;
								if (Integer.valueOf(p1Score.getText()) > Integer.valueOf(p2Score.getText())) {
									winner = "Game Over: Player 1 Wins!";
								} else if (Integer.valueOf(p1Score.getText()) < Integer.valueOf(p2Score.getText())) {
									winner = "Game Over: Player 2 Wins!";
								} else {
									winner = "Game Over: Scores Tied/Draw!";
								}
								JFrame gameEndFrame = finalResult.frame(125, 300, "", 3, false);
								JOptionPane finalPopUp = finalResult.optionPaneDialog(gameEndFrame, "Game Over", winner, -1); 
								gameEndFrame.getContentPane().add(finalPopUp);			 
								gameEndFrame.dispose();
							}
							
							
						}
					}
				});			
			} 
		} 
		
	}
	
}
