# dblpct

The % in the string given as the first argument is doubled and output to stdout.  
It's my hobby CLI tool.  

## install

```
# pip install dblpct
```


## how to use

ex1)
```
# dblpct http://example.com/%E3%83%86%E3%82%B9%E3%83%88URL
http://example.com/%%E3%%83%%86%%E3%%82%%B9%%E3%%83%%88URL
```

ex2)
```
# dblpct -r http://example.com/%%E3%%83%%86%%E3%%82%%B9%%E3%%83%%88URL
http://example.com/%E3%83%86%E3%82%B9%E3%83%88URL
```

`-r`  means `Reverse operation` of this tool.

ex3)
```
 # dblpct -r $(dblpct %%)
%%

 # dblpct $(dblpct -r %%)
%%

 # dblpct $(dblpct %%)
%%%%%%%%
```

## Caution

Special characters in bash, etc. are not escaped.  
They will be interpreted as a command line string when entered.  

ex1)
```
 # dblpct FJWRF%)faw
-bash: syntax error near unexpected token `)'
```

If you want to enter special characters,  
enclose them in quotes or escape them appropriately.  

ex2)
```
 # dblpct 'fahj4(jfawe&%%fawle$kf'
fahj4(jfawe&%%%%fawle$kf
```
