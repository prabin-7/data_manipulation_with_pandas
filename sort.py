# Sort homelessness by individuals
import pandas as pd
homelessness = pd.read_csv('homelessness.csv', index_col= 0)
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())

# exercise 3
# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(['region','family_members'],ascending = [True,False])

# Print the top few rows
print(homelessness_reg_fam.head())

# ex4
# Select the state and family_members columns
state_fam = homelessness[['state','family_members']]
#needs compulsory double sq.brackets to select multiple columns and it results in df
print(state_fam.head())


# exercise5:
# Filter for rows where family_members is less than 1000 
# and region is Pacific
filter_1 = homelessness['family_members']<1000
filter_2 = homelessness['region'] == 'Pacific'
fam_lt_1k_pac = homelessness[filter_1&filter_2] 

# See the result
print(fam_lt_1k_pac)

#exercise 6:

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)