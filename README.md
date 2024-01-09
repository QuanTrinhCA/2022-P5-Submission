# [Problem E: Be A Bee](https://nbhspc22.kattis.com/contests/nbhspc22/problems/nbhspc22.beabee)

It has been known for some time that honeybees can perform a “waggle dance” to tell other bees in their hive about how to get to a good patch of flowers. A biologist has recorded the key characteristics of several waggle dances, and now we want to find the patches of flowers to which the bee was sending its hive-mates.

The waggle dance specifies the distance and direction from the hive that the other bees would need to go. It is performed on a vertical surface, such as the side wall of the hive. If the bee “waggles” while climbing straight up, the flowers are in the direction of the sun (the bee should go directly away from its shadow). If it waggles while climbing straight down, the flowers are in the opposite direction from the sun (the bee should head directly toward its shadow). In general, if the flowers are at an angle of a from the sun, the bee will waggle while travelling at an angle of a from vertical. For distance, x seconds of waggling means a distance of about x km.

Our biologist has made a number of records of waggle dances observed in the hive. Some observations were made at 8 am, with others at 3 pm. The data recorded were the time the observation was made, the duration of the waggle, and the overall angle a (in degrees from straight up) that the bee was going while waggling.

The biologist wants to go to the flowers too. Turn each observation into directions for the biologist, who plans to start at the hive, step toward the east or west some number of times, then step toward the north or south some number of times. With each step, the biologist covers 1 m.

To complete this task, you need to know where the sun is, at various times of day. At 8 am, the sun is at 90 degrees, whereas it is at 220.8 degrees at 3 pm. Note that 0 degrees is north, 90 degrees is east, and so forth.

## Input
There is one line, containing one observation. Its first item contains either 8 (representing 8 am), or 15 (representing 3 pm). This is the time when the observation was made. The second item is a positive integer between 0 and 359, inclusive. It is the angle (from vertical, given in degrees) that the bee was travelling while waggling. The third item is a positive number (with one digit after the decimal point) between 0.1 and 2.0, representing the number of seconds that the bee was waggling. A single space separates each item.

## Output
The output consists of one line telling the direction in the east or west direction and how many steps to take, then telling the direction in the north or south direction and how many steps to take. Directions are North, South, East and West with capitals. The number of steps should be rounded to the closest integer, and a single space should separate each word or number from the next word or number. Although 0 steps North and 0 steps South are theoretically equivalent to each other, for this problem 0 South is not allowed. Similarly, 0 West is not allowed.

## Sample Input 1
```
8 0 0.5
```

## Sample Output 1
```
East 500 North 0
```

## Sample Input 2
```
8 180 0.1
```

## Sample Output 2
```
West 100 North 0
```

## Sample Input 3
```
15 1 0.5
```

## Sample Output 3
```
West 333 South 373
```
