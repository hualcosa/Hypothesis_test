# -*- coding: utf-8 -*-

'''
Let’s start by including a data interface called fetchmaker
that will give you access to FetchMaker’s dog data.
Make all other necessary imports here
'''
import fetchmaker
import numpy as np
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

'''
The attributes that FetchMaker keeps track of are:

weight, an integer representing how heavy a dog is in pounds
tail_length, a float representing tail length in inches
age, in years
color, a String such as "brown" or "grey"
is_rescue, a boolean 0 or 1
The fetchmaker package lets you access this data for a specific breed 
of dog with the following format:
   fetchmaker.get_weight("poodle")
This returns a Pandas DataFrame of the weights of the poodles recorded
in the system. The other methods are get_tail_length, get_color, get_age, 
and get_is_rescue, which all take a breed as an input.
Get the tail lengths of all of the "rottweiler"s in the system, and store
 it in a variable called rottweiler_tl.
'''
rottweiler_tl = fetchmaker.get_tail_length("rottweiler")

'''
Print out the mean of rottweiler_tl and the standard deviation of
rottweiler_tl
'''
print(np.mean(rottweiler_tl))
print(np.std(rottweiler_tl))

'''
Over the years, we have seen that we expect 8% of dogs in the FetchMaker
system to be rescues. We want to know if whippets are significantly more
or less likely to be a rescue.
Store the is_rescue values for "whippet"s in a variable called whippet_rescue.
'''
whippet_rescue = fetchmaker.get_is_rescue('whippet')

'''
Get the number of entries in whippet_rescue that are 1
'''
num_whippet_rescues = np.count_nonzero(whippet_rescue)

'''
Get the number of samples in the whippet set by taking the np.size of 
whippet_rescue. Store this in a variable called num_whippets.
'''
num_whippets = np.size(whippet_rescue)

'''
Use a binomial test to test the number of whippet rescues,
num_whippet_rescues, against our expected percentage, 8%.
'''
binomial_test_pvalue = binom_test(num_whippet_rescues, num_whippets, .08)

'''
Print out the p-value. Is your result significant?
Answer: No!!!
'''
print(binomial_test_pvalue)

'''
Three of our most popular mid-sized dog breeds are whippets, terriers,
and pitbulls. Is there a significant difference in the average weights
of these three dog breeds? Perform a comparative numerical test to determine
if there is a significant difference.
'''
whippets_weight = fetchmaker.get_weight('whippet')
terriers_weight = fetchmaker.get_weight('terrier')
pitbulls_weight = fetchmaker.get_weight('pitbull')

anova_results = f_oneway(whippets_weight, terriers_weight, pitbulls_weight)
anova_pvalue = anova_results[1]
print(anova_pvalue)

'''
Now, perform another test to determine which of the pairs of these dog breeds
differ from each other.
'''
values = np.concatenate([whippets_weight, terriers_weight, pitbulls_weight])
labels = ['whippet'] * len(whippets_weight) + ['terrier'] * len(terriers_weight) + ['pitbull']* len(pitbulls_weight)

tukey_result = pairwise_tukeyhsd(values, labels, .05)
print(tukey_result)

'''
We want to see if "poodle"s and "shihtzu"s have significantly different color breakdowns.
Get the poodle colors and store it in a variable called poodle_colors.
Get the shih tzu colors and store it in a variable called shihtzu_colors.
'''
poodle_colors = fetchmaker.get_color('poodle')
shitzu_colors = fetchmaker.get_color('shihtzu')

'''
You can get the number of occurrences of brown poodles by using
np.count_nonzero(poodle_colors == "brown").
Use this function to build a Chi Square contingency table, called color_table
'''
colors = ['black', 'brown', 'gold', 'grey', 'white']

contingency_table = np.array([[0, 0],
                              [0, 0],
                              [0, 0],
                              [0, 0],
                              [0, 0]])
for i in range(5):
    color = colors[i]
    contingency_table[i,0] = np.count_nonzero(poodle_colors == color)
    contingency_table[i,1] = np.count_nonzero(shitzu_colors == color)

'''
Feed your color_table into SciPy’s Chi Square test, save the p-value and print it out.
'''
_, chi2_pvalue, _, _ = chi2_contingency(contingency_table)
print(chi2_pvalue)