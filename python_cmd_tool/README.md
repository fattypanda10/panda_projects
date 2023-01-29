## Python Command Line Tool for Debian Packages

Download and Get Package Statistics for a given architecture

<!-- TOC -->

* [Python Command Line Tool for Debian Packages](#python-command-line-tool-for-debian-packages)
    * [General Directory Structure](#general-directory-structure)
    * [Basic Project Info](#basic-project-info)
    * [Project Description | Approach](#project-description--approach)
    * [Other files](#other-files)

<!-- TOC -->

#### General Directory Structure

<img src="canonical/static/dir_tree.png" width="350" alt="project directory structure"/>

#### Basic Project Info

- package and dependency management tool - Poetry
- VCS - git
- major [pre-commit hooks](./.pre-commit-config.yaml) for formatting code
    - black
    - flake8
    - isort
- license - [MIT](./LICENSE.md)
- *main.py* - entry point for the tool [main script](canonical/main.py)
- more info under [Project TOML](./pyproject.toml)

#### Project Description | Approach

- The goal comprises primarily of two actions, which is achieved through two types of objects
    - **Downloader**:
        - check if architecture names file exists locally
            - if yes
                - then search in it and fetch the contents ✅
            - if no
                - then make a request to base URL
                - get the architecture names
                - fetch content (HTML)
                - parse (HTML) to get all URLs of gzip files
                - get arch names from them and save them locally in a txt file
                - re-check if the name exists
                    - if yes, go ahead and fetch the contents ✅
                    - if no, exit out (max attempt reached - 1) ❌
        - the above logic
            - prevents an additional (if not needed) request to server
            - faster
        - after the contents of architecture are fetched using its URL
            - get content and save as gzip locally
            - also save content as a txt (*bytes*) file for further use
    - **Parser**:
        - open the saved txt file
        - get content in right format (*bytes --> str*)
        - parse the raw text
        - process contents
            - two methods - **split-based** & **regex-based** (flag can be set in *main.py* if required)
                - **split-based**
                    - principle - split the contents and then get file(s) and package(s) considering the fact that
                      package(s) will always be towards the end (second column) and file(s) in the first column
                      separated by one or more whitespace (as described in *content-indices* format)
                    - define two dict
                        - dict with packages as keys and number of files in them as values
                            - memory-efficient
                            - faster
                        - dict with packages as keys and the files in them as values
                            - can also be processed and obtained, if needed (user-defined)
                    - there could be four cases based on a row (2 columns - file & package)in the data
                        - file and package both present
                        - either one is missing (both cases handled together) --> categorised under "ungrouped data"
                            - more functionality is needed to verify if the missing element is package or file
                        - both are missing --> row skipped/ignored
                    - **regex-based**
                        - principle - match the package(s) in the data row based on regex
                        - rest is same as above after the file(s) and package(s) have been obtained
                        - if the regex match fails (though has been tested a lot), it uses the above method rather than
                          crashing
        - process the dict to get package stats
            - sort (default descending) the dict based on values (no of files)
            - get the top-n (default n = 10) packages
            - format the required results
            - output to console
            - also save (optional) the results in a txt file for later use
    - The above was achieved through two classes with same names
    - Corresponding directory and files
        - *modules*
            - *downloader.py*
            - *parser.py*
- To handle the cmdline functionality for running the script from cmdline, to get the architecture from user and other
  options, a separate script was written
    - two main functions
        - function *args_parser*
            - sets up the *argparse.Namespace* for cmdline arguments
            - two arguments - positional *arch* and optional *verbose*
            - validates the *arch* argument
            - returns the *Namespace*
        - function *validate_arch*
            - validates the *arch* argument from cmdline
            - basis for validation - purely numeric architecture names do not exist (till now)
            - if validated, returns the lowercase value of *arch*
    - Corresponding directory and file
        - *modules*
            - *cmdline_parser.py*
- Logging for the whole project is handled through a logger, defined separately once
    - root logger and subsequent use in different modules
    - two handlers - File and Stream - with different log levels
    - logs are stored under *logs* directory
    - formatter to get relevant info
    - returns configured logger
    - Corresponding directory and file
        - *logs*
            - *log_info.log*
- Tests for some major functions were written
    - *pytest* as the testing library
    - *conftest.py* contains the required fixtures and mocks
    - Corresponding directory and file
        - *tests*
            - *test_cmdline_parser.py*
            - *test_downloader.py*
            - *test_parser.py*
        - *canonical* (root)
            - *conftest.py*
- Main script
    - *main.py* is the main script for invoking the tool from command line or running directly
    - cmdline usage
        - *python main.py {req: architecture name} {optional: verbosity}*
        - for help and usage: *python main.py -help*

#### Other files

- *static* - consists of images for readme
- project files - Poetry, git
