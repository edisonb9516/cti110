"""
This program is going to create a prediction of sales in the company
9-11-2019
CTI-110 P2T1 - Sales Prediction
Brandon Edison
"""

#Get the projected total sales

total_sales = float(input('Enter the projected sales: '))

#calculate the profit as 23 percent of total sales

profit = total_sales * 0.23

#Display the profit

print('The profit is $', format(profit, ',.2f'))
