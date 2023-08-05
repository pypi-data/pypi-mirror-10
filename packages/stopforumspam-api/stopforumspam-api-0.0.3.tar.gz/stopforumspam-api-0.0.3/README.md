Overview
=======

Designed to be a very basic but easy to use interface to the StopForumSpam API.
You can use this the query StopForumSpam and, provided you have a key, add data to the database too.

It is important to read and understand StopForumSpam's terms before using this software.


Alternatives
============

If you're using Django you may wish to use the the more mature [django-stopforumspam](https://github.com/benjaoming/django-stopforumspam).


Installation
============

    pip install stopforumspam_api


Example
=======

```python
>>> from stopforumspam_api import query
>>> response = query(ip="199.115.114.220")
>>> respone.appears()
True
>>> response.ip.appears
True
>>> response.ip.frequency
17
>>> response.ip.lastseen
datetime.datetime(2015, 5, 5, 20, 32, 35)
```
