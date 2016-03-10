# Get REF list from "ngsl.txt". (single token per line, alphabetical)

# Get SOURCE list from "everyman-families.txt". (tab-delimited, multi-token list with a headword and its lemmas on each line, alphabetical)

# Get BOOK text from "everyman-full.txt". (raw novel text)



# Compare the first item in each line of SOURCE with REF.
# - If not in REF, add it (and all other words in that line in SOURCE) to VOCAB list.
# - If in REF, ignore.



# Attempt to find each word in BOOK text in VOCAB list.
# - If found, add <b></b> tags around the word in BOOK text.
# - If not found, ignore.



# Save new BOOK text as an HTML document.

# Save VOCAB list as a TXT document.
