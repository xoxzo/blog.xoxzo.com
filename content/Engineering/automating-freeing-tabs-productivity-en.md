Title: Automate Browsing to Free Up Browser Tabs, Save Time and be Productive
Date: 2018-12-21 20:00
Slug: automate-browsing-free-tabs-save-time-be-productive-en
Lang: en
Tags: python; automation; lifehack; requests; beautifulsoup; xoxzo.cloudpy;
Author: Josef Monje
Summary: We spend a lot of time in our browser. Sometimes we dedicate a few browser tabs for some simple activity like monitoring a page for changes. But these seemingly small activities eventually end up occupying a lot of our browser's tabs, and in turn distracts us from doing more important things and maintaining our productivity. In this post, I'll walk through the process of creating a simple script to watch a Kickstarter project for deals. This is aimed at beginners or non-programmers.

## Tab Overload Problems

We spend a lot of time in our browser. Sometimes we dedicate a few browser tabs to do some simple repetitive activity like monitoring a certain page for changes. Eventually, we end of with a lot of open tabs, from some forgotten purpose. Maintaining a lot of tabs can sometimes even prevent us from quitting our browser application just because there's something "important" about those tabs. I admit, this used to happen to me.

Browsers take up a lot of precious computing resources. The more tabs we keep, the less our computer can perform for other tasks. The problem eventually accumulates and we end up with a slow computer, preventing or slowing us down from accomplishing more important things and maintaining our productivity. Who wants a slow browser or computer? I sure wouldn't want to have to take care of my browser and its tabs like a pet or a plant, and grow many open tabs.

## A Better Way

> _"There must be a better way!"_

-- Raymond Hettinger, Python core developer

As Raymond Hettinger, one of my favorite Python developers, would say "There must be a better way!". We can keep those distracting tabs and slow browsers from slowing us down. For this example, I chose to write a script to watch a Kickstarter project so I can get better deals just in case they become available. Beginners or non-programmers can use this as a simple #lifehack or as a starting point and apply it to their own use cases like waiting for that new anime or manga episode.

