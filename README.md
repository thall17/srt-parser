# SRT Parser
This script is designed to read directories full of .srt files (specifically with Udacity lectures in mind), and do the following:
* Output html files, one per lesson, with trascripts in bulleted note format, which can be imported into the Mac Notes app.
* Output csv files, one per lesson, with transcripts listed in the proper format to be uploaded to Brainscape for automated flashcard generation. The front of the card will be the video title, and the back of the card will be the full transcript from that individual video.
Enjoy!
## How to Use
1. Download parse_srt.py.
2. Download all transcripts from your Udacity course. To do so, open a course in a browser, watch any video, click the Folder icon in the left sidebar, then click "Transcripts Zip File" to download all transcripts for that course.
3. Open Terminal.
4. Navigate from the command line to the directory containing the `parse_srt.py` Python script.
5. Enter the command `python parse_srt.py <full_path_to_class_transcripts>`.
6. The script will create a folder called "output" inside of the course transcripts directory. Within that, it will create a "html" directory and a "csv" directory, and output all files to the appropriate folder.

## Afterwards...
### Create Flashcards
1. After completing the above steps, go to your Brainscape account.
2. Create a new "class" (name it after the name of the course you're taking).
3. Once inside your Brainscape class, click IMPORT.
4. Select all of the .csv files inside of the "csv" folder.
5. Once the decks are created, you can edit individual cards in your browser using Brainscape's Advanced Editor, to add bolding, underine, make corrections to the transcript text, add images, etc. You can also add more flash cards to your decks later if there are individual small topics and questions you need to improve on.
### Import into Notes App
1. Open the notes app of your choosing, as long as it allows importing of .html files.
2. Import the .html files in the "html" directory created by the script.
3. Watch lecture videos and edit the notes however you wish (bold certain things, make more sub-bullets, etc.)
