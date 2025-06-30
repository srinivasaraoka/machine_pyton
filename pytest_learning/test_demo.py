import re

def findNumbers(nums):
        even=0
        odd=0
        for x in nums:
            
            count=0
            while x>0:
                
                count=count+1
                print(" ",count)
                x=x//10
            if count%2==0:
                even=even+1
        return even 
#print(findNumbers([1,23,456,4444])  )      

str1= """
DB10-Indoor-ExtGPS                ecf4.0cce.12e0  3       Enabled        Up            160      2/8 (12 dBm)    (5,1,9,13,17,21,25,29)              Local   
DB10-Outdoor-IntGPS               ecf4.0cce.1480  3       Enabled        Down          160      ~8/8 (-3 dBm)   (21,17,25,29,1,5,9,13)              Local         """
ap_model = "DB10-Indoor-ExtGPS"
pattern1 = re.search(r'Up\s*\d*', str1)
# Regex pattern to find the required bracketed numbers for the given AP model
pattern = rf"{ap_model}.*?(\(\d+(?:,\d+)*\))"

# Search for the pattern in the string
match = re.search(pattern, str1)
if match:
    extracted_string = match.group(1)
    print(extracted_string)
print(pattern1)