#Gestalt - a python-like way to configure your application

In Java we have [Spring Framework](https://spring.io/) that give us this feature. In .NET world we have 
[SlowCheetah](https://marketplace.visualstudio.com/items?itemName=VisualStudioProductTeam.SlowCheetah-XMLTransforms) 
package to do it.

In Python we have freedom to build as we want, as we need, as we can. But on reinventing the wheel - so I decided to 
use [Dynaconf](http://brunorocha.org/python/dynaconf-let-your-settings-to-be-dynamic.html) with some approach.

And it will let your application in compliance with [https://12factor.net/config](https://12factor.net/config) too - 
best practices dude. :p

##Why Gestalt?

See [Gestalt_psychology](https://en.wikipedia.org/wiki/Gestalt_psychology) if you want a kind answer.
In fact is because settings and configuration are very common and I like of this original german word. ;)

##Dependences and how to use

You will need:
 * install dynaconf package dependence.
 * put [gestalt folder files](./gestalt) it in you project.
 * adapt gestalt .py files to what you need.
   - put in [gestalt default.py](./gestalt/default.py) all variables used to your application settings.
   - remember to set a unique value for PROJECT_NAME property in [gestalt __init__.py](./gestalt/__init__.py)
   - replace in [gestalt development.py](./gestalt/development.py), [gestalt staging.py](./gestalt/staging.py) 
   and [gestalt production.py](./gestalt/production.py) the values for each variable as you need.
 * see in [__main__.py](./__main__.py) a sample to use, adapt and be happy. :D

##Why I did it?

I came from .NET platform and my actual team use Java and Docker and we decided to adapt our Python projects nearest as 
possible of our Java projects.

Our goals were:
 * centralize in one file all our settings - we use [./gestalt/default.py](./gestalt/default.py).
 * get from env vars all our sensible data - we use [./gestalt/default.py](./gestalt/default.py) too.
 * set each specific var value to desired environment on a specific file inherited from the created default.
