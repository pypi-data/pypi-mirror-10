[![Build Status](https://travis-ci.org/zniper/django-scraper.svg?branch=master)](https://travis-ci.org/zniper/django-scraper)
[![Coverage Status](https://coveralls.io/repos/zniper/django-scraper/badge.svg?branch=master)](https://coveralls.io/r/zniper/django-scraper?branch=master)
[![Downloads](https://pypip.in/download/django-scraper/badge.svg)](https://pypi.python.org/pypi/django-scraper/)
[![Latest Version](https://pypip.in/version/django-scraper/badge.svg)](https://pypi.python.org/pypi/django-scraper/)

**django-scraper** is a Django application for collecting online content following user-defined instructions

Features
--------

* Extract content of given online website/pages and stored under JSON data
* Crawl then extract content in multiple pages, with given depth.
* Can download media files present in page
* Have option for storing data under ZIP file
* Support standard file system and AWS S3 storage
* Customisable crawling requests for different scenarios
* Process can be started from Django management command (~cron job) or with Python code
* Support extracting multiple content (text, html, images, binary files) in the same page
* Have content refinement (replacement) rules and black words filtering
* Support custom proxy servers, and user-agents

_Support Django 1.6, 1.7, and 1.8_

Samples
-------

Below is a sample result from scraping https://news.ycombinator.com/ask

* [Reusult ZIP file](https://dl.dropboxusercontent.com/u/44239448/94f8f6d9-news.ycombinator.com.zip)
* JSON result via a renderer:
  ![JSON result](https://dl.dropboxusercontent.com/u/44239448/scraper-screen.jpg)

Important Notice
----------------
Since version 0.3.0, django-scraper have completely different data models, those have been redesigned to better work with complex requests and easier to maintain.

And the consequence is older versions cannot run migration with this one. Please clean the old structure before performing new migration or syncdb.

There are some more difference in settings and returned data. Please refer to configuration part for more details.

Installation
------------
This application requires some other tools installed first:
    
    lxml
    requests

**django-scraper** installation can be made using `pip`:

    pip install django-scraper
    
Configuration
-------------
In order to use **django-scraper**, it should be put into `Django` settings as installed application.
    
    INSTALLED_APPS = (
        ...
        'scraper',
    )

If `south` is present in current Django project, please use `migrate` command to create database tables. 
  
    python manage.py migrate scraper

Otherwise, please use standard 'syncdb' command

    python manage.py syncdb
    
There is also an important configuration value should be added into `settings.py` file:

    SCRAPER_CRAWL_ROOT = '/path/to/local/storage'

Some optional setting options are:
    
    SCRAPER_COMPRESS_RESULT = True/False
    SCRAPER_TEMP_DIR = '/your_temp_dir/'

When having two above options with `SCRAPER_COMPRESS_RESULT` set to True, the application will compress crawled data and store under a Zip file.

    SCRAPER_NO_TASK_ID_PREFIX = 'any-prefix'

This one is a custom value which will be added at front of task ID (or download location) of each crawled result.
    
Usage
-----

Since version 0.3.0, there is no more `Source`. It's kind of broken into new models: `Spider`, `Collector`, `Selector`

* **Selector** - Definition of single data portion, which contains key (name), XPath to wanted content and data type
* **Collector** - Contains list of Selectors which will extract data from a given page. Besides, it has replace rules, black words and option for download images.
* **Spider** - The one (with list of Collectors) crawls from one page to another to collect links then perform extracting data from those pages using Collector's methods.

###### Spider
* `url` - URL to the start page of `source` (website, entry list,...)
* `name` - Name of the crawl session
* `target_links` - List of XPath to links pointing to pages having content to be grabbed (entries, articles,...)
* `expand_links` - List of XPath to links pointing to pages containing target pages. This relates to crawl_depth value.
* `crawl_depth` - Max depth of scraping session. This relates to expand rules
* `crawl_root` - Option for extracting starting page or bypass.
* `collectors` - List of collectors which will extract data on target pages
* `proxy` - Proxy server will be used when crawling current source
* `user_agent` - User Agent value set in the header of every requests

###### Collector
* `name` - Name of the collector
* `get_image` - Option to download all images present in extracted `html` content
* `selectors` - List of selectors pointing to data portion
* `replace_rules` - RegEx List of regular expressions will be applied to content to remove redundant data.

    *Example:*
        [('`<br/?>`', ''), ('`&nbsp;`', '')]

* `black_words` - Select set of words separated by comma. A page will not be downloaded if containing one of those words.
* `proxy` - Proxy server will be used when crawling current source
* `user_agent` - User Agent value set in the header of every requests

###### Selector
* `key` - Name of the selector
* `xpath` - XPath to the content to be extract
* `data_type` - Type of the content, which could be: `text`, `html`, `binary`

There are several ways to extract content or start a scraping session:

    a_collector.get_content('http://....')
    a_spider.crawl_content()

or under console, by running management command `run_scraper`:
    
    $python manage.py run_scraper
    
With this command, all active spider inside current Django instance will be processed consecutively.

--

*For further information, issues, or any questions regarding this, please email to me@zniper.net*
