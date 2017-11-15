# SRT Flashcards
This script is designed to read directories full of .srt files (specifically from Udacity lectures), and export them to properly formatted .csv files, which can then be batch uploaded to Brainscape to automatically create flashcard decks.  Though flashcards are usually less verbose that these will be, I've found it beneficial to read and re-read transcripts (after watching the videos) and having Brainscape track which material is sticking for me and which material I need to revisit.
Enjoy!
## Usage
1. Download parse_srt.py.
2. Download all transcripts from your Udacity course. To do so, open a course in your browser, watch any video, click the Folder icon in the left sidebar, then click "Transcripts Zip File" to download all transcripts for that course.
3. Open Terminal.
4. Navigate from the command line to the directory containing the `parse_srt.py` Python script.
5. Enter the command `python parse_srt.py <full_path_to_class_transcripts>`.
6. The script will create a folder called "output" inside of the course transcripts directory, and .csv files will be output to that folder. Within each .csv, there is 1 row per video.
## Create Flashcards
1. After completing the above steps, go to your Brainscape account.
2. Create a new "class" (name it after the name of the course you're taking).
3. Once inside your Brainscape class, click IMPORT.
4. Select all of the .csv files inside of the "output" folder.
5. Once the decks are created, you can edit individual cards in your browser using Brainscape's Advanced Editor, to add bolding, underine, make corrections to the transcript text, add images, etc. You can also add more flash cards to your decks later if there are individual small topics and questions you need to improve on.
