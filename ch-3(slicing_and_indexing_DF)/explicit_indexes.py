# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures['date'] >= '2010') & (temperatures['date'] <= '2011')]
#here in above line need to use full date for the comparision as '2010'>=temperatures['date'] only compares to 2010-01-01.
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index('date').sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010':'2011'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['2010-08': '2011-02'])

#exercise -4:
# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[23,1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5,:])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5,3:5]) #this is also temperatures.iloc[:5,2:4]