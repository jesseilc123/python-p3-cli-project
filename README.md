## Generating Your CLI

A CLI is, simply put, an interactive script. You can run it with `python cli.py`
or include the shebang and make it executable with `chmod +x`. It will ask for
input, do some work, and accomplish some sort of task by the end.

Past that, CLIs can be whatever you'd like. An inventory navigator? A checkout
station for a restaurant? A choose-your-adventure video game? Absolutely!

Here's what all of these things have in common (if done well): a number of
`import` statements (usually _a lot_ of import statements), an `if __name__ ==
"__main__"` block, and a number of function calls inside of that block. These
functions should be kept in other modules (ideally not _just_ `helpers.py`)

There will likely be some `print()` statements in your CLI script to let the
user know what's going on, but most of these can be placed in functions in
other modules that are grouped with others that carry out similar tasks. You'll
see some variable definitions, object initializations, and control flow
operators (especially `if/else` blocks and `while` loops) as well. When your
project is done, your `cli.py` file might look like this:

```py
from helpers import (
    function_1, function_2,
    function_3, function_4,
    function_5, function_6,
    function_7, function_8,
    function_9, function_10
)

if __name__ == '__main__':
    print('Welcome to my CLI!')
    function_1()
    x = 0
    while not x:
        x = function_2(x)
    if x < 0:
        y = function_3(x)
    else:
        y = function_4(x)
    z = function_5(y)
    z = function_6(z)
    z = function_7(z)
    z = function_8(z)
    function_9(z)
    function_10(x, y, z)
    print('Thanks for using my CLI')

```

***

## Updating Your README.md

`README.md` is a Markdown file that describes your project. These files can be
used in many different ways- you may have noticed that we use them to generate
entire Canvas lessons- but they're most commonly used as homepages for online
Git repositories. **When you develop something that you want other people to
use, you need to have a README.**

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this lesson's resources for a basic guide to Markdown.

### What Goes into a README?

This README should serve as a template for your own- go through the important
files in your project and describe what they do. Each file that you edit
(you can ignore your Alembic files) should get at least a paragraph. Each
function should get a small blurb.

You should descibe your actual CLI script first, and with a good level of
detail. The rest should be ordered by importance to the user. (Probably
functions next, then models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

***

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you
off to a good start with your Phase 3 Project.

Happy coding!

***

## Resources

- [Setting up a respository - Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
