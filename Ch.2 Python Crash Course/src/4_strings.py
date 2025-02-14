#4a) Defining strings w/ either "" or '' (must match)
single_quoted_string = 'data science'
double_quoted_string = "data science"


#4b) backslashes for special characters
tab_string = "\t"                               # represents the tab character
len(tab_string)                                 # == 1


#4c) "Raw strings" == strings prefixed with 'r' that treat backslashes as literal characters
not_tab_string = r"\t"                          # represents the characters '\' and 't'
len(not_tab_string)                             # == 2


#4d) Multiline strings use triple double-quotes
multi_line_string = """This is the first line.
                        and this is the second line
                        and this is the third line"""


#4e) "F-String" == a way to substitute values into strings // using a first and last name seperately
first_name = "Joel"
last_name = "Grus"

            # Combining the two into a full name
full_name1 = first_name + " " + last_name                   # String addition
full_name2 = "{0} {1}".format(first_name, last_name)        # String.format

            # A raw, regular old f-string
full_name3 = f"{first_name} {last_name}"                # f-string  that we will prefer