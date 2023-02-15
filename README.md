# PHSX815 Spring 2023 Week 2

Week 2 lecture and Homework involved Tossing Coins (Bernoulli and Binomial Distributions), Rolling Dice (Categorical and Multinomial Distributions), and the continued mystery of Mr. Rogan's missing cookie fiasco (Exponential and Erlang Distributions)!

Everything is in the Python folder, so go there!

### Tossing Coins

To simulate a coin toss, run the **CoinToss.py**. file with Python. In Linux, this means opening the PHSX815_Week2 folder in the terminal and simply running, 
> $ python3 CoinToss.py

Variables that you can mess around with include the probability of landing on heads, the seed, the number of tosses per experiment, and the number of experiment. 

To do this enter values after the appropiate argument: `-seed x.x`,`-seed xxxx`, `-Ntoss xxxx`, `-Nexp xxxx`. 

You can also choose to output to the program to a textfile with the following unix command: 
> $ python3 CoinToss.py -output cointoss1.txt

You can name the output file whatever you want, and can include any additional arguments mentioned above.

Note: With the same seed value, you will get the same string of numbers from the algorithm as your output, so make sure to change the seed number if you are wanting to see a variety of outcomes. 

The default probability for landing on heads is 0.5 (50%), but you can compare data according to different hypothesis (probabilities) using the **CoinAnalysis.py** program.

To do this, use the **cointossoutput.txt** file as an input file for the **CoinAnalysis.py** file with the following argument:
> $ python3 CoinAnalysis.py -cointossoutput.txt

This takes the output file from **CoinToss.py** and creates a graph from its contents. A picture of this graph is saved in the repo as **Coin Toss Graph.png**.

![Coin Toss Graph.png](https://github.com/DJDdawg/PHSX815_Week2/blob/master/python/Coin%20Toss%20Graph.png))

The above graph was created using two different input files, the first having a probaility of 30%, and the second having a probability of 60%. Each experiment had 100 coin flips, and 10 total experiments were ran. 

The code to run this looks like the following:

>$ python3 CoinToss.py -prob 0.6 -Ntoss 100 -Nexp 10 -output cointoss1.txt
>
>$ python3 CoinToss.py -prob 0.3 -Ntoss 100 -Nexp 10 -output cointoss2.txt
>
>$ python3 CoinAnalysis.py -prob0 0.6 -input0 cointoss1.txt -prob1 0.3 -input1 cointoss2.txt

The clear distinction between the two distributions is because of the stark contrast in the two hypothesises. 
---

### Mr. Rogan's Cookie Hoax

An example that has tortured students since Day 1 of class has now been fully analyzed. 

Each culprit has their own, constant rate parameter corresponding to how many cookies per day that they eat. Our job is to catch the culprit. 

We can simulate data taken from a single culprit with the **CookieTimer.py** program. It can be run in the terminal with, 
> $ python3 CookieTimer.py

, where we can also use the arguments `-seed xxxx`, `-Nexp xxxx`, `-Nmeas xxxx`, and `-rate xxxx`, the same as before. 

Again, this can be outputted to a textfile using the following:

> $ python3 CookieTimer.py -Nmeas 1000 -Nexp 10 > cookieoutput.txt

This can then be used as the input file for the aptly named analyizng script, **CookieAnalysis.py**, which I painstakingly debugged for the case of Nexp > 1, with the help of my friend Neema. He helped explain the code for plotting the histograms, mean, and quartiles. 

**CookieAnalysis.py** can be run with,

> $ python3 CookieAnalysis.py cookie_output.py

which will then sort the data, find the mean value, find quartile values, make a histogram, and add the quartiles to the plot as dashed lines.

Again, a picture of this graph is saved in the repo as **Coin Toss Graph.png**.

![Cookie Analysis Graph](https://github.com/DJDdawg/PHSX815_Week2/blob/master/python/Cookie%20Analysis%20Graph.png))


### Gambling with Dice

A categorical distribution has been added to the **Random.py** file. This simulates a a roll of a 6-sided die, which is often used in the fabled college game "Beer Die", or the more family friendly "Yahtzee!".

Then, the **DiceRoll.py** program was created to simulate rolling that dice multiple time. Similar to **CookieTimer.py**, you have some arguments to mess around with. They are, `-seed xxxx`, `-Nroll xxxx`, `-Nexp xxxx`, `-p1 x.x`, `-p2 x.x`, `-p3 x.x`, `-p4 x.x`, `-p5 x.x`. Nroll is the number of times that the dice is rolled in a single experiment, and each pi is the probability of rolling a certain side of the die. By default, each pi is 1/6, just like a normal die. Be careful that the sum of p1 through p6 is 1 if you decide to weight your die!

Here is an example of runnning this code with a weighted dice.
>$ python3 DiceRoll.py -Nroll 50 -Nexp 5 -p1 0.3 -p2 0.1 -p3 0.1 -p4 0.2 -p5 0.1 -output Dicerolls1.txt

This sends the output of this program to a text file named **Dicerolls1.txt**

Just like previously, we then use this input file and feed it into our analysis program **DiceHist.py**, which counts the outcome of each dice roll, and produces a histogram of the results. 

> $ python3 Dicehist.py Dicerolls1.txt
> 
> The graph is included in the folder as **Dice Roll Graph.png**.

![Dice Roll Graph]([(https://github.com/DJDdawg/PHSX815_Week2/blob/master/python/Dice%20Roll%20Graph.png))
---
