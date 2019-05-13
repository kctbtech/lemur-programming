# lemur-programming
A programming language fully designed with python. More details can be found on this page: https://mykbtech.weebly.com/lemur-programming.html

# Getting Lemur on My Computer
QUICK DISCLAIMER: v1.5 has been taken down as some new features need to be added. v1.4 can still be used however.
First of all, you will need to have python IDLE installed. It must be version 3.6.4 or newer. If you have that done, you must make sure to have a text editing program on your computer.
Got both! Great!
So, first of all, download version 1.5 or above of the Lemur programming language. Simply click on the file name and you should be able to do it from there!
If you have got that, now go to your downloads area and create a folder called 'Lemur Programming'. Inside of that folder make another folder called 'LemurPrograms' (Make sure it is all joined up). Next get the .py file you installed and drag that into the 'Lemur Programming' folder. Next, get the directory of the LemurPrograms folder and open the .py file you installed.
Scroll down to the bottom of the file and look at the line of code that goes as follows:
file = "/Users/kieranblackley/Downloads/Lemur Programming/LemurPrograms/" + input("Please specify a file name for your program: ")
In the bit that says '/Users/kieranblackley/Downloads/Lemur Programming/LemurPrograms/', replace it with the directory you got from the LemurPrograms folder. If the name 'LemurPrograms' does not appear in the directory, then simply add it to the end of the directory you got. Make sure you put a '/' at the end of the bit you are adding to.

So, you have now installed Lemur on your device. Run the program and hopefully there will be no errors.
You should be asked if you want to use the Lemur shell or run an existing program. 
If you write shell you will be able to write your own stuff and all of that, or if you write program you should be asked to write the filename of your program. You do not have any programs done yet, but you will be able to make some once you find out how to do the basics of Lemur.

# Making a Program
This is very simple. You simply create a .txt file in one of your text editor programs and save it in the 'LemurPrograms' folder. 
When you have viewed the rest of this README.md file, you will be able to create programs in Lemur and hopefully run them withut errors! Don't worry if you make errors, simply view your program and try to get that error away by reviewing over this README.md file and making some enhancements. Don't worry, it is very easy when you get the hang of it!

PLEASE VIEW THE PARTS THAT COME NEXT IN THIS README.md FILE IN YOUR TEXT EDITOR AS THE PIECES OF CODE THAT ARE SHOWN TO BOOST YOUR UNDERSTANDING SEEMED TO GET WRAPPED DOWN INTO ONE LINE. YOUR TEXT EDITOR SHOULD HOPEFULLY NOT WRAP THOSE PIECES OF TEXT. THANK YOU FOR UNDERSTANDING!

# A Basic Hello-World Program
echo "Hello World!"

# Whats to Be Added? (a.k.a Disclaimers)
Lemur is surprisingly easy to learn once you get used to how most of its things are structured. Please be aware that local and global variables have not yet been created. Also, more advanced topics such as classes have not yet been created but please be aware that I might add them. Good news though, define functions (task functions as called in the language) are here, so you can at least make some of your own custom programming structures. However, task functions cannot have their own booleans, inputs etc. yet and instead are more of a way to sort out your code better.

# The Basics
First of all, you will want to know the basic things like:
-if statements;
-input and output;
-variables.
First of all, lets look at input and output.
To output things to the screen you have to write:
echo "Whatever you want to have outputted to the screen."
However, this form of the echo command can only support strings and variables, it cannot support mathematical expressions etc.
So, to output a mathematical expression we would write:
math_echo 10 * 10
That would output 100.
There are a few other variations on the echo command but these two are the ones you would like to know first.

When we want to get user input, we have to write the following:
get_num_input // We use this type of input when the players input is going to be treated as a number // "Whatever message appears to the player" &VariableToAssignTo // You will understand why the & symbol has been used later on 
get_string_input // We use this type of input when the players input is going to be treated as a string // "Whatever message appears to the player" &VariableToAssignTo // Just like said before, you will understand why the & symbol has been used later on 

When structuring an if statement we do not need to indent anything but it is optional if you want to make your code look better and easy to follow.

To write an if statement we would do the following:
if (argument here)
//Whatever would happen in the if statement
breakif
The breakif command tells the compiler that the if statement has ended.

In some languages, two == are used instead of = when writing an if statement. Luckily, the compiler only needs one = to work with in the argument.

So, if we wanted to check if something is equal to something then we would do this:
if (number, expression or variable) = (number, expression or variable)
//Whatever you choose to have happen here
breakif

Else statements have not yet been fully implemented and do not work that well at the moment. We hope to improve them so you can start to use them in your programs.

Variables are another thing you will need to know. In Lemur code, variables are signified by the & symbol. We have to signify if something is a variable, because the Lemur compiler needs to have a good idea of whether you are using a string, number or a variable. Without that information, it might get a bit confusing for the compiler.

Also, when you learn about task functions, you will notice that the compiler might be able to easily confuse the two together.

At the moment, I am finding ways in which to make the compiler notice if something is a variable or not, but I think that is going to be very hard at the moment. Because of this, I am going to keep it this way.

If you want to assign a value to a variable you have to write the following:
If you want to assign a number or expression to a variable you write:
assign_math &Variable (Number or expression goes here)
If you want to assign a string to a variable you write:
assign_string &Variable "String goes here"
If you want to assign a pre-existing variable that is being treated as a number then you write:
assign_num_var &Variable &NameOfPre-ExistingVariable
If you want to assign a pre_existing variable that is being treated as a string then you write:
assign_string_var &Variable &NameOfPre-ExistingVariable

