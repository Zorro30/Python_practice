def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates= jars/100
    return jelly_beans,jars,crates

Start_point= 10000

secret_formula(Start_point)

print ("We'd have {} beans, {} jars, and {} crates.".format(*secret_formula(Start_point)))