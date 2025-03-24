# Add total col as sum of individuals and family_members
import pandas as pd
homelessness = pd.read_csv('homelessness.csv',index_col = 0)

homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Add p_homeless col as proportion of total homeless population to the state population
homelessness['p_homeless'] = homelessness['total']/homelessness['state_pop']

# See the result
print(homelessness)