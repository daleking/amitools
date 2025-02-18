# Change Log

## [0.2.0][2] (2019-06-27)

### vamos

* Re-implemented dos ReadArgs() to be more compatible (#80)
* Re-implemented dos ReadItem() to be more compatible
* Fix exception when running in Vim (#77) (@zedr)
* added more tests to vamos-test suite
* Allow to SelectInput()/SelectOutput() with BNULL
* truncate inodes to 32 bit for fl_Key in Lock (workround for 64bit fs) (#72, #35)
* added dummy OpenResource() (@selco)
* added Uitlity's Amiga2Date(), Date2Amiga(), CheckDate() (@selco)
* added full math library support (double, single and ffp precision) (@selco)
* Added ExamineFH() (@bebbo)
* fix SDivMod32 (@bebbo)
* added Docker based toolchains for building test programs with vc, gcc6 and AROS gcc
* added profiling support
* machine: run code in user mode
* machine: do not pulse reset on every run
* allow to create temp volumes
* allow to auto create assign dirs
* machine: removed obsolete Trampoline (replaced by machine sub runs)
* complete rewrite of config infrastructure. added .json configs
* rewrote lib handling and support creation via MakeLibrary() 
* replaced VamosRun with a machine layer
* honor cwd and progdir in OpenLibrary() calls
* added GetProgramDir()
* do not split command line args when parsing. fixed args with comma, parentheses.

### hunktool

* fixed loading of short relocations

### romtool

* fixed romtool to allow splitting ext ROMs
* updated split files to ROMsplit 1.25
* fixed scanning residents without name

### xdftool

* allow to format/work with partitions of arbitrary block size (>512 bytes) (>4GB FFS)
* fixed relabel command (@Zalewa)

### rdbtool

* added import/export partition image
* fixed init of empty disk

### misc

* started moving the docs to RST and ReadTheDocs
* added vamostool and refactored typetool and vamospath


## [0.1.0][1] (2017-08-03)

* First public release


[1]: https://github.com/cnvogelg/amitools/tree/v0.2.0
[2]: https://github.com/cnvogelg/amitools/tree/v0.1.0
