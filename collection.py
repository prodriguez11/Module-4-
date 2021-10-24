# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {                                                     #fixed miss spelling
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"                             #added  bracket
}
for author, date in authors.items():                             #added coman and replace brackets with parantheses
    print("%s" % author + " died in " + "%s." % date)            #put in parantheses
