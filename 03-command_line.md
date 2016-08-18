# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > pwd -> print working directory
hostname -> my computer's network name
mkdir -> make directory
cd -> change directory
ls -> list directory
rmdir -> remove directory
pushd -> push directory
popd -> pop directory
cp -> copy a file or a directory
mv -> move a file or directory
less -> page through a file
cat -> print the whole file
xargs -> execute arguments
find -> find files
grep -> find things inside files
man -> read a manual page
apropos -> find what man page is appropriate
env -> look at your environment
echo -> print some arguments
export -> export/set a new environment variable
exit -> exit the shell
sudo -> become a superuser
chmod -> change permission modifiers
chown -> change ownership

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls -> Shows content of directory
ls - a -> Shows all files (including hidden files that start with a dot)
ls -l -> Shows detail about files in long format
ls -lh -> Shows detail of unit formats
ls -lah -> Sama as above but including all files
ls -t -> Sorts by time modified (most recently modified first) then by 
lexographical order
ls - Glp -> enable colorized output and writes a / after directories

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > -G -> Allows colorized output
-F -> Displays a slash after each pathname that is a director, an 
asterisk
after each that is an executable and an @ after symbolic links
-1 -> forces one entry per line
-u -> Sorts by time of last access
-lT -> Displays detailed time information about files 

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs builds a list of arguments that can be used by other
utilities using pipes to create powerful commands. For example, I could
type $ find . - name "*.txt" - type f - print | xarges /bin/rm - f. This
would delete all text files in the current directory.


 

