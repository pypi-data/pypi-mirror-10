Overview
=======

Designed to be a very basic but easy to use interface to the StopForumSpam API.
At present only querying facilities are provided, I may add an interface for adding data to StopForumSpam.


Alternatives
============

If you're using Django you may wish to use the the more mature [stopforumspam](https://github.com/benjaoming/django-stopforumspam).


Example
=======

```python
>>> from stopforumspam_api import query
>>> r=query(ip="199.115.114.220")
>>> r.appears()
True
>>> r.ip.appears
True
>>> r.ip.frequency
17
>>> r.ip.lastseen
datetime.datetime(2015, 5, 5, 20, 32, 35)
```
