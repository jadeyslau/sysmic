# starter code for Chapter 6: End of Chapter Questions Q2

canonical = [
    'Wnt', 'LPR5/6', 'Frizzled',
    'Dsh', 'APC', 'Axin', 'GSK3',
    'CK1', 'Beta-Cathenin'
]

noncanonical = [
    'Wnt', 'Frizzled', 'Dsh',
    'DAAM1', 'Profilin', 'Rho',
    'ROCK'
]

#Convert array to set
canonical = set(canonical)
noncanonical = set(noncanonical)

#Find common elements
common = canonical.intersection(noncanonical)
print('Common: ', common)

#Find unique elements
unique = canonical.symmetric_difference(noncanonical)
print('Unique: ', unique)

#Is APC in one of the sets
print('APC' in canonical or noncanonical)

combined = frozenset(common.union(unique))
print('Immutable updated set: ',combined)
