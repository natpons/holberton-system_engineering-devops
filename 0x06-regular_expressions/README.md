# 0x06. Regular expression

Foundations - System engineering & DevOps  Scripting

_By Sylvain Kalache, co-founder at Holberton School_

_For this project, students are expected to look at this concept:_

-   _[Regular Expression](https://intranet.hbtn.io/concepts/29)_

## Background Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the  `//`:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a

```

## Resources

**Read or watch**:

-   [Regular expressions - basics](https://intranet.hbtn.io/rltoken/SJ2eQ7V2iQlCgLc-L96zWg "Regular expressions - basics")
-   [Regular expressions - advanced](https://intranet.hbtn.io/rltoken/qyjWL-J1_qUaZGR690gH1Q "Regular expressions - advanced")
-   [Rubular is your best friend](https://intranet.hbtn.io/rltoken/WCjn8NgohbQ5NGXEObWZvQ "Rubular is your best friend")
-   [Use a regular expression against a problem: now you have 2 problems](https://intranet.hbtn.io/rltoken/Zfvv_ydOCvJ_YaBB6eDqVw "Use a regular expression against a problem: now you have 2 problems")
-   [Learn Regular Expressions with simple, interactive exercises](https://intranet.hbtn.io/rltoken/Y-OVGcJ5cskdXWIBowiE_A "Learn Regular Expressions with simple, interactive exercises")

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Ubuntu 14.04 LTS
-   All your files should end with a new line
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   The first line of all your Bash scripts should be exactly  `#!/usr/bin/env ruby`
-   All your regex must be built for the Oniguruma library

-   [](https://students-support.hbtn.io/hc)
    
      
    

----------

----------

# Regular Expression

System engineering & DevOps

----------

A regular expression, commonly called a regexp, is a sequence of characters that define a search pattern. It is mainly for use in pattern matching with strings, or string matching (i.e. it operates like a find and replace command). While it is a very powerful tool, it is also very dangerous because of its complexity.

![](https://intranet.hbtn.io/images/contents/sysadmin/concepts/29/regex_now_2_problems.jpg)

**_[Some people, when confronted with a problem, think](https://intranet.hbtn.io/rltoken/jFwEEnGk2BPx0eJpQ2MurA "Some people, when confronted with a problem, think")_  _[I know, Ill use regular expressions. Now they have two problems.](https://intranet.hbtn.io/rltoken/jFwEEnGk2BPx0eJpQ2MurA "I know, I'll use regular expressions.   Now they have two problems.")_**  (super classic joke in the industry)

One thing you have to be careful with is that different languages use different regexp engines. That means that a regexp in Python, for example, will be interpreted differently in Javascript:

Regular expressions are everywhere and software engineers, no matter their positions, will have to use them during their careers. System administrators and DevOps are the ones using them the most because they are very handy for log parsing.

Read about regexp:

-   [http://www.regular-expressions.info/](https://intranet.hbtn.io/rltoken/UiNlZh3kfbxisotXH-gI0A "http://www.regular-expressions.info/")
-   [http://www.w3schools.com/jsref/jsref_obj_regexp.asp](https://intranet.hbtn.io/rltoken/tcX5DBSbWv1emQQQIzuchw "http://www.w3schools.com/jsref/jsref_obj_regexp.asp")  Play with regexp (or compose them):
    
-   Ruby:  [http://rubular.com/](https://intranet.hbtn.io/rltoken/M4whgZsxtYEk50WGcYbPRA "http://rubular.com/")
    
-   PHP/Javascript/Python:  [https://regex101.com/](https://intranet.hbtn.io/rltoken/InqFxs9vWK2lTXxeCVHM8Q "https://regex101.com/")
