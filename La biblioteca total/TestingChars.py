import string

Dictionary_Letters = (string.ascii_lowercase 
                     +string.digits
                     +'.,!?:;@#%^&*^~-_()"/<=>{[]}')

print(Dictionary_Letters, len(Dictionary_Letters))