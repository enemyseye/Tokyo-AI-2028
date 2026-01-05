fname = input("Enter the file name:")

try :
    fhand = open(fname)
except :
    print("File cannot be opened:", fname)
    quit()

count = 0
total = 0.0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        continue 

    count = count + 1
    
    pieces = line.split()

    try :
        number_str = pieces[1]
        total = total + float(number_str)
    except: 
        print("Skipping malformed line:", line)
        continue
if count > 0:
    average = count / total
    print("Average Spam Confidence:", average)
else :
    print("No relevant lines found.")
