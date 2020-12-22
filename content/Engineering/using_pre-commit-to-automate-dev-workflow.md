Title: Using pre-commit to automate development workflow in your python projects
Date: 2020-12-22 14:00
Author: Jules Capacillo
Tags: python; tutorial; pre-commit; black; flake8;
Slug: automate-workflow-using-pre-commit
Lang: en
Summary: Using python's pre-commit package to configure your pre-commit hooks

Working remotely as a Software Engineer has taught me that in order for a feature to be delivered well, people should be able to code review your work properly focusing mostly on the logic you did rather than the small nitty-gritty things. Good thing we have packages such as [Black](https://github.com/psf/black), [Flake8](https://github.com/PyCQA/flake8) and optionally [Mypy](https://github.com/python/mypy) (if you want to include static typing)  to check for us, The only thing missing is automating the process.

One thing we can use are [Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks), specifically pre-commit hooks as I want to perform the automated checks before someone commits to the repository.  the only challenge was how to share this with your teammates, and here comes python’s [pre-commit](https://github.com/pre-commit/pre-commit) package.

Using pre-commit is relatively easy, below are the steps you can follow:

1.  Install it using pip: `pip install pre-commit` 
2. Create a `.pre-commig-config.yaml` file containing your desired hooks
3. Run `pre-commit install` to install your pre-commit hook in git


Here’s a sample `.pre-commig-config.yaml` that contains Black, Flake8, and MyPy.

![.pre-commig-config.yaml](/images/using-pre-commit/precommit.png)


You can add additional configurations in the yaml file pertaining to each of your hooks. In the example above we edited `max-line-length` since Black has a limit of 90 characters instead of 88.

To test here’s a sample file we named `test.py`.

![test.py](/images/using-pre-commit/testpy.png)

Now let’s try to add and commit this to our local repository by doing `git add` then `git commit`

![terminal results](/images/using-pre-commit/blackresults.png)

We can see that our hooks are working! Hope this helps and here’s a [repo](https://github.com/juleski/python_dev_setup)  of the setup so you can freely test.

As an added bonus you may want to check what hooks other open source projects use on their development pipeline. You can learn a lot! Here’s the one from [flask](https://github.com/pallets/flask/blob/master/.pre-commit-config.yaml).