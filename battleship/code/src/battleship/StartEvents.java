/* STARTING EVENTS - ""infuses" life in the starting panel which is already formed/made prior to the calling of this class
 * Different buttons present on the starting panel are made active by adding appropriate action listeners to them
 */

package battleship;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;


// Class for all the events related to the starting panel
public class StartEvents {
	
	// Initialisation of the variables
	StartPanel startingPanel;
	String scoringOptionSelected = "-1";
	String shipPositionSelected = "-1";
	String shipPositionsFileName = "-1";
	
	// Constructor for the class, accepts the starting panel to make it active
	public StartEvents(StartPanel startPanel) {
		startingPanel = startPanel;
	}
	
	
	// Rules Button
	public void rulesButton() {
		startingPanel.rules.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				ArrayList<String> fileContent = new ArrayList<String>();
				File rulesFile = new File("Rules.txt");
				Scanner scan;
				try {
					scan = new Scanner(rulesFile);	
					while (scan.hasNextLine()) {
						fileContent.add(scan.nextLine());
					}
				} catch (FileNotFoundException e1) {	
					e1.printStackTrace();
				}
				GUIMenu panel3 = new GUIMenu();
				JFrame rulesFrame  = panel3.frame(625,850, "Rules", 2, true);
				JPanel rulesPanel = panel3.panel(Color.lightGray);
				JTextArea rulesBook = panel3.textArea(800,800, fileContent, 15, Color.lightGray);
				JButton closeRules = panel3.button(40, 20, "Close");
				rulesFrame.getContentPane().add(rulesPanel);
				rulesPanel.add(rulesBook);
				rulesPanel.add(closeRules);
				closeRules.addActionListener(new ActionListener () {
					@Override
					public void actionPerformed(ActionEvent e) {
						rulesFrame.dispose();
					}
				});
			}
		});
	}
			
	
	// High Scores
	public void highScoresButton() {
		startingPanel.highScores.addActionListener(new ActionListener() {
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
	
	
	// Exit Button
	public void exitButton() {
		startingPanel.exit.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				startingPanel.startFrame.dispose();
			}
		});
	}
	
	
	// BoardS Size Selector
	public ArrayList<Integer> boardSizeSelector() {
		ArrayList<Integer> dimensions = new ArrayList<Integer>();
		startingPanel.rowSpinner.addChangeListener(new ChangeListener() {
			@Override
			public void stateChanged(ChangeEvent e) {

			}
		});
		
		startingPanel.colSpinner.addChangeListener(new ChangeListener() {
			@Override
			public void stateChanged(ChangeEvent e) {
			}
		});
		
		dimensions.add((int) startingPanel.rowSpinner.getValue());
		dimensions.add((int) startingPanel.colSpinner.getValue());
		return dimensions;
		
	}
		
	
	// Scoring System Window 
	public void scoringSystem() {
		startingPanel.scoringSystem.addActionListener(new ActionListener () {
			@Override
			public void actionPerformed(ActionEvent e) {
				GUIMenu scoringSystemPanel = new GUIMenu();
				JFrame scoreSystemFrame = scoringSystemPanel.frame(150, 300, "Scoring System", 2, true);
				JPanel scoreSystemPanel = scoringSystemPanel.panel(Color.lightGray);
				JButton confirmSelection = scoringSystemPanel.button(40, 20, "Confirm");
				JRadioButton scoreSystem1 = scoringSystemPanel.radioButton("Option 1: Same Points Per Hit", 15);	
				scoreSystem1.setActionCommand("1");
				JRadioButton scoreSystem2 = scoringSystemPanel.radioButton("Option 2: Unique Points Per Hit", 15);
				scoreSystem2.setActionCommand("2");				
				ButtonGroup scoreSys = new ButtonGroup();
				scoreSys.add(scoreSystem1);
				scoreSys.add(scoreSystem2);
				scoreSystemFrame.getContentPane().add(scoreSystemPanel);
				scoreSystemPanel.add(scoreSystem1);
				scoreSystemPanel.add(scoreSystem2);
				scoreSystemPanel.add(confirmSelection);
				
				// Get Selection Event
				// Option 1
				scoreSystem1.addActionListener(new ActionListener () {
					@Override
					public void actionPerformed(ActionEvent e) {
						if (scoreSystem1.isSelected()) {
							scoringOptionSelected = scoreSystem1.getActionCommand();
							
						}
					}
				});
				// Option 2
				scoreSystem2.addActionListener(new ActionListener () {
					@Override
					public void actionPerformed(ActionEvent e) {
						if (scoreSystem2.isSelected()) {
							scoringOptionSelected = scoreSystem2.getActionCommand();
							
						}
					}
				});
				
				// Confirm Event 
				confirmSelection.addActionListener(new ActionListener() {
					@Override
					public void actionPerformed(ActionEvent e) {
						scoreSystemFrame.dispose();
					}
				});
				
			}
		});
	}
	
	// Ship Positions Option
	public void shipPositions() {
		startingPanel.shipPlacement.addActionListener(new ActionListener () {
			@Override
			public void actionPerformed(ActionEvent e) {
				GUIMenu shipPositions = new GUIMenu();
				JFrame shipPositionsFrame = shipPositions.frame(225, 360, "Placement of Ships", 2, true);
				JPanel shipPositionsPanel = shipPositions.panel(Color.lightGray);
				JButton confirmSelection = shipPositions.button(40, 20, "Confirm");
				JRadioButton shipPlacement1 = shipPositions.radioButton("Option 1: Random Placement of all Ships", 15);	
				shipPlacement1.setActionCommand("1");
				JRadioButton shipPlacement2 = shipPositions.radioButton("Option 2: Ship Placement through Text File.", 15);
				JLabel fileNote1 = shipPositions.label("*For Option 2: ", 12);
				JLabel fileNote2 = shipPositions.label("*The Text File should be in the same Directory as this Project", 12);
				JLabel fileNote3 = shipPositions.label("*The File Name should be added with the extension (.txt)", 12);
				shipPlacement2.setActionCommand("2");
				JTextField fileNameField = shipPositions.textField(150, 25, 14, Color.white, true, false);
				fileNameField.setText("Filename");
				ButtonGroup positions = new ButtonGroup();
				positions.add(shipPlacement1);
				positions.add(shipPlacement2);
				shipPositionsFrame.getContentPane().add(shipPositionsPanel);
				shipPositionsPanel.add(shipPlacement1);
				shipPositionsPanel.add(shipPlacement2);
				shipPositionsPanel.add(fileNameField);
				shipPositionsPanel.add(fileNote1);
				shipPositionsPanel.add(fileNote2);
				shipPositionsPanel.add(fileNote3);
				shipPositionsPanel.add(confirmSelection);
				
				
				// Get Selection Event
				// Option 1
				shipPlacement1.addActionListener(new ActionListener () {
					@Override
					public void actionPerformed(ActionEvent e) {
						if (shipPlacement1.isSelected()) {
							fileNameField.setEnabled(false);
							fileNameField.setText("Filename");
							startingPanel.rowSpinner.setEnabled(true);
							startingPanel.colSpinner.setEnabled(true);
							shipPositionSelected = shipPlacement1.getActionCommand();
							
						}
					}
				});
				
				// Option 2
				shipPlacement2.addActionListener(new ActionListener () {
					@Override
					public void actionPerformed(ActionEvent e) {
						if (shipPlacement2.isSelected()) {
							fileNameField.setEnabled(true);
							fileNameField.setText("");
							startingPanel.rowSpinner.setEnabled(false);
							startingPanel.colSpinner.setEnabled(false);
							shipPositionSelected = shipPlacement2.getActionCommand();
							
						}
					}
				});
				
				// Confirm Event 
				confirmSelection.addActionListener(new ActionListener() {
					@Override
					public void actionPerformed(ActionEvent e) {
						shipPositionsFileName = fileNameField.getText();
						shipPositionsFrame.dispose();
						
					}
				});
				
			}
		});
		
	}

}
