/*
 * GUI MENU - Collection of all the GUI elements that are needed to make the components of the game
 * A "Dropbox" basically - one single place to choose all 
 * the required parts)
 */

package battleship;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.util.ArrayList;
import javax.swing.*;
import battleship.GUIMenu;

// Initialisation of several different components
public class GUIMenu {
	
	JFrame frame;
	JPanel panel;
	JLabel label;
	JButton button;
	JButton gButton;
	JSpinner spinner;
	JTextArea txtarea;
	JRadioButton radio;
	JOptionPane optionPaneDialog;
	JOptionPane optionPane;
	JTextField txtField;
	

	// Makes a Frame
	public JFrame frame(int width, int height, String text, int value, boolean visible) {
		
		// Custom parameters
		frame = new JFrame();
		frame.setTitle(text);
		frame.setSize(height, width);
		frame.setLocationRelativeTo(null);
		frame.setDefaultCloseOperation(value);
		frame.setVisible(visible);
		frame.setBackground(Color.black);
		return frame; 
	}
	
	// Makes a Panel
	public JPanel panel(Color colour) {
		panel = new JPanel();
		panel.setBackground(colour);
		return panel;
	}
	
	// Makes a Label
	public JLabel label(String text, int fontSize) {
		label = new JLabel(text);
		label.setFont(new Font("Calibri", Font.BOLD, fontSize));
		return label;
	}
	
	// Makes a Button
	public JButton button(int width, int height, String text) {
		button = new JButton(text);
		button.setSize(height, width);
		button.setBackground(Color.green);
		return button;
	}
	
	// Makes a Grid Button
	public JButton gridButton(int width, int height, Color bgcolour) {
		gButton = new JButton();
		gButton.setSize(height, width);
		gButton.setBackground(bgcolour);
		return gButton;
	}

	// Makes a Spinner
	public JSpinner spinner(int defValue, boolean enable) {
		spinner = new JSpinner();
		spinner.setValue(defValue);
		spinner.setEnabled(enable);
		spinner.setBackground(Color.green);
		return spinner;
	}
	
	// Makes a TextArea
	public JTextArea textArea(int width, int height, ArrayList<String> fileContent, int fontSize, Color colour) {
		txtarea = new JTextArea();
		txtarea.setSize(width, height);
		for (String i:fileContent) {
			txtarea.append(i + "\n");
		}
		txtarea.setFont(new Font("Calibri", Font.BOLD, fontSize));
		txtarea.setBackground(colour);
		txtarea.setEditable(false);
		txtarea.setLineWrap(true);
		return txtarea;
	}
	
	// Makes a TextField
	public JTextField textField(int width, int height, int fontSize, Color color, boolean visible, boolean activate) {
		txtField = new JTextField();
		txtField.setPreferredSize(new Dimension(width, height));
		txtField.setFont(new Font("Calibri", Font.BOLD, fontSize));
		txtField.setBackground(color);
		txtField.setEditable(true);
		txtField.setVisible(visible);
		txtField.setEnabled(activate);
		return txtField;
	}
	
	// Makes a Radio Button
	public JRadioButton radioButton(String text, int fontSize) {
		radio = new JRadioButton();
		radio.setText(text);
		radio.setFont(new Font("Calibri", Font.CENTER_BASELINE, fontSize));
		return radio;
	}
	
	// Makes an Error Option Pane
	public JOptionPane optionPaneDialog(JFrame frame, String title, String text, int msgCode) {
		optionPaneDialog = new JOptionPane();
		JOptionPane.showMessageDialog(frame, text, title, msgCode);
		return optionPaneDialog;
	}

}
