# HackeRank - Linux Shell
Solutions to [**HackerRank Linux Shell**](https://www.hackerrank.com/domains/shell)

Useful Sources:
- [A quick guide to writing scripts using the bash shell](http://www.panix.com/~elflord/unix/bash-tute.html)

## Let's Echo
> Write a bash script which does just one thing: saying "HELLO".

```shell script
echo 'HELLO'
```

## A Personalized Echo
> Write a Bash script which accepts `name` as input and displays a greeting:
> "Welcome (name)" 

```shell script
read name
echo "Welcome $name"
```

_Note that, unlike double quotes `"`, single quotes `'` will not perform 
string interpolation (variable substitution)._

## Looping and Skipping
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

## Looping with numbers
> Use `for` loops to display the natural numbers from `1` to `50`.

```shell script
for i in {1..50}
do
    echo $i
done
```

## The World of Numbers
> Given two integers, `X` and `Y`, find their sum, difference, product, and quotient.
```shell script
read X
read Y
echo $((X + Y))
echo $((X - Y))
echo $((X * Y))
echo $((X / Y))
```

## Comparing Numbers
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

## Getting started with conditionals
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

## More on Conditionals
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

## Cut #1
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
