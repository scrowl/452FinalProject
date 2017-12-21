# final_spcrowl2_2CR

# Create lists for sorted item descriptions
alist = []
btobplist = []
brlist = []
bslist = []
btlist = []
bvlist = []
bxlist = []
ctozlist = []

# Create the file that will be our output, we use utf-8 encoding for non-Roman characters
fileout = open('newacquisitions.txt', 'w', encoding="utf-8")

def main():

# Import the CSV module and read in our example file, we use utf-8 encoding for non-Roman characters
    import csv
    infile = open('newBooks.csv', encoding="utf-8")
    csv_infile = csv.reader(infile)

# This will be our list of lists (rows in our csv file)
    listofitems = []

# Make our list of lists
    for row in csv_infile:
        listofitems.append(row)

# Cut off the titles of the columns (the first row)
    listofitems = listofitems[1:]

# Clean up the titles of the books: some end in " /" and some end in "."
    for row in listofitems:
        title = row[5]
        if len(title) != 0:
            if title[-1] == "/":
                title = title[:-2]
                row[5] = title
            if title[-1] == ".":
                title = title[:-1]
                row[5] = title

# Divert the items by call number, they are imported in call number order,
# so it's important to ensure that the items B-BP are sorted into the correct
# category. We make sure the BRs, BSs, BTs, BVs, and BXs get filtered out first,
# then default all the rest of the call numbers starting with B into their
# correct category.
    for row in listofitems:
        callnumber = row[4]
        if callnumber.startswith("A"):
            A(row)
        elif callnumber.startswith("BR"):
            BR(row)
        elif callnumber.startswith("BS"):
            BS(row)
        elif callnumber.startswith("BT"):
            BT(row)
        elif callnumber.startswith("BV"):
            BV(row)
        elif callnumber.startswith("BX"):
            BX(row)
        elif callnumber.startswith("B"):
            BtoBP(row)
        else:
            CtoZ(row)

# The overall heading of our text file
    print("### New Acquisitions This Month", file=fileout)
    print("---", file=fileout)

# Here we insert the sections one at a time from their lists
    # New As
    if len(alist) != 0:
        print("#### New As:", file=fileout)
        for item in alist:
            print(item, file=fileout)

    # New B to BPs
    if len(btobplist) != 0:
        print("#### New B - BPs:", file=fileout)
        for item in btobplist:
            print(item, file=fileout)

    # New BRs
    if len(brlist) != 0:
        print("#### New BRs:", file=fileout)
        for item in brlist:
            print(item, file=fileout)

    # New BSs
    if len(bslist) != 0:
        print("#### New BSs:", file=fileout)
        for item in bslist:
            print(item, file=fileout)

    # New BTs
    if len(btlist) != 0:
        print("#### New BTs:", file=fileout)
        for item in btlist:
            print(item, file=fileout)

    # New BVs
    if len(bvlist) != 0:
        print("#### New BVs:", file=fileout)
        for item in bvlist:
            print(item, file=fileout)

    # New BXs
    if len(bxlist) != 0:
        print("#### New BXs:", file=fileout)
        for item in bxlist:
            print(item, file=fileout)

    # New C to Zs
    if len(ctozlist) != 0:
        print("#### New C - Zs:", file=fileout)
        for item in ctozlist:
            print(item, file=fileout)

    # Close our file, we're done!
    fileout.close()

# These methods are for formatting: if the item has no title, we won't include
# it at all (it's too confusing for readers). If the item has no author, we
# won't include an author line. Then we add the call number and add this
# whole set to the appropriate list.
def A(item):
    if len(item[5]) != 0:
        itemdesc = "##### " + item[5] + "\n"
        if len(item[6]) != 0:
            itemdesc += "**By " + item[6] + "**\n"
        itemdesc += "**Call Number**: " + item[4]
        alist.append(itemdesc)

def BtoBP(item):
    if len(item[5]) != 0:
        itemdesc = "##### " + item[5] + "\n"
        if len(item[6]) != 0:
            itemdesc += "**By " + item[6] + "**\n"
        itemdesc += "**Call Number**: " + item[4]
        btobplist.append(itemdesc)

def BR(item):
    if len(item[5]) != 0:
        itemdesc = "##### " + item[5] + "\n"
        if len(item[6]) != 0:
            itemdesc += "**By " + item[6] + "**\n"
        itemdesc += "**Call Number**: " + item[4]
        brlist.append(itemdesc)

def BS(item):
    if len(item[5]) != 0:
        itemdesc = "##### " + item[5] + "\n"
        if len(item[6]) != 0:
            itemdesc += "**By " + item[6] + "**\n"
        itemdesc += "**Call Number**: " + item[4]
        bslist.append(itemdesc)

def BT(item):
    if len(item[5]) != 0:
        itemdesc = "##### " + item[5] + "\n"
        if len(item[6]) != 0:
            itemdesc += "**By " + item[6] + "**\n"
        itemdesc += "**Call Number**: " + item[4]
        btlist.append(itemdesc)

def BV(item):
    if len(item[5]) != 0:
        itemdesc = "##### " + item[5] + "\n"
        if len(item[6]) != 0:
            itemdesc += "**By " + item[6] + "**\n"
        itemdesc += "**Call Number**: " + item[4]
        bvlist.append(itemdesc)

def BX(item):
    if len(item[5]) != 0:
        itemdesc = "##### " + item[5] + "\n"
        if len(item[6]) != 0:
            itemdesc += "**By " + item[6] + "**\n"
        itemdesc += "**Call Number**: " + item[4]
        bxlist.append(itemdesc)

def CtoZ(item):
    if len(item[5]) != 0:
        itemdesc = "##### " + item[5] + "\n"
        if len(item[6]) != 0:
            itemdesc += "**By " + item[6] + "**\n"
        itemdesc += "**Call Number**: " + item[4]
        ctozlist.append(itemdesc)


main()
