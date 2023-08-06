dap2rpm
=======

Generate RPM specfiles for DevAssistant DAP packages.

Usage::

   dap2rpm revealjs
   dap2rpm revealjs -v 0.2
   dap2rpm revealjs -L LICENSE NOTICE
   dap2rpm Downloads/revealjs-0.2.dap

**Note for non-Fedora users**: As dap2rpm is intended primarily for use in
Fedora, it automatically strips off the pre-release tags from the version
string (e. g.  ``0.1dev`` becomes ``0.1``), and attaches it to the Release tag
in the SPEC (in this case, ``Release: 0.1.dev%{?dist}``). This behaviour is
mandated by the Fedora Packaging Guidelines. If you want to avoid it, specify
the argument ``--keep-format`` when running dap2rpm.
