# IDOC
Individual Drosophila Optogenetic Conditioner

 * [Introduction](#introduction)
 * [How to do an experiment](#how-to-do-an-experiment)
    * [Open software](#open-software) 
    * [Run software](#run-software) 
    * [Start the experiment](#start-the-experiment)
    * [Browse and understand your results](Browse-and-understand-your-results)
    * [Analyze traces](#analyze-traces)
 * [Make a paradigm](#make-a-paradigm)
 * [Indices](#indices)
  * [Read the logs](#read-the-logs)
 * [Enhancements](#enhancements)
    

# Install

1. Create a conda environoment

`conda create --name idoc python=3.7.4`

2. Install pypylon

Running `pip install pypylon` may install a version of the package which is buggy in conda environments.
We recommend to instead do the following

`pip install git+https://github.com/basler/pypylon.git@1cbda303a0ab0d335c82f0460e71c0cc5c12bbeb`

This will install from source the version of the module available under the git hash commit `1cbda303a0ab0d335c82f0460e71c0cc5c12bbeb`. This version was verified in Ubuntu 20.04.3

3. Install idoc

`pip install idoc`

4. Set minimal configuration

The configuration is by default installed to

`$HOME/idoc/idoc/config/idoc.conf` in JSON format

You need to enter three fields under the `"folders.results"` entry

1. results: Path to a directory where the data from the new experiments will be saved
2. mappings: Path to a directory containing at least one mapping .csv file
3. paradigms: Path to a directory containing at least one paradigm .csv file

A valid mapping should look like this:

```
hardware,pin_number
IRLED,45
LED_R_LEFT,3
LED_R_RIGHT,2
```

A valid paradigm should look like this

```
hardware,start,end,on,off,mode,value
IRLED,0,5,NaN,NaN,o,1
LED_R_LEFT,1,2,1,1,o,1
LED_R_RIGHT,1,2,1,1,o,1
```

See more in the section

5. Provide the default mapping and the default paradigm

IDOC needs the paradigm and mapping passed in the config to be available at boot.
Therefore, you need to make sure the file listed in the config under 
* `controller.paradigm_path` exists in the directory under `folders.paradigms.path`
* `controller.mapping_path` exists in the directory under `folders.mappings.path`


CLI
=======


# To execute with the controller module

```
idoc-server --control
```


# To load a program

```
echo '{"program_path": "AV_vs_Air.csv"}' | curl -d @- localhost:9000/load_program
```


# To run a program

```
curl localhost:9000/controls/record
```
