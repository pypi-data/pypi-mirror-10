Flent: The FLExible Network Tester
==================================

Python wrapper to run multiple simultaneous netperf/iperf/ping instances
and aggregate the results. The main documentation is in the man page,
`available as HTML here <https://tohojo.github.io/flent.1.html>`__.

Tests are specified as config files (which are really Python), and
various parsers for tool output are supplied. At the moment, parsers for
netperf in -D mode, iperf in csv mode and ping/ping6 in -D mode are
supplied, as well as a generic parser for commands that just outputs a
single number.

Several commands can be run in parallel and, provided they output
timestamped values, (which netperf ping and iperf do, the latter with a
small patch, available in the misc/ directory), the test data points can
be aligned with each other in time, interpolating differences between
the actual measurement points. This makes it possible to graph (e.g.)
ping times before, during and after a link is loaded.

An alternative run mode is running several iterated tests (which each
output one data point, e.g. netperf tests not in -D mode), and
outputting the results of these several runs.

The aggregated data is saved in (bzipped) json format for later
processing and/or import into other tools.

Apart from the json format, the data can be output as csv values, emacs
org mode tables or plots. Each test can specify several different plots,
including time-series plots of the values against each other, as well as
CDF plots of (e.g.) ping times.

Plotting requires a functional matplotlib installation (but everything
else can run without matplotlib), and can be output to the formats
supported by matplotlib by specifying the output filename with -o
output.{png,ps,pdf,svg}. If no output file is specified, the plot is
diplayed using matplotlib's interactive plot browser, which also allows
saving of the output (in .png format).

The basic invocation is ``./flent -H <host> <test_name>``. Various
options to control test parameters are available; try running
``./flent -h``. Tests can be displayed with ``./flent --list-tests`` and
the available plots can be displayed with
``./flent --list-plots <test_name>``.

Running tests and plotting/displaying the output is logically split up
in two separate processes, but can be combined into one. When a test is
run, its data output is always saved in a file called
``<test_name>-<date>.flnt`` in the same directory as the output file
selected with -o (or the current directory if no output file is
selected). This file can be read back in with the -i switch, in which
case the test will not be run again, but the saved test data will be
used as input for plotting functions etc. If an output format is
selected while a test is run, the test data will be used directly for
this output, but will still be saved in the json file.

Installing
----------

Install the package system-wide by running
``sudo python2 setup.py install`` or ``sudo pip install flent`` for the
latest released version. Packages for Debian/Ubuntu and Arch Linux are
available at OBS:
https://build.opensuse.org/project/repositories/home:tohojo:flent.

Quick Start
-----------

You must run netperf on two computers - a **server** and a **client**.

#. **Server (Computer 1):** Netperf needs to be started in "server mode"
   to listen for commands from the Client. To do this, install netperf
   on the Server computer, then enter:

   ``netserver &``

   *Note:* Instead of installing netperf on a local server, you may
   substitute the netserver that is running on netperf.bufferbloat.net
   by using "-H netperf.bufferbloat.net" in the commands below.

#. **Client (Computer 2):** Install netperf, then install flent on your
   Client computer. When you invoke flent on the Client, it will connect
   to the specified netserver (-H) and carry out the measurements. Here
   are some useful commands:

   -  | RRUL: Create the standard graphic image used by the Bufferbloat
        project to show the down/upload speeds plus latency in three
        separate charts.
      | 
        ``flent rrul -p all_scaled -l 60 -H address-of-netserver -t text-to-be-included-in-plot``

   -  | CDF: A Cumulative Distribution Function plot showing the
        probability that ping times will be below a bound.
      | 
        ``flent rrul -p ping_cdf -l 60 -H address-of-netserver -t text-to-be-included-in-plot``

   -  | TCP Upload: Displays TCP upload speed and latency in two charts.
      | 
        ``flent tcp_upload -p totals -l 60 -H address-of-netserver -t text-to-be-included-in-plot``

   -  | TCP Download: Displays TCP download speeds and latency in two
        charts.
      | 
        ``flent tcp_download -p totals -l 60 -H address-of-netserver -t text-to-be-included-in-plot``

The output of each of these commands is a graphic (PNG) image along with
a data file in the current working directory that can be used to
re-create the plot, either from the command line (see the man page), or
by loading them into the GUI. Run ``flent --gui`` to start the GUI.

The json data format
--------------------

The aggregated test data is saved in a file called
``<test_name>-<date>.flnt``. This file contains the data points
generated during the test, as well as some metadata. The top-level json
object has five keys in it: ``version``, ``x_values``, ``results``,
``metadata`` and ``raw_values``.

``version`` is the file format version as an integer.

``x_values`` is an array of the x values for the test data (typically
the time values for timeseries data).

``results`` is a json object containing the result data series. The keys
are the data series names; the value for each key is an array of y
values for that data series. The data array has the same length as the
``x_values`` array, but there may be missing data points (signified by
null values).

``metadata`` is an object containing various data points about the test
run. The metadata values are read in as configuration parameters when
the data set is loaded in for further processing. Not all tests use all
the parameters, but they are saved anyway.

``raw_values`` holds an array of objects for each data series. Each
element of the array contains the raw values as parsed from the test
tool corresponding to that data series.
