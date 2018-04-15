def Print(Title, Description):
    Title = str(Title)
    Description = str(Description)
    print(" \v %s: \n" % (Title))
    print("\t+" + (len(Description) + 2) * '-' + "+")
    print("\t| " + Description + ' |')
    print("\t+" + (len(Description) + 2) * '-' + "+")
    print("\n")
