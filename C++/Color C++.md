# C++
## ANSI color sequences

``` c ++ 
    \033[33m;    //text yellow
    \033[33;44m  //yellow on blue
    \033[0m;     //restore to default
```
The color sequences are composed of sequences of numbers separated by semicolons.  The most common codes are:

               0   to restore default color
               1   for brighter colors
               4   for underlined text
               5   for flashing text
              30   for black foreground
              31   for red foreground
              32   for green foreground
              33   for yellow (or brown) foreground
              34   for blue foreground
              35   for purple foreground
              36   for cyan foreground
              37   for white (or gray) foreground
              40   for black background
              41   for red background
              42   for green background
              43   for yellow (or brown) background
              44   for blue background
              45   for purple background
              46   for cyan background
              47   for white (or gray) background
##  Escape sequences
To specify control or blank characters in the color sequences, C- style \-escaped notation can be used:

              \a   Bell (ASCII 7)
              \b   Backspace (ASCII 8)
              \e   Escape (ASCII 27)
              \f   Form feed (ASCII 12)
              \n   Newline (ASCII 10)
              \r   Carriage Return (ASCII 13)
              \t   Tab (ASCII 9)
              \v   Vertical Tab (ASCII 11)
              \?   Delete (ASCII 127)
              \_   Space
              \\   Backslash (\)
              \^   Caret (^)
              \#   Hash mark (#)
