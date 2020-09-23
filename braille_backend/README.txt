
**************************************************************

HOW TO START

**************************************************************

// first make the connections according to the given circuit diagram

	// the circuit diagram shows only connection for one braille unit (with 6 solenoids, which displays one
		english character at a time) but more can be added

// to run codes:

	// setup service account key for firebase

	// save the key as "key.json" in current directory

	// copy and place the directory on raspberry pi

	// change the values of "root", "i_dir", "err_dir", "cnfm_dir" & "read_dir" variables in "headers.py"
		according to the new directory location

// run the codes


**************************************************************

WHAT EACH FILE IS FOR

**************************************************************

// NOTE : GO THROUGH THE "braille.py" PROGRAM TO CLEARLY UNDERSTAND THE WORKING OF THE ENTIRE BRAILLE SYSTEM

// "braille.py" can be run on any computer to help understand how the braille output of system works

// "braille.py" displays the braille output in terms of a "3x2 matrix of 1's and 0's" (1 => high; 0 => low)

// "braille.py" is also used as a header file in the "read.py" and "read_text_file.py" programs

// the "circuit_diagram.png" shows all the connections in color-coded format clearly, along with pinout
	decription for each of the 3 main parts we use :
	1)	RASPBERRY PI
	2)	74HC595 SHIFT REGISTER
	3)	ULN2803A DARLINGTON TRANSISTOR ARRAY

// directories "errs" & "load_instructions" contains audio files for various error and instruction messages

// "headers.py" contains definitions for various functions which help simplify voice input and ouput

// "firebase.py" contains definitions for various functions which help simplify load, listen, read as well as
	firebase connectivity operations

// "load.py" is the program that downloads requested files from firebase cloud by taking user voice input

// "listen.py" is the program which takes user voice input for name of book and then outputs the audio files
	associated	with the requested book

// "read.py" is the program which demonstrates the working of the braille unit with all the characters

// "read_text_file.py" is the program which takes user voice input for name of book and then controls the braille
	units according to the text files associated with the requested book