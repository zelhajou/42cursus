`C-x C-f` : opens a file, asks for the name. if it cannot find the file, creates the file

`C-x C-s` : Saves the file

`C-s s`   : Saves all files with a prompt

`C-s C-w` : Saves all files with a different name.

Everytime you save a file, Emacs creates another file with the name *"filename~"*.<br>
This tilde(~) file is the previous version of the file. It will be in the same dir.<br>
Also, Emacs auto-saves everything you type to a file with the name *"#filename#"*.<br>
If you quite Emacs without saving, you can see this **auto-save** file.<br>

`C-x C-c` : quits Emacs

`M-x recover-file `

## Copy/Cut/Paste Commands
`C-k`     : Kills/deletes the whole line, puts it into clipboard.

`C-y`     : PAstes whatever is in the clipboard at the cursor. Subsequent `C-y`'s will keep on pasting.
          
`C-space` : Starts marking/highligting a region.

`M-w`     : Copies this region into the clipboard.

`C-w`     : Cuts this regions into the clipboard (delets the region and copies it to clipbord)
  
Saving a region involves hitting `C-space` to start selecting, and then hitting `M-w` or `C-w` to copy or cut it into the clipboard, and then hitting `C-y` to paste it.If you dont like the region you are selecting, hit `C-g` <br>
`C-g`     : Always quits your command.

## Cursor Commands
`C-a`     : Beginning of line

`C-e`     : End of line

`M->`     : End of buffer

`M-<`     : Beginning of buffer

`C-/`     : Undo

`C-g C-/` : Redo

## Buffer Management Commands
`C-x b`   : Switches buffers, asks you which buffer to switch to.

`C-x C-b` : Switches buffers, but shows you the list of buffers in a new window

Hit `C-x o` (other window) to go the other window and hit `<enter>` on the buffer you want to switch to

`C-x 0` : will close that window

`C-x 1` : will leave only one window

`C-x 2` : Xill make a horizontal cut and show a secondray window

`C-x 3` : Will maje a vertical cut and show a secondary window

## Search Commands
`C-s` : Searches forward as you type. Beware \n is not newline, it is `C-j` When you are within a search, `C-s` will find the next occurance . 
You can always hit `C-g` to quit the search and return where you were.

`M-C-s` : Searches a regexp

Again, hitting `C-s` While you are ine regexp search will find the next occurance.

`C-g` will quit and go back to where your cursor was.

`M-%`   : searches and replaces.
  
`M-s` o : searches and shows all the occurances in an *Occur* buufer. you can clicj on the lines to jumpt to those lines.

`M-x` grep : greps a pattern in  the files you specify and shows the results in a *Grep* buffer. It is similar to "occur" as you can click/enter on the lines to go to that file. > grep -nH -e "is" my_dir/*.txt

`M-x` regrep : will recursively grep in a dircrtory (all the files and subdirectories)

## Commands
Emacs understands lisp, it is a dialect of lisp.

`M-x` command-name : will execute the command.

`M-x` pwd : Prints the working directory

`M-x` indent-region : Indents the region.

hit `M-x` and type anything and hit TAB to auto-complete the commands (or to see the available commands. )

You can hit `M-:` to go to the evaluate buffer where you can evaluate a lisp statement.
for example, "setq" sets a variable to a value.

You can aslo use `C-x` `C-e` to evalute (i.e. run) a lisp statement at the cursor.

`(drts your_var '124)`
`your_var my_var`

## ~/.emacs file and Packages
Emacs is very versatile, you can program it, and add new abilities. let's say that we develop a new language that Emacs does not know about.<br>
All we have to do is to write a "Package" so that Emacs can color-code it for example.Or even write a package for Emacs to auto-complete Keywords in this language.<br>
This makes Emacs a platform for editing many different things.

*~/.emcas* file (A file called ".emacs" under your home directory) holds all the elisp statements that is run when you start your Emacs.<br>
*~/.emacs.d* directory (A directory called ".emacs.d" under your home directory) holds all the packages (files of lisp commands/statements) for Emacs.

You load a package by refering it in a "require" statement.


![[Emacs.jpg]]