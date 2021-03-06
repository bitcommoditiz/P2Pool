This is a modified version of the original forrestv p2pool
-------------------------
* handle all bitcommoditiz
* some minor bugs fix
* merged with nice web interface by hardcpp

Thanks to hardcpp and forrestv for their original work available at:
https://github.com/forrestv/p2pool
https://github.com/hardcpp/P2PoolExtendedFrontEnd
 

Running P2Pool:
-------------------------
Run P2Pool with the "--net xxx" option, where xxx is the bitcommoditiz you are P2pooling

Example :

	python run_p2pool.py --net xauz --no-bugreport --address GJHJhvh677OOJHHGGF --disable-upnp

Run for additional options.

    python run_p2pool.py --help

Once p2pool is running point your miner to 127.0.0.1 on the miner port of the bitcommoditiz you want to mine.
Provide your bitcommoditiz address as username to get your reward (no account needed).

Example (your miner is minerd and you are mining on your own local Goldz pool):

	/minerd --no-stratum --url http://127.0.0.1:15500/ --user GKLkjBGFRh123456


Here are the values for the various bitcommoditiz worker port.

	NAME          SYMBOL     WORKER_PORT   REWARD   UNIT
	Goldz          xauz       15500           1     OZz (Ouncez)
	Palladiumz     xpdz       15502           1     OZz (Ouncez)
	Silverz        xagz       15504           1     OZz (Ouncez)
	Platiniumz     xptz       15506           1     OZz (Ouncez)
	Crude Oilz     clz        15508           1     bblz (Barrelz)
	Wheatz         wz         15510           1     Tz (Tonz)
	Cornz          zcz        15512           1     Tz (Tonz)
	Cottonz        ctz        15514           1     lbz (Poundz)
	Coffeez        kcz        15516           1     lbz (Poundz)
	Cocoaz         ccz        15518           1     Tz  (Tonz)



If you want to operate a public bitcommoditiz pool and get payment for that launch p2pool on a public server with :
  -f FEE_PERCENTAGE, this charge workers such percentage fee to mine on your p2pool instance. The fee is for you.


Requirements:
-------------------------
Generic:
* Bitcommoditiz node >=0.8.6.3
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)
* build with scrypt support (see bellow)

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages


Donations towards further development (donation in bitcoin to the original author forrestv):
    1HNeqi3pJRNvXybNX4FKzZgYJsdTSqJTbk

Official wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool


Notes for Bitcommoditiz:
=========================
Requirements:
-------------------------
In order to run P2Pool with the bitcommoditiz network, you would need to build and install the
ltc_scrypt module that includes the scrypt proof of work code that bitcommoditiz use for hashes.

Linux:

    cd bitcommo_scrypt
    sudo python setup.py install

Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    cd bitcommo_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install

Windows (microsoft visual c++)
* Open visual studio console

In bash type this:

    SET VS90COMNTOOLS=%VS110COMNTOOLS%	           # For visual c++ 2012
    SET VS90COMNTOOLS=%VS100COMNTOOLS%             # For visual c++ 2010
    cd bitcommo_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install
	
If you run into an error with unrecognized command line option '-mno-cygwin', see this:
http://stackoverflow.com/questions/6034390/compiling-with-cython-and-mingw-produces-gcc-error-unrecognized-command-line-o

Sponsors:
-------------------------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool

