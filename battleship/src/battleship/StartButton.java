/*
 * STARTBUTTON - The starting point for the players to play the game, present on the starting panel and once all settings
 * are deemed correct from the user's end, the game can be started by clicking on this button
 */

package battleship;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Scanner;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;


// Start Button Class with relevant methods for the required settings on the Starting Panel
public class StartButton {
	
	// Initialisation of the variables
	StartPanel startPanel = new StartPanel();
	StartEvents starter = new StartEvents(startPanel);
	String[] playPanel = {"0", "Player 1", "0"}; 
	ArrayList<Integer> dims;
	ArrayList<String> fileContent = new ArrayList<String>();
	
	// Method for Generating the set of coordinates for Random Placement
	public ArrayList<List<ArrayList<Integer>>> getRandomCoordinates(int rows, int cols, int rowOrColGeneration) {
		
		// Common Variables and Values
		int carLen = 5;
		int batLen = 4;
		int subLen = 3;
		int desLen = 2;
		int[] shipLen = {carLen, batLen, subLen, desLen};
		int totalShips = shipLen[0] + shipLen[1] + shipLen[2] + shipLen[3];
		Random randNum = new Random();
		ArrayList<List<ArrayList<Integer>>> coordinates = new ArrayList<List<ArrayList<Integer>>>();
		
		
		// CHOICE 1 - Either Row or Col Generation (For 5 <= Rows & Cols <=7) (Small Grid - to avoid overlap)
		if (rowOrColGeneration == 1) {
			
			int rowColChoice = randNum.nextInt(2);
			ArrayList<ArrayList<Integer>> validCoordinates = new ArrayList<ArrayList<Integer>>();
			if (rowColChoice == 0) {
				
				// Ship be placed on rows (horizontal)
				for (int p = 0; p < shipLen.length; p ++) {
					ArrayList<Integer> xyPair = new ArrayList<Integer>();
					ArrayList<ArrayList<Integer>> coordSet = new ArrayList<ArrayList<Integer>>();
					int maxCol = cols - (shipLen[p] - 1);
					int[] yCoords = new int[shipLen[p]];
					int counter = 0;
					while (true) {
						int x = randNum.nextInt(rows);
						int y0 = randNum.nextInt(maxCol);
						
						for (int i = 0; i < shipLen[p]; i ++) {
							yCoords[i] = y0 + i;
							xyPair.add(x);
							xyPair.add(yCoords[i]);
							coordSet.add(xyPair);
							xyPair = new ArrayList<Integer>();
						}
						
						// checking for every coordinate if it's valid or not
						for (int q = 0; q < coordSet.size(); q++) {
							if (validCoordinates.contains(coordSet.get(q))) {
								coordSet = new ArrayList<ArrayList<Integer>>();
								break;
							}
						}
						if (coordSet.size() != 0) {
							for (int r = 0; r < coordSet.size(); r++) {
								validCoordinates.add(coordSet.get(r));
								counter++;
							}
						}										
						if (counter == shipLen[p]) {
							break;
						}
					}
				}
			} else if (rowColChoice == 1) {
				
//				Ship be placed on cols (vertical)
				for (int p = 0; p < shipLen.length; p ++) {
					ArrayList<Integer> xyPair = new ArrayList<Integer>();
					ArrayList<ArrayList<Integer>> coordSet = new ArrayList<ArrayList<Integer>>();
					int maxRow = rows - (shipLen[p] - 1);
					int[] xCoords = new int[shipLen[p]];
					int counter = 0;
					while (true) {
						int y = randNum.nextInt(cols);
						int x0 = randNum.nextInt(maxRow);
						for (int i = 0; i < shipLen[p]; i ++) {
							xCoords[i] = x0 + i;
							xyPair.add(xCoords[i]);
							xyPair.add(y);
							coordSet.add(xyPair);
							xyPair = new ArrayList<Integer>();
						}
						// checking for every coordinate if it's valid or not
						for (int q = 0; q < coordSet.size(); q++) {
							if (validCoordinates.contains(coordSet.get(q))) {
								coordSet = new ArrayList<ArrayList<Integer>>();
								break;
							}
						}
						if (coordSet.size() != 0) {
							for (int r = 0; r < coordSet.size(); r++) {
								validCoordinates.add(coordSet.get(r));
								counter++;
							}
						}										
						if (counter == shipLen[p]) {
							break;
						}
					}
				}
			}
			
			// Extracting coordinates for each ship from one single group of total coordinates
			List<ArrayList<Integer>> carrierDim = validCoordinates.subList(0, carLen);
			
			List<ArrayList<Integer>> battleshipDim = validCoordinates.subList(carLen, 
																			carLen + batLen);
			
			List<ArrayList<Integer>> submarineDim = validCoordinates.subList(carLen + batLen, 
																			carLen + batLen + subLen);
			
			List<ArrayList<Integer>> destroyerDim = validCoordinates.subList(carLen + batLen + subLen, 
																			totalShips);
			
			coordinates.add(carrierDim); 
			coordinates.add(battleshipDim);
			coordinates.add(submarineDim); 
			coordinates.add(destroyerDim);
					
			
		// CHOICE 2 - Both Row and Col Generation and then Random Choosing for each ship - either to be placed along rows or cols
		// (for Rows & Cols >= 8) (for larger grids)
		} else if (rowOrColGeneration == 2) {
		
			ArrayList<ArrayList<Integer>> validCoordinates = new ArrayList<ArrayList<Integer>>();
			
			// Ship be placed on rows (horizontal)
			for (int p = 0; p < shipLen.length; p ++) {
				ArrayList<Integer> xyPair = new ArrayList<Integer>();
				ArrayList<ArrayList<Integer>> coordSet = new ArrayList<ArrayList<Integer>>();
				int maxCol = cols - (shipLen[p] - 1);
				int[] yCoords = new int[shipLen[p]];
				int counter = 0;
				while (true) {
					int x = randNum.nextInt(rows);
					int y0 = randNum.nextInt(maxCol);
					
					for (int i = 0; i < shipLen[p]; i ++) {
						yCoords[i] = y0 + i;
						xyPair.add(x);
						xyPair.add(yCoords[i]);
						coordSet.add(xyPair);
						xyPair = new ArrayList<Integer>();
					}
					// checking for every coordinate if it's valid or not
					for (int q = 0; q < coordSet.size(); q++) {
						if (validCoordinates.contains(coordSet.get(q))) {
							coordSet = new ArrayList<ArrayList<Integer>>();
							break;
						}
					}
					if (coordSet.size() != 0) {
						for (int r = 0; r < coordSet.size(); r++) {
							validCoordinates.add(coordSet.get(r));
							counter++;
						}
					}										
					if (counter == shipLen[p]) {
						break;
					}
				}
			}
			//	Ship be placed on cols (vertical)
			for (int p = 0; p < shipLen.length; p ++) {
				ArrayList<Integer> xyPair = new ArrayList<Integer>();
				ArrayList<ArrayList<Integer>> coordSet = new ArrayList<ArrayList<Integer>>();
				int maxRow = rows - (shipLen[p] - 1);
				int[] xCoords = new int[shipLen[p]];
				int counter = 0;
				while (true) {
					int y = randNum.nextInt(cols);
					int x0 = randNum.nextInt(maxRow);
					for (int i = 0; i < shipLen[p]; i ++) {
						xCoords[i] = x0 + i;
						xyPair.add(xCoords[i]);
						xyPair.add(y);
						coordSet.add(xyPair);
						xyPair = new ArrayList<Integer>();
					}
					// checking for every coordinate if it's valid or not
					for (int q = 0; q < coordSet.size(); q++) {
						if (validCoordinates.contains(coordSet.get(q))) {
							coordSet = new ArrayList<ArrayList<Integer>>();
							break;
						}
					}
					if (coordSet.size() != 0) {
						for (int r = 0; r < coordSet.size(); r++) {
							validCoordinates.add(coordSet.get(r));
							counter++;
						}
					}										
					if (counter == shipLen[p]) {
						break;
					}
				}
			}
			
			// ShipSet 1 - Horizontal
			List<ArrayList<Integer>> carrier1Dim = validCoordinates.subList(0, carLen);
			
			List<ArrayList<Integer>> battleship1Dim = validCoordinates.subList(carLen, 
																			carLen + batLen);
			
			List<ArrayList<Integer>> submarine1Dim = validCoordinates.subList(carLen + batLen, 
																			carLen + batLen + subLen);
			
			List<ArrayList<Integer>> destroyer1Dim = validCoordinates.subList(carLen + batLen + subLen, 
																			totalShips);
			
			// ShipSet 2 - vertical
			List<ArrayList<Integer>> carrier2Dim = validCoordinates.subList(totalShips, 
																			totalShips + carLen);
			
			List<ArrayList<Integer>> battleship2Dim = validCoordinates.subList(totalShips + carLen, 
																			totalShips + carLen+ batLen);
			
			List<ArrayList<Integer>> submarine2Dim = validCoordinates.subList(totalShips + carLen+ batLen, 
																			totalShips + carLen+ batLen + subLen);
			
			List<ArrayList<Integer>> destroyer2Dim = validCoordinates.subList(totalShips + carLen+ batLen + subLen, 
																			(2 * totalShips));
							
			// random selection of ships (horizontal or vertical) 
			int[] shipChoices = new int[shipLen.length];
			for (int r =0; r < shipLen.length; r++) {
				shipChoices[r] = randNum.nextInt(2);
			}
			List<ArrayList<Integer>> carrierDim;
			List<ArrayList<Integer>> battleshipDim;
			List<ArrayList<Integer>> submarineDim;
			List<ArrayList<Integer>> destroyerDim;
			
			if (shipChoices[0] == 0) {
				carrierDim = carrier1Dim;
			} else {
				carrierDim = carrier2Dim;
			}
			
			if (shipChoices[1] == 0) {
				battleshipDim = battleship1Dim;
			} else {
				battleshipDim = battleship2Dim;
			}
			
			if (shipChoices[2] == 0) {
				submarineDim = submarine1Dim;
			} else {
				submarineDim = submarine2Dim;
			}
			
			if (shipChoices[3] == 0) {
				destroyerDim = destroyer1Dim;
			} else {
				destroyerDim = destroyer2Dim;
			}
			

			coordinates.add(carrierDim); 
			coordinates.add(battleshipDim);
			coordinates.add(submarineDim); 
			coordinates.add(destroyerDim);
			
		}
	// Final set of coordinates for the placement of the ships using the Random placement
	return coordinates;
	
	}