You can also use variables in if statements. You cannot use them in expressions yet, but that feature will be made soon.

Anyways, to use variables in an if statement, then you write:

if &Variable = (Another &variable,  number or expression can go here)
//Whatever stuff is going to happen
breakif

Linking back onto if statements, you can also check if something is bigger or smaller than something else. So if you want to do that, then you write:
if (thing here) > (thing here)
//Stuff
breakif
or
if (thing here) < (thing here)
//Stuff
breakif

Comments are not able to be written in the Lemur language but that will also be added soon in later versions/iterations of it, just in case you were wondering.

Now back on track with variables, you can also increase and decrease variables.
To do that simply write:
var_increase &VarName (Whatever you want to increase it by. This can be a number, expression or another &variable)
or to decrease a variable:
var_decrease &VarName (Whatever you want to increase it by. This can be a number, expression or another &variable)

## Taking it Further
So you like the Lemur programming language so far? Well, there are some more things you can learn. Please remember this is not a high-level programming language, but with your requests and much more it might soon be that!

Anyways, the first thing you might want to know before you go further is what you will learn in this section.
Here we will be looking at:
-String manipulation;
-For loops;
-Returning random integers;
-Task functions.

So lets get started.

We will start with for loops as they are the most easy to grasp.

For loops are written like this:

for (How many times you want to the loop to go on. This can be a number, expression or &variable.)
//Whatever code you want to put in
breakfor

It is that simple. If you want to put a for loop inside of a for loop, or a for loop inside of a for loop inside of a for loop. Then you simply write:
2for (How many times you want to the loop to go on. This can be a number, expression or &variable.)
//Whatever code you want to put in
break2for
or even further:
3for (How many times you want to the loop to go on. This can be a number, expression or &variable.)
//Whatever code you want to put in
break3for

You cannot have 4for or 5for or so on sadly, but I can add more easily. Perhaps up to 5for or 6for.

So now you understand for loops.

The next thing we will look at is string manipulation.
So far, Lemur can replace substrings and take out parts of a single string. It can also join two strings together.
If you want to replace part of a string then you write:
replace "What you want to replace" in (This can be a variable or a string) with "What you want to replace it with"
So, if I wrote this code:
replace "there" in "Hello there!" with "world"
I would get:
Hello world!
Or if I wrote this code:
assign_string &string "Hello there!"
replace "there" in &string with "world"
I would also get:
Hello world!
However, when you just write the replace command, it will assign the replacement to a variable called 'replacement'. So, to get that into one of your own variables you would have to write:
assign_replacement &Variable
Or, if you want to show that on screen you can do:
return_replacement
Instead of:
assign_replacement &Variable
echo &Variable

Next, if you want to join two strings together, you would write:
join "First string here" and "Second string here" //Please remember that if you are going to have a space in between the two strings, you would have to write multiple join commands if you are joining a variable with another variable or write a space before or after one of the existing strings.

So, if I wrote:
join "Hello " and "world!"
I would get:
Hello world!
Or if I wrote:
assign_string &s1 "Hello "
assign_string &s2 "world!"
join &s1 and &s2
I would get:
Hello world!
However, just like the replace function, you will not get an output just by simply writing the function. So, to assign the joined string to another variable you would write:
assign_join &Variable
Or if you want to output the joined string, you would write:
return_join

Now we can look at how to get substrings from a piece of text.

To do that you have to write:
get_substring (Variable or string you are looking at) (Where do you want to start from in the string. This can only be a number, expression or variable) to (Where do you want to end at in the string. This can only be a number, expression or variable)
This will get you a piece of text.

Like in python, the letter you are looking at is represented by whatever letter it is - 1, so n-1 is a thing you will need to remember.
So if I wrote:
get_substring "Hello world!" 0 to 5
I would get:
Hello 
If you want to return just a letter you can just get rid of all of the parts from the 'to'. So if I wanted the second letter (which is represented as 1 in this case), I would write:
get_substring "Hello world!" 2
This would get me:
e

I bet you know what I am going to say now. So, like before, you will not get an output just by writing the function by itself. So, if you want to assign the substring to a variable, you would write:
assign_substring &Variable
If you want to output the substring, you would write:
return_substring

So now we have fully looked at string manipulation. The next thing we need to look at is how to return a random integer.

This is very simple.

You would write:
get_random (number, expression or variable here) to (number, expression or variable here)

So if I wrote:
get_random 1 to 10
I would get:
//Any number in between 1 and 10

Very simple!

Lastly, we need to look at task functions.

A task function is written like this:

task (Task name goes here. Do not use speech marks/inverted commas around the name of function)
//Whatever the function is going to do
breaktask

Remember to write 'breaktask' at the end of a task. If you do not do that, the compiler might merge a task function with something else.

When you want to run a task you have written, you would write:
$NameOfTask

If there are variables you will be using in the task function, that will require data from another function, you would simply write all of the data you would need before calling the task. So, if I wanted to use a variable called 'apples', and I wanted to set it to the variable called 'globalApples', I would write:

assign_num_var &apples &globalApples
$Task

So, before calling the task, you must set the variables you will use in the task beforehand. This is a good alternative to use before I add the feature of having string and number inputs in a task's declaration.


These are all of the basics of Lemur that you will need to know. More features will soon be added. Please request them when you can! Thank you!
