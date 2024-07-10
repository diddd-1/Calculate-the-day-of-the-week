Using Python to write a program that reads in a date in the form year, month and day
(three integers) and prints what day of the week it is.

The day of the week calculation must be done with a formula called Zeller's congruence, see below.



- that the year is in the range 1583 – 9999
- that the month is in the interval 1-12
- that the day number within the month matches the month number, i.e. that if month is 1, 3, 5, 7, 8, 10 or 12 then day number is in the range 1-31,
  if the month is 4, 6, 9, or 11 then the day number is in the range 1-30 and if the month is 2 then day number in the range 1-28 or 1-29 depending on whether it is a leap year or not.
- It is a leap year if the year is evenly divisible by 400, or if it is evenly divisible by 4 but not evenly divisible by 100.
