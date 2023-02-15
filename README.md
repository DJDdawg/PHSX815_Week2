# PHSX815 Spring 2021 Week 2

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
---

### Mr. Rogan's Cookie Hoax

A categorical distribution has been added to the **Random.py** file. It generates a roll of a 6-sided die. By including this class in our previous **rng.py** file. we can generate a text file that contains any amount of permutations of our Random algorithm. The textfile for this is named **dicerolls.txt** and is created by,
> $ python3 rng.py

By then running,
> $ python3 plot_rng.py

we can create a histogram of the rolls. These are discrete values, as can be seen in the **dicerolls.txt** file. The output graph is included in the folder as **Graph_plot_rng.py**.

![Graph_plot_rng.py](https://user-images.githubusercontent.com/76142511/215650195-cb703a08-aa43-435c-90ae-4fd4cd93a314.png)

*Note: The histogram is a little wonky, I am so sorry. I spend a long time trying to fix it and it only got worse.*

---

### Gambling with Dice

In this portion of the assignment, the great cookie mystery continues and it is up to us to graph probability distributions to help determine the culprit of the stolen cookies. Through use of familiar random number generators, we can use the **CookieTimer.py** file to generate a spread of times for a particular situation of cookie thievery. We do this by running the code in our terminal with,

> $ python3 CookieTimer.py

where we can also use the arguments `-Nexp ####`, `-Nmeas ####`, and `-seed ####` same as before. We can output this directly to a text file by adding,

> $ python3 CookieTimer.py > cookie_output.py

which can then be used as the input file for the aptly named analyizng script, **CookieAnalysis.py**. We run this by entering,

> $ python3 CookieAnalysis.py cookie_output.py

which will then sort the data, find the mean value, find quartile values, make a histogram, and add the quartiles to the plot as dashed lines. Pretty neat!

![fig3](https://user-images.githubusercontent.com/76142511/215650365-43616cbd-8a3f-4a4e-9089-f35f11698e10.png)

[^1] The code for the file is provided by [Dr. Chris Rogan (crogan) on github](https://github.com/crogan/PHSX815_Week2.git).

