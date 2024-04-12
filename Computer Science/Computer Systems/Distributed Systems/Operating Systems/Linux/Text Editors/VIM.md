
## Global

|key|Description|
|:--------| :--------|
|`:help` *keyword* | open help for keyword|
|`:saveas` *file* | save file as|
|`:close` | close current pane|
|`K`| open man page for word under the cursor|

## Cursor movement

|key|Description|key|Description|
|:--------| :--------| :--------| :--------|
|`h`| move cursor left|`k`| move cursor up|
|`j`|move cursor down|`l`| move cursor right|
|`w`| jump forwards to the start of a word |`W`| jump forwards to the start of a word (words can contain punctuation)|
|`e`| jump forwards to the end of a word|`E`| jump forwards to the end of a word (words can contain punctuation)|
|`b`| jump backwards to the start of a word|`B`| jump backwards to the start of a word (words can contain punctuation)|
|`0`| jump to the start of the line |`$`| jump to the end of the line |
|`gg`| go to the first line of the document |`G`| go to the last line of the document |
|`5G`| go to line 5 |
|`}`| jump to next paragraph (or function/block, when editing code|`{`|jump to previous paragraph (or function/block, when editing code)|
| `Ctrl`+`e`| move screen down one line (without moving cursor) | `Ctrl`+`y`| move screen up one line (without moving cursor) |
| `Ctrl`+`b` | move back one full screen | `Ctrl`+`f` | move forward one full screen |
| `Ctrl`+`d` | move forward 1/2 a screen | `Ctrl`+`u` | move back 1/2 a screen |



## Text Manipulation

|key|Description|key| Description|
|:--------| :--------|  :-------- | :--------| 
| `i` | insert before cursor  |  `r` | replace sigle character  | 
| `I`   | insert at start of line | `cc` | replace line  | 
| `a`   | isnert after cursor     | `cw` | replace to end of word  | 
| `A`   | insert at end of line   |  `c$` | replace to end of line |
| `o`   | add new line below cursor   |  `s` | substitute character |
| `O`   | add new line above cursor   | `S` | substitute line |
| `ea`  | insert at end of line       |  `u` | undo |
| `Esc` | exit insert mode            | `Ctrl`+`r` | redo |

## Text Manipulation Cont.

|key|Description|key| Description|
|:--------| :--------|  :-------- | :--------| 
| `yy` | yank (copy) a line | `yw`   | yank a word    |
| `2yy`   | yank a line | `y$`   | yank to end of line |  
| `p`   | paste after cursor |  `P`   | paste before cursor  |
| `D` | delete to end of line  | `x` | delete character  | 
| `dd`  | delete/cut a line  | `dw` | delete a word       | 
|`/string` | Search for "string" | ||
 
## Marking text (Visual Mode)

|key|Description|key| Description|
|:--------| :--------|  :-------- | :--------| 
| `v` | enter visual mode  | `Ctrl` | start visual block mode  |
| `V` | enter linewise visual mode | `Esc` | exit visual mode | 
|` aw` | mark a word | `ab` | a block with () |
| `aB` | a block with {} | `ib` | inner block with () |
| `iB` | inner block with {} ||

## Visual commands

|key|Description|key| Description|
|:--------| :--------|  :-------- | :--------|
| `>`   | shift text left | `<`   | shift text right | 
| `>>`   | shift left by shiftwidth | `<<`  | shift right by shiftwidth |
| `==` | auto-indent line | `~` | change case |
| `y` | yank (copy) marked text | `d` | delete marked text |

## Registers

|key|Description|
|:--------| :--------|
|`:reg` |show registers content|
|`"xy` | yank into register x|
|`"xp` | paste contents of register x|

Tip Registers are being stored in ~/.viminfo, and will be loaded again on next restart of vim.<br>
Tip Register 0 contains always the value of the last yank command.

## Save & Exit

|key|Description|
|:--------| :--------|
| `ZZ` | save and quit  |
| `ZQ`   | quite without saving |
| `:W`   | write/save | 
| `:q`   | quit (fails if there are changes) |
| `:wq`   | write and quit | 
| `:x`   | write and quit |
| `:q!`  | force quit without saving |
| `:qa` | quite all vim buffers |

## Working with multiple files

|key|Description|key| Description|
|:--------| :--------| :-------- | :--------|
| `:e` file | edit a file in a new buffer | | |
| `:bn` | go to the next buffer |`:bp` |go to the previous buffer|
| `:bd` | delete a buffer (close a file) |`:ls`| list all open buffers|
| `:sp` file | open a file in a new buffer and split window| `:vsp` file | open a file in a new buffer and vertically split window |
|`Ctrl`+`ws`| split window| `Ctrl`+`wv` | split window vertically
| `Ctrl`+`ww`| switch windows| `Ctrl`+`wq`| quit a window|
|`Ctrl`+`wh`| move cursor to the left window (vertical split) |`Ctrl`+`wj` | move cursor to the window below (horizontal split)|
|`Ctrl`+`wl`| move cursor to the right window (vertical split) |`Ctrl`+`wk`| move cursor to the window above (horizontal split)|

## Tabs

|key|Description|key| Description|
|:--------| :--------| :-------- | :--------|
| `:tabnew` | open a file in a new tab |||
| `gt` or `:tabnext` or `:tabn` | move to the next tab | `gT` or `:tabprev` or `:tabp`| move to the previous tab |
| `#gt` | move to tab number # | `:tabmove` `#` | move current tab to the #th position (indexed from 0) |
| `:tabclose` or `:tabc` | close the current tab and all its windows | `:tabonly` or `:tabo`| close all tabs except for the current one |
| `:tabdo` `command` | run the command on all tabs (e.g. :tabdo q - closes all opened tabs)|||

## Search and replace

|key|Description|key| Description|
|:--------| :--------| :-------- | :--------|
| `/pattern` | search for pattern | `?pattern` | search backward for pattern |
| `\vpattern` | 'very magic' pattern: non-alphanumeric characters are interpreted as special regex symbols (no escaping needed) |
| `n` | repeat search in same direction | `N` | repeat search in opposite direction |
| `:%s/old/new/g` | replace all old with new throughout file | `:%s/old/new/gc` | replace all old with new throughout file with confirmations |
| `:noh` | remove highlighting of search matches|||

## Search in multiple files

|key|Description|
|:--------| :--------|
|`:vimgrep` /pattern/ {`{file}`}| search for pattern in multiple files - e.g. :vimgrep /foo/ `*/` |
| `:cn` | jump to the next match |
| `:cp` | jump to the previous match |
| `:copen` | open a window containing the list of matches |