	// Starts the Play (this method is called from the MainRunGame class to start the game application)
	public void initiatePlay() {
		startPanel.makeStartPanel();
		starter.rulesButton();
		starter.highScoresButton();		
		starter.scoringSystem();
		starter.shipPositions();
		starter.exitButton();  
		
		startPanel.startGame.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				
				dims = starter.boardSizeSelector();

				// Boolean conditions for Errors
				boolean dimSize0 = dims.get(0) == 0 && dims.get(1) == 0;
				boolean rowsNotEqualCols = dims.get(0) != dims.get(1);
				boolean dimSizeSmall = dims.get(0) < 5 && dims.get(1) < 5;
				boolean noScoreOption = starter.scoringOptionSelected.equals("-1");
				boolean noShipPlacement = starter.shipPositionSelected.equals("-1");
				boolean rowSpinnerEnabled = startPanel.rowSpinner.isEnabled();
				boolean colSpinnerEnabled = startPanel.colSpinner.isEnabled();
				boolean fileShipPlacement = starter.shipPositionSelected.equals("2");
				boolean randomShipPlacement = starter.shipPositionSelected.equals("1");
				
				
				// Check for Errors (Refer to Report please for more details)
				if ((dimSize0 || rowsNotEqualCols || dimSizeSmall || noScoreOption || noShipPlacement) && rowSpinnerEnabled && colSpinnerEnabled) {
					
					GUIMenu errorMsgWindow = new GUIMenu();
					JFrame errorFrame = errorMsgWindow.frame(100, 400, "", 3, false);
					
					JOptionPane errorMsgPane = errorMsgWindow.optionPaneDialog(errorFrame, 
																				"Error with Game Settings", 
																				"Incorrect/Missing settings: "
																				+ "Please Ensure correct Dimensions (refer to Rule 7 in Rules), Scoring Option & Ship Placement!",
																				0);
					errorFrame.getContentPane().add(errorMsgPane);
					errorFrame.dispose();

				
				// All good - no errors - Continue!
				// Ship Placement Option - if - File Based Placement
					
				} else if ((!noScoreOption) && (fileShipPlacement)) {
				
					//Go ahead with file reading and setup the game board and start the game
					File shipPositionsFile = new File(starter.shipPositionsFileName);
					Scanner scan;
					try {
						scan = new Scanner(shipPositionsFile);	
						while (scan.hasNextLine()) {
							fileContent.add(scan.nextLine());
						}
					} catch (FileNotFoundException e1) {	
						e1.printStackTrace();
					}
					int rows = Integer.valueOf(fileContent.get(0));
					int cols = Integer.valueOf(fileContent.get(0));
					
					// parse the ship positions file
					fileContent.remove(0);
					String[] ships = {"Carrier", "Battleship", "Submarine", "Destroyer"};
					ArrayList<String[]> fileShipNames = new ArrayList<String[]>();
					int nameCheck = 0;
					ArrayList<String[]> posStrings = new ArrayList<String[]>();
					
					for (int i=0; i<fileContent.size(); i ++) {
						posStrings.add(fileContent.get(i).substring(ships[i].length() + 1).split(";", 6));
						fileShipNames.add(fileContent.get(i).substring(0).split(";", 2));
					}
					
					for (int x = 0; x < fileShipNames.size(); x++) {
						if (!fileShipNames.get(x)[0].equals(ships[x])) {
							nameCheck = -1;
						}
					}
					
					// Mainly for formatting the coordinates as proper (x, y) pairs
					ArrayList<ArrayList<Integer>> posIndexes = new ArrayList<ArrayList<Integer>>();
					for (int j=0; j<posStrings.size(); j++) {
						ArrayList<Integer> q = new ArrayList<Integer>();
						String[] temp1 = posStrings.get(j);
						for (String k: temp1) {
							String[] temp2 = k.split("\\*", 6);
							for (int v =0; v < temp2.length; v++) {
								q.add(Integer.valueOf(temp2[v].strip()) - 1);
							}
							posIndexes.add(q);
							q = new ArrayList<Integer>();
						}
					}
					
					int carLen = posStrings.get(0).length; 
					int batLen = posStrings.get(1).length;
					int subLen = posStrings.get(2).length; 
					int desLen = posStrings.get(3).length;
					
					// Same as previously described - extracting ship-specific coordinates from the total coordinates
					List<ArrayList<Integer>> carrierDim = posIndexes.subList(0, carLen);
					List<ArrayList<Integer>> battleshipDim = posIndexes.subList(carLen, carLen + batLen);
					List<ArrayList<Integer>> submarineDim = posIndexes.subList(carLen + batLen, carLen + batLen + subLen);
					List<ArrayList<Integer>> destroyerDim = posIndexes.subList(carLen + batLen + subLen, carLen + batLen + subLen + desLen);
					
					ArrayList<List<ArrayList<Integer>>> coordinates = new ArrayList<List<ArrayList<Integer>>>();
					coordinates.add(carrierDim); 
					coordinates.add(battleshipDim);
					coordinates.add(submarineDim); 
					coordinates.add(destroyerDim);
					
					// for detecting overlap of ships (used further below)
					HashSet<ArrayList<Integer>> coordSet = new HashSet<ArrayList<Integer>>();
					for (int f =0;f < posIndexes.size(); f ++) {
						coordSet.add(posIndexes.get(f));
					}

					// FILE CHECK - number of tiles, overlapping, wrong name, number of ships
					
					// boolean conditions for the file error checks
					boolean not4Ships = coordinates.size() != 4;
					boolean not14Coords = posIndexes.size() != (carLen + batLen + subLen + desLen);
					boolean overlapShips = coordSet.size() != posIndexes.size();
					boolean wrongShipName = nameCheck == -1;
					boolean wrongDimensions = (rows < 5 && cols < 5);
					
					// Checking of errors with file - (please refer to the report for extra details)
					if ((not4Ships) || (not14Coords) || (overlapShips) || (wrongShipName) || (wrongDimensions)) {
						
						GUIMenu errorMsgWindow = new GUIMenu();
						JFrame errorFrame = errorMsgWindow.frame(100, 400, "", 3, false);
						
						JOptionPane errorMsgPane = errorMsgWindow.optionPaneDialog(errorFrame, 
																					"Error with File", 
																					"Wrong/Incorrect Data for Ship Placement: "
																					+ "Please Ensure Correct Ship Placement Data in the File (Refer to Rule 8 in Rules)",
																					0);
						errorFrame.getContentPane().add(errorMsgPane);
						errorFrame.dispose();
						
					} 
						
					startPanel.startFrame.dispose();
					GameBoard gamingPanel = new GameBoard();
					JButton[][] grids = gamingPanel.makeGamePanel(gamingPanel.scoresTurn(playPanel), rows, cols, coordinates);
					GameEvents play = new GameEvents(gamingPanel);
					play.highScoresButton();
					play.quitGameButton();
					play.mainGamePlay(starter.scoringOptionSelected, rows, cols, grids, coordinates);
								
					
				//  Ship Position Option - if Random Placement of Ships is chosen
				} else if ((!dimSize0) && (!rowsNotEqualCols) && (!dimSizeSmall) && (!noScoreOption) && (randomShipPlacement)) {
						
						int rows = dims.get(0);
						int cols = dims.get(1);
						
						if ((rows >=5 && rows <= 7) && (cols >= 5 && cols <= 7)) {
							ArrayList<List<ArrayList<Integer>>> coordinates = getRandomCoordinates(rows, cols, 1);
							startPanel.startFrame.dispose();
							GameBoard gamingPanel = new GameBoard();
							JButton[][] grids = gamingPanel.makeGamePanel(gamingPanel.scoresTurn(playPanel), rows, cols, coordinates);
							GameEvents play = new GameEvents(gamingPanel);
							play.highScoresButton();
							play.quitGameButton();
							play.mainGamePlay(starter.scoringOptionSelected, rows, cols, grids, coordinates);

						} else if (rows >= 8 && cols >= 8) {
							ArrayList<List<ArrayList<Integer>>> coordinates = getRandomCoordinates(rows, cols, 2);
							startPanel.startFrame.dispose();
							GameBoard gamingPanel = new GameBoard();
							JButton[][] grids = gamingPanel.makeGamePanel(gamingPanel.scoresTurn(playPanel), rows, cols, coordinates);
							GameEvents play = new GameEvents(gamingPanel);
							play.highScoresButton();
							play.quitGameButton();
							play.mainGamePlay(starter.scoringOptionSelected, rows, cols, grids, coordinates);
					}
							
				}					
			} 
		
		});	
	}

}
