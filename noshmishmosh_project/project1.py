#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
The Nosh Mish Mosh is a recipe and ingredient meal delivery service. We ship
 he raw materials and you get to cook it at your home! We’ve decided to hire a
data analyst to help them make product and interface decisions. Get started
and we’ll be able to judge the amount of data we’ll need for these differences
to be meaningful.
'''
'''
We’ve collected customer data for the past week and exposed it through a Python
library, so first import noshmishmosh.
'''
import noshmishmosh


'''
Next, we’ll need to do a little bit of data analysis — let’s use numpy to help
'''
import numpy as np

'''
Nosh Mish Mosh wants to run an experiment to see if we can convince more people
to purchase meal plans if we use a more artisanal-looking vegetable selection.
We’ve photographed these modern meals with blush tomatoes and graffit
i eggplants, but aren’t sure if this strategy will sell enough units to
benefit from establishing a business relationship with a new provider.
'''

'''
Let’s get the ball rolling on finding those numbers! In order to get our
 baseline, we need to first know how many users visited the site. 
'''
all_visitors = noshmishmosh.customer_visits

'''
Next we need to know how many visitors to the site ultimately end up buying
a meal or set of meals from Nosh Mish Mosh. 
'''
paying_visitors = noshmishmosh.purchasing_customers

'''
Calculate the lengths of the two lists
'''
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

'''
Now to get the baseline
'''
baseline_percent = paying_visitor_count/total_visitor_count * 100
#print(baseline_percent)

'''
These rainbow fingerling potatoes don’t come cheap. We’d like to know for sure
that we’ll be pulling in at least $1240 more every week. In order to figure out
how many more customers we need we’ll have to investigate the average revenue
generated from a given sale. Luckily we have a list of the money spent by each
customer in noshmishmosh.money_spent. Save that list into a variable called
payment_history.
'''
payment_history = noshmishmosh.money_spent

'''
We need to find how many typical purchases it would take to reach $1240 in
additional revenue using our historical data.
'''
average_payment = np.mean(payment_history)

'''
We want to know how many of these “usual” payments it would take to clear our
$1240 mark
'''
new_customers_needed = np.ceil(1240/average_payment)

'''
Now find the percent lift required by multiplying the number of customers by
100.0 and dividing the result by the total visitor count ascertained earlier
'''
percentage_point_increase = 100 * new_customers_needed / total_visitor_count

'''
In order to find our minimum detectable effect, we need to express 
percentage_point_increase as a percent of baseline_percent
'''
minimum_detectable_effect = 100 *  percentage_point_increase / baseline_percent
#print(minimum_detectable_effect)


'''
The last thing we need to calculate the sample size for Nosh Mish Mosh’s
artisanal rebranding is our statistical significance. We’d like to be fairly
certain, but this isn’t going to be a million dollar decision, so let’s
go with 90%.
'''

'''
Now put it all together! Puch the baseline, the minimum detectable effect,
and the statistical significance into the calculator and evaluate how many
people need to be shown the new assets before we can check if the results
are a significant improvement. Save the results in a variable called 
ab_sample_size.
'''
ab_sample_size = 90












