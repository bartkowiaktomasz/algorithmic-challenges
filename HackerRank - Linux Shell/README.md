# HackeRank - Linux Shell
Solutions to [**HackerRank Linux Shell**](https://www.hackerrank.com/domains/shell)

Useful Sources:
- [A quick guide to writing scripts using the bash shell](http://www.panix.com/~elflord/unix/bash-tute.html)

## Easy
### Let's Echo
> Write a bash script which does just one thing: saying "HELLO".

```shell script
echo 'HELLO'
```

### A Personalized Echo
> Write a Bash script which accepts `name` as input and displays a greeting:
> "Welcome (name)" 

```shell script
read name
echo "Welcome $name"
```

_Note that, unlike double quotes `"`, single quotes `'` will not perform 
string interpolation (variable substitution)._

### Looping and Skipping
> Your task is to use for loops to display only odd natural numbers from `1` to `99`.

```shell script
i=1
while [ $i -le 99 ]
do
    if [ $(($i % 2)) == 1 ]
    then
        echo $i
    fi
    i=$((i+1))
done
```
alternatively:
```shell script
for i in {1..99}
do
    if [ $(($i % 2)) == 1 ]
    then
        echo $i
    fi
done
```

### Looping with numbers
> Use `for` loops to display the natural numbers from `1` to `50`.

```shell script
for i in {1..50}
do
    echo $i
done
```

### The World of Numbers
> Given two integers, `X` and `Y`, find their sum, difference, product, and quotient.
```shell script
read X
read Y
echo $((X + Y))
echo $((X - Y))
echo $((X * Y))
echo $((X / Y))
```

### Comparing Numbers
> Given two integers, `X` and `Y`, identify whether `X<Y` or `X=Y` or `X>Y`.
```shell script
read X
read Y
if [ $X -gt $Y ]
then
    text="is greater than"
elif [ $X == $Y ]
then
    text="is equal to"
else
    text="is less than"
fi
echo "X $text Y"
```

### Getting started with conditionals
> Read in one character from the user (this may be `Y`, `y`, `N`, `n`). 
> If the character is `Y` or `y` display `YES`. If the character is `N` 
> or `n` display `NO`. No other character will be provided as input.

```shell script
read char
if [ $char == 'y' ] || [ $char == 'Y' ]
then
    echo "YES"
elif [ $char == 'n' ] || [ $char == 'N' ]
then
    echo "NO"
fi
```

### More on Conditionals
> Given three integers (`X`, `Y`, and `Z`) representing the three sides 
> of a triangle, identify whether the triangle is Scalene, 
> Isosceles, or Equilateral.

```shell script
read X
read Y
read Z
if [ "$X" == "$Y" ] && [ "$Y" == "$Z" ]
then
    echo "EQUILATERAL"
elif [ "$X" == "$Y" ] || [ "$Y" == "$Z" ] || [ "$X" == "$Z" ] 
then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
```

### Cut #1
```shell script
cut -f1,3 -d ":" /etc/passwd
```
will display only fields (`-f`) `1` and `3`
from `etc/passwd`, with delimiter (`-d`) being `:`. Use flag `-c` to
print characters, e.g. `cut -c1-5` prints characters 1-5.

> Given `N` lines of input, print the `3rd` character from each line 
> as a new line of output.

```shell script
while read line ; do
    echo $line | cut -c3
done
```

### Cut #2
> Display the `2`th and `7`th character from each line of text.

```shell script
while read line; do
    echo $line | cut -c2,7
done 
```

### Cut #3
> Display a range of characters starting at the `2`th position of
> a string and ending at the `7`th position (both positions included).

```shell script
while read line; do
    echo $line | cut -c2-7
done 
```

### Cut #4
> Display the first four characters from each line of text.

```shell script
while read line; do
    echo $line | cut -c1-4
done
```

### Cut 5
> Given a tab delimited file with several columns (`tsv` format) 
> print the first three fields.

```shell script
cut -f-3
```

_NOTE that `TAB` is the default delimiter. There is no need for `while` loop 
as the input get's piped directly to the solution. `echo`ing is also redundant
as the output goes directly to `stdout`._
Solution with explicit delimiter:
```shell script
cut -f-3 -d$'\t'
```

### Cut #6
> Print the characters from thirteenth position to the end.

```shell script
cut -c13-
```

### Cut #7
> Given a sentence, identify and display its fourth word. Assume that the space
> (`' '`) is the only delimiter between words.

```shell script
cut -f4 -d' '
```

### Cut #8
> Given a sentence, identify and display its first three words. Assume that the 
> space (`' '`) is the only delimiter between words.

```shell script
cut -f-3  -d' '
```

### Cut #9
> Given a tab delimited file with several columns (`tsv` format) 
> print the fields from second fields to last field.

```shell script
cut -f2-
```

### Head of a Text File #1
> Display the first `20` lines of an input file.

```shell script
head -n20
```

_NOTE: flag `-n` means "lines", `-c` - "characters", `-f` - "follow"
(e.g. you want to see the log file as it updates live). The same 
flags apply to `tail`._

### Head of a Text File #2
> Display the first `20` characters of an input file.

```shell script
head -c20
```

### Middle of a Text File
> Display the lines (from line number `12` to `22`, both inclusive) 
> of a given text file.

```shell script
head -n22 | tail -n11
```

### Tail of a Text File #1
> Display the last `20` lines of an input file.

```shell script
tail -n20
```

### Tail of a Text File #2
> Display the last `20` characters of an input file.

```shell script
tail -c20
```


### 'Tr' Command #1
_`Tr` stands for "translate", `-d` - delete, `-s` - squeeze
(use e.g. when you want to substitute many repeated whitespaces by one_
> In a given fragment of text, replace all parentheses `()`  with box brackets `[]`.

```shell script
tr '()' '[]'
```

### 'Tr' Command #2
> In a given fragment of text, delete all the lowercase characters `a-z`.

```shell script
tr -d 'a-z'
```

### 'Tr' Command #3
> In a given fragment of text, replace all sequences of multiple spaces with just one space.

```shell script
tr -s ' ' ' '
```

### Sort Command #1
_NOTE: `$'string'` expands to `string` as per ANSI C standard, e.g.
`\t` expands to horizontal tab._

> Given a text file, order the lines in lexicographical order.

```shell script
sort
```

### Sort Command #2
> Given a text file, order the lines in reverse lexicographical order 
> (i.e. `Z-A` instead of `A-Z`).

```shell script
sort -r
```

### Sort Command #3
> Sort the lines in ascending order
>
```shell script
sort -n
```

### Sort Command #4
> Sort the lines in descending order

```shell script
sort -nr
```

### Sort Command #5
> Rearrange the rows of the table in descending order of the 
> values for the average temperature in January.
_FLAGS: `-r` - reversed, `-n` - numeric `-k` column, `-t` - delimiter._ 
```shell script
sort -rn -k2 -t $'\t'
```

### 'Sort' command #6
> You need to sort this file in ascending order of the second column (i.e. 
> the average monthly temperature in January).
```shell script
sort -n -k2 -t $'\t'
```
