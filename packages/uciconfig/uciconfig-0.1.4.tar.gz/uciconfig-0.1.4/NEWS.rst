=====================
NEWS about uci-config
=====================

Overview of changes to uci-config in reverse chronological order.

0.1.4
=====

* Fix a bug where reloading a store didn't clean previous sections which
  could trigger bugs including the noname section being seen *after* named
  sections.

0.1.3
=====

* Add a CommandLineStore object for use cases where option values can be
  specified as overrides on the command line.

0.1.2
=====

* Support python3.

* Fix empty value parsing ('a=') and the related line handling.

0.1.1
=====

* Add debian packaging (ubuntu native for now).

0.1.0
=====

* Add MANDATORY as a special default value for options that must be set.

* Provide support to write cmdline UI.

0.0.3
=====

* Fix pyflakes issues.

0.0.2
=====

* Revert to python2 to match current needs.

* Fix bugs in exceptions messages.

* Support a default value for RegistryOption.

* Fix comment handling for config values.

* Support Store sharing inside the same process.

* Fix comment handling for sections.

0.0.1
=====

First release.
