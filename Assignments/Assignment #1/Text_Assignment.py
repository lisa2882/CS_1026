
a. The customer’s name (a string)
b. The customer’s age (an integer)
c. The customer's classification code (a character).
d. The number of days the vehicle was rented (an integer).
e. The vehicle's odometer reading at the start of the rental period (an integer).
f. The vehicle's odometer reading at the end of the rental period (an integer).
It will then process that customer information and display the results.




2. The program will compute the amount of money that the customer will be billed, based on the
age of the customer, the customer's classification code, number of days in the rental period, and
number of kilometers driven.
3. The program will recognize both upper case and lower case letters for the classification codes; the
codes and related information are as follows:
a. Code 'B' (budget)
i. base charge: $20.00 for each day,
ii. kilometers driven charge: $0.30 for each kilometer driven.
b. Code 'D' (daily)
i. base charge: $50.00 for each day,
ii. kilometers driven charge: no charge if the average number of kilometers
driven per day is 100 kilometers or less; otherwise, $0.30 for each kilometer
driven above the 100 kilometer per day limit.
c. Code 'W' (weekly)
i. base charge: $200.00 for each week or fraction of a week (i.e., each fraction of
a week is treated as a week, for example 8 days is treated as 2 weeks),
ii. kilometers driven charge:
 There is no additional charge if the average number of kilometers driven
per week is 1000 kilometers or less;
 If the average number of kilometers driven per week exceeds 1000
kilometers but does not exceed 2000 kilometers, then there is an
additional $50.00 charge per week;
 If the average number of kilometers driven per week exceeds the 2000
kilometer per week limit, then there is an additional $100.00 charge per
week plus $0.30 for each kilometer driven over the 2000 kilometer per
week average.
Irrespective of the classification code, for all customers under 25 years old, an additional $10
for each day will be added to their total bill. The amount billed to the customer is the sum of
the base charge, any charges for the extra kilometers driven and the surcharge for young
drivers.""
4. The program will compute the number of kilometers driven by the customer during the rental
period.
5. For each customer, the program will display a summary with the following information:
a. The customer’s name,
b. The customer’s age,
c. The customer's classification code,
d. The number of days the vehicle was rented,
e. The vehicle's odometer reading at the start of the rental period,
f. The vehicle's odometer reading at the end of the rental period,
g. The number of kilometers driven during the rental period,
h. The amount of money billed to the customer for the rental period,
All output should be appropriately labeled and formatted. The amount of money billed should
be displayed with a dollar sign and will be rounded to two fractional digits (for example, $125.99
or $43.87).
6. The program should also detect and report invalid classification codes. When an invalid
classification code is detected, the program will display an error message as well as the invalid
code, customer’s name, and age. After displaying this information the program should end.