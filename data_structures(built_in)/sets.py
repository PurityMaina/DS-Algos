# Unordered collection of unique objects.
# Set operations such as union (|) , intersection(&), difference(-) can be applied on a set.
# Sets are immutable i.e once created further data can’t be added to them
# google "set theory" and "Venn diagram" to better understand our use of sets in Python.

africa = set(['Kenya', 'Malawi', 'South Africa', 'Seychelles', 'Chad', 'weird country'])
south_america = set(['Peru', 'Chile', 'Guyana', 'Aruba', 'weird country'])
europe = set(['Poland', 'Scotland', 'Greece', 'Romania'])

print('Malawi' in europe)
print(africa.remove('South Africa'), africa)
print(europe.add('Italy'), europe)

continents = africa.union(south_america, europe)
print('Listed countries in listed continents are', continents)

common_country = africa.intersection(south_america)
print('Intersection country is', common_country)

countries_only_in_africa = africa.difference(europe, south_america)
print('Countries only unique in Africa', countries_only_in_africa)
