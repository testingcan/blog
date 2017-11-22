Title: Crawling dynamically generated content with Scrapy
Date: 2017-11-21
Category: Tutorial
Tags: scrapy, python
Summary: Learn how to crawl dynamic pages with Scrapy.

[One](https://stackoverflow.com/questions/33185651/python-scrapy-for-dynamic-content) [of](https://stackoverflow.com/questions/27525142/selenium-ajax-dynamic-pagination-base-spider) [the](https://stackoverflow.com/questions/44110505/no-data-after-scraping-a-website) [most](https://stackoverflow.com/questions/41165599/how-to-get-the-href-and-associated-information-using-scrapy) [frequent](https://www.reddit.com/r/learnpython/comments/6ij1qa/trying_to_get_a_url_using_bs4_but_source_code_is/) questions I have encountered concerning Scrapy is how to crawl dynamic pages. People may learn about Scrapy because their goal is to crawl a particular page, but then fail to understand why their Spider returns only empty outputs. 
You may have run into this problem. Odds are, since you are reading this, you may have this problem right now. I know that I did. 
Frequently people will resort to Selenium or Splash or whatever, to simulate a browser in order to crawl a dynamic webpage. In my opinion the likes of Selenium can be overkill for many crawling-tasks, especially if your goal is only to crawl a dynamic webpage. Scrapy is well capable of crawling dynamic pages and by learning how to do it, you will gain many important skills that will help you analyze websites and build better spiders. 

## What you will learn

In this article I will go into the following skills:

* Learning how to use the scrapy shell to assess a website
* Learning how to identify requests that are made on a website
* Learning how to duplicate the necessary requests in your spider

So let's dive right in with the first question you will likely as yourself, when confronted with a dynamic webpage...

## Why does my Spider not return anything? 

I had just learned about Scrapy because a project at work would have needed, well, Webscraping. After researching and weighing countless options, I finally found this little library written in Python. Getting it up and running was fairly easy, using small websites with a rather limited complexity. Eagerly, I jumped into the real project, crawling a web-shop in order to compare prices. After having set up the spider and running it, I found out to my dismay that my trusted csv-file was populated by... 

Nothing. 

Cue multiple code-reviews, hours of reading and dozens of curses. My spider seemed to be correct. I must have missed something. If you read the linked questions in the beginning, you might have seen that many people people have a completed spider, that is basically correct, but not for this task. So how do we know if we are dealing with a dynamic webpage? 

### Use the shell!

The Scrapy shell is a wholly powerful tool, a must for beginners and... wholly underutilized. Beginners start by putting together complex spiders for hours on end only to realize that the spider they have coded is completely unfit for the task at hand. Again, I did too. 