Personally, when I see some cool [Kickstarter](https://www.kickstarter.com/) project, I'm usually not lucky or fast enough to get the limited early bird deals. In this post, I'll walk through the process of creating a simple script to watch out for early bird slots in case they become available. This can happen when a supporter suddenly changes their mind or changes their pledge. In which case, we would suddenly see something like `Limited (1 left of 10)` in the page and it probably wouldn't last very long before someone takes it. It would be a total waste of time to keep an open tab and keep refreshing it every once in a while to do this task.

We're going to work on a command-line script written in Python. Let's begin!

## Writing Our Python Script

First, let's make sure that `Python` and `pip` are installed. You can test the `Python` and `pip` commands in the Windows Command Prompt or macOS/Linux Terminal to see if it works or if you get errors. You can download the latest Python version [here](https://www.python.org/downloads/), it should be some version of `Python 3`. Here's a helpful page in [MakeUseOf](https://www.makeuseof.com/tag/install-pip-for-python/) to help you if you need to install `pip` or for troubleshooting.

Then we'll make a file for our script. I named my file `ks-watcher.py`, Python files end with `py`. You can put it anywhere like your Desktop, it doesn't matter right now. Navigate to your file's folder in your Command Prompt/Terminal. Then open the file with your favorite text editor. We can now start writing our code and test it along the way.

### Using `sys`

Open your script file and paste this:

```python
import sys

urls = sys.argv[1:]
if len(urls) == 0:
    print('Please provide at least one Kickstarter project URL to check.')
else:
    print(urls)
```

* `sys` is part of the `Python` standard library so we don't have to download anything to use it.
* `sys.argv` gives us a list of command-line arguments passed to the script.
* `sys.argv[1:]` slices the list and returns a new one, starting from the index `1`, which is actually the second one because the first one is index `0`. The value is then assigned to a variable `urls`.
* `len(urls)` gives us the number of elements in our url list. If no URLs were given, a message is printed.

To use our script we can just run in the command-line:

```
python ks-watcher.py
```

This should show us our message to provide a Kickstarter project URL. Let's test it with a URL.

```
python ks-watcher.py https://www.kickstarter.com
```

Next, we'll write a few functions to do what we want:

1. Download the HTML page in the URL
2. Get the parts that we want from the HTML

### Using `requests`

To download the URL, we'll use the `requests` library, which makes doing this super simple. In the command-line type:

```
pip install requests
```

You should see that it will be downloaded to your computer and we can use it in our script.

```python
import sys

import requests


def get_url(url):
    print('Checking:', url)
    response = requests.get(url)
    if response.ok:
        return response.content
    else:
        print('Something went wrong, try again later...')
        return


urls = sys.argv[1:]
if len(urls) == 0:
    print('Please provide at least one Kickstarter project URL to check.')

for url in urls:
    try:
        content = get_url(url)
        if content:
            print(content)
    except Exception as e:
        print(e)
```

* `get_url()` is a function that accepts the URL, we print it to check what page the script is browsing.
* `requests.get(url)`  here we use `requests` to send a [`GET`](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods) request to the URL and then assign the result to the `response` variable.
* [`response.ok` ](http://docs.python-requests.org/en/master/api/#requests.Response.ok) is used to check if our request went through. Then either the HTML content of the response is returned, or an error message is printed and nothing is returned.
* `for url in urls:` uses our list of URLs in a loop. The indented codeblock below it uses each `url`.
* `try: ... except:` catches any kind of `Exception` or error, which allows us to handle it and our code to continue running. It would be best if we can specify the exceptions here so we can handle them individually. For now, we print it so we can find out what they might be.
* We call`get_url()` inside this block, and if there's content, we print it for now. If there's an error, we also print it.

When we run this code, it just prints the HTML content from the page, or the error if any.

### Using `BeautifulSoup`

To parse the HTML content, we'll use the `BeautifulSoup` library. In the command-line type:

```
pip install beautifulsoup4
```

This is the library that helps us parse the HTML easier.

```python
import sys

import requests
from bs4 import BeautifulSoup as soup


def get_url(url):
    print('Checking:', url)
    response = requests.get(url)
    if response.ok:
        return soup(response.content, 'html.parser')
    else:
        print('Something went wrong, try again later...')


def check_earlybird(content):
    sidebar = content.find_all('li', {'class': 'pledge-selectable-sidebar'})
    for selectable in sidebar:
        title = selectable.find('h3', {'class': 'pledge__title'})
        stats = selectable.find('div', {'class': 'pledge__backer-stats'})
    
        limit = None
        backer_count = None
        if stats:
            limit = stats.find('span', {'class', 'pledge__limit'})
            backer_count = stats.find('span', {'class', 'pledge__backer_count'})
    
        if title and limit:
            title = title.text.strip()
            limit = limit.text.strip()
            if 'limited' in limit.lower():
                message = "{0} - {1}".format(title, limit)
                return message


urls = sys.argv[1:]
if len(urls) == 0:
    print('Please provide at least one Kickstarter project URL to check.')

for url in urls:
    try:
        content = get_url(url)
        if content:
            message = check_earlybird(content)
            print(message)
    except Exception as e:
        print(e)
```

* `from bs4 import BeautifulSoup as soup` imports `BeautifulSoup` and assigns it to the alias `soup`. I did this to make it easier to write.
* `get_url()` was modified to return an instance of the `BeautifulSoup` object and we told it to use the HTML parser.
* `check_earlybird()` is a function that accepts the content, which is now a `BeautifulSoup` object. Within this function, we find the specific HTML elements we're interested in.
* `content.find_all()` and `content.find()` are BeautifulSoup methods provided by the `BeautifulSoup` object to make it easy to look for elements. CSS classes can be a good way to select elements because CSS has to be specific in targetting an element. I inspected the page template to see names were used.
* The `sidebar` has many selectable pledge options so I use `find_all()`.
* I loop through the `selectable` elements to find the title and the stats, from which I also get the limit and backer count.
* `.text.strip()` is used on the `title` and `limit` to remove leading and trailing characters like spaces and new lines.
* `.lower()` is used because we don't know the case the text is written in so we just make sure that everything is in lowercase.
* Then we check if `limited` is present, these early deals usually accommodate a fixed number of backers and is display as `Limited (N left of X)`

To run this script on a page:

```
python ks-watcher.py https://www.kickstarter.com/projects/1183795653/tracxcroll-change-your-trackball-to-the-scroller
```

```
Checking: https://www.kickstarter.com/projects/1183795653/tracxcroll-change-your-trackball-to-the-scroller
Early Bird! - Limited (96 left of 150)
```

Now that's what we're talking about!

We can think of several ways to use this script like enclose it in a loop that runs at certain intervals. You can use [cron](https://www.makeuseof.com/tag/linux-task-scheduling-crontab-explained/) for macOS or Linux to run it according to some schedule. You can also use [Task Scheduler](https://www.makeuseof.com/tag/4-boring-tasks-can-automate-windows-task-scheduler/) for Windows.

One last thing we can add in this script is the ability to get notificationss when we finally detect the message we want. For example, when the phrase "Limited (1 left of" suddenly appears.

### Using `xoxzo.cloudpy`

To send notifications, we'll use our `xoxzo.cloudpy` library. In the command-line type:

```
pip install xoxzo.cloudpy
```

This is our [Xoxzo client library](https://github.com/xoxzo/xoxzo.cloudpy) that helps us use SMS or even voice calls easily using the Xoxzo API.

```python
import sys

import requests
from bs4 import BeautifulSoup as soup
from xoxzo.cloudpy import XoxzoClient


def get_url(url):
    print('Checking:', url)
    response = requests.get(url)
    if response.ok:
        return soup(response.content, 'html.parser')
    else:
        print('Something went wrong, try again later...')


def check_earlybird(content):
    sidebar = content.find_all('li', {'class': 'pledge-selectable-sidebar'})
    for selectable in sidebar:
        title = selectable.find('h3', {'class': 'pledge__title'})
        stats = selectable.find('div', {'class': 'pledge__backer-stats'})
    
        limit = None
        backer_count = None
        if stats:
            limit = stats.find('span', {'class', 'pledge__limit'})
            backer_count = stats.find('span', {'class', 'pledge__backer_count'})
    
        if title and limit:
            title = title.text.strip()
            limit = limit.text.strip()
            if 'limited' in limit.lower():
                message = "{0} - {1}".format(title, limit)
                return message


def send_notification(number, message):
    sid = "<your xoxzo sid>"
    auth_token = "<your xoxzo auth_token>"
    xc = XoxzoClient(sid=API_SID, auth_token=API_TOKEN)
    result = xc.send_sms(
       message = message,
       recipient = number,
       sender = number,
   )


urls = sys.argv[1:]
if len(urls) == 0:
    print('Please provide at least one Kickstarter project URL to check.')

for url in urls:
    try:
        content = get_url(url)
        if content:
            message = check_earlybird(content)
            sms = '{0}\n{1}'.format(url, message)
            result = send_notification('<your number here>', sms)
            msgid = result.messages[0]['msgid']
            print(msgid, sms)
    except Exception as e:
        print(e)
```

The event we're watching for could happen anytime and it would be best to get notified right away. In this case, SMS I would choose SMS as a medium so I can receive it ASAP.

* `from xoxzo.cloudpy import XoxzoClient` here we import the client into our script
* `send_notification()` function was added to use the Xoxzo client and send the message to myself. To use this, we need to [register an account](https://www.xoxzo.com/accounts/signup/) and get an API SID and TOKEN that we can use in our script.
* `XoxzoClient(sid=API_SID, auth_token=API_TOKEN)` here we use our credentials to create a Xoxzo client instance and assign it to the variable `xc`.
* `result = xc.send_sms()` we simply use the `send_sms()` method of XoxzoClient.
