Neo-Observer is a Python module implementing the observer pattern using
a centralized registry. You send an event to the registry and it will
dispatch the call the registered observers of the event. You can
register functions or subclasses of a defined observable interface.
Events have a name, a sender and optional info object. You can register
an observable to receive an event based on its name, sender or both.
Require Python 2.5 and higher (excluding Python 3).

2011-04-19: To remove any ambiguity, adding the same observer again
cancel the previous registration.

2011-04-19: *New improved version*

-  Use weak references whenever it is possible. Objects no longer
   referenced by your code will not receive events so you don’t have to
   remember to call ‘remove\_observer’.

-  Any callable can be used as an observer as long as the callable can
   be called with the single event argument or without argument at all.

-  When adding an observer, you can specify the method to be called on
   the observer to receive the event.

-  Implementation changes: Using a type hierarchy instead of a type flag
   for the different types of observers.

While I was having a centralized registry in mind when I was creating
this class, I realize that ObserverRegistry can work in a decentralized
way too. Any class derived from ObserverRegistry is an ObserverRegistry
too (just don’t forget to call **init**).

Author: Pierre Thibault (pierre.thibault1 -at- gmail.com)

License: MIT

Project site: https://github.com/Pierre-Thibault/neo-observer

Epydoc documentation located at:
https://github.com/Pierre-Thibault/neo-observer/wiki/doc/index.html but
it is html so it is better to clone the wiki and open it locally in a
web browser.

Join the user group: http://groups.google.com/group/neo-users
