pytest-trialtemp
================

py.test plugin for using the same _trial_temp working directory as trial


usage
-----

Install the plugin with ``pip install pytest-trialtemp`` and it will be used
automatically when tests are run.

To disable it for a particular run, use ``py.test -p no:trialtemp [...]`` to
run your tests. See pytest's documentation for further options.


why?
----

I frequently use ``py.test`` to run Twisted tests written using ``trial``. This
works pretty well on its own, except trial's temporary directory infrastructure
assumes the working directory during test runs is ``./_trial_temp`` or
something similar.

In order to avoid littering my project root with annoying test-created
temporary directories, I wrote this little plugin.
