# kc-hits

- [Description](#description)
- [Installing and running the application](#installing-and-running-the-application)
  - [If python (v3.8+) is already installed on the system](#if-python-v38-is-already-installed-on-the-system)
  - [If python is not installed on the system](#if-python-is-not-installed-on-the-system)
- [Creating a development environment](#creating-a-development-environment)
  - [Building a standalone executable](#building-a-standalone-executable)
- [Releases](#releases)
- [Standalone executables](#standalone-executables)
- [Screenshots of elements of the application](#screenshots-of-elements-of-the-application)
- [References](#references)

## Description

The software "key characteristics of carcinogens - high throughput screening discovery tool" or `kc-hits` is a tool useful in the process of evaluating and classifying chemicals for their carcinogenicity [^1].

It was developed by a team at the International Agency for Research on Cancer (IARC) to help automate the workflow involved in related results from high throughput assays, such as those generated under the ToxCast/Tox21 program [^2], with the Key Characteristics of Carcinogens [^3].

It is a Python application with a graphical user interface.

## Installing and running the application

**NOTE: The application makes use of a database of chemical and assay data. The process of loading the database can be relatively slow on some platforms. So, there may be a significant lag between the time the application is launched and the graphical user interface appears. However, once started, the software should run relatively quickly.**

### If python (v3.8+) is already installed on the system

Install `kc-hits` using `pip`:

```
$ pip install kc-hits
```

The application creates a launchable executable that should be runnable using the following (or some variation, depending on the operating system):

```
$ kc-hits_vxxx.exe
```

where xxx is the version number (e.g., `kc-hits_v0.6.0.exe`).

### If python is not installed on the system

Make use of one of the standalone executables listed below. No further dependencies should be required. The executable should be launchable as any other application on the system.

## Creating a development environment

There are several dependencies that must be installed. These are listed in
`environment.yml`.

It is recommended that users create a virtual environment to run or work
with the application.

The commands below reflect the use of the [conda](https://docs.conda.io/en/latest/) tool for managing virtual environments.

After cloning the repository and navigating into the main directory, create the environment with the dependencies and activate the environment:

```
$ conda env create -f environment.yml

$ conda activate kc_hits
```

The application may then be run using

```
$ python kc_hits.py
```

### Building a standalone executable

To build a standalone executable, make sure the virtual environment is active and that the `pyinstaller` executable is in your path. Then use the following:

```
$ pyinstaller -wF --clean kc_hits.spec
```

The executable will be created in the `dist` subdirectory.

## Releases

| Version | Notes                                                             |
| ------- | ----------------------------------------------------------------- |
| 0.5.4   | Used in the workflow for IARC Volume 130                          |
| 0.6.0   | Incorporates information from the ToxCast/Tox21 data release v3.4 |

## Standalone executables

| Version | Platform   | url                                    |
| ------- | ---------- | -------------------------------------- |
| 0.6     | MS Windows | https://doi.org/10.5281/zenodo.5831533 |

## Screenshots of elements of the application

The chemical selection pane:

![image of chemical selection pane](https://gitlab.com/i1650/kc-hits/-/raw/main/images/chemical_selection_pane.png?raw=true "chemical selection pane")

The two panes with summary results shown:

![image of summary results](https://gitlab.com/i1650/kc-hits/-/raw/main/images/summary_results.png?raw=true "summary results")

The two panes with detailed results shown:

![image of detailed results](https://gitlab.com/i1650/kc-hits/-/raw/main/images/detailed_results.png?raw=true "detailed results")

One of the worksheets of the saved report spreadsheet:

![image of report spreadsheet](https://gitlab.com/i1650/kc-hits/-/raw/main/images/report_spreadsheet_01.png?raw=true "report spreadsheet")

![image of report spreadsheet](https://gitlab.com/i1650/kc-hits/-/raw/main/images/report_spreadsheet_02.png?raw=true "report spreadsheet")

## References

[^1]: Samet,J.M. et al. (2020) The IARC Monographs: Updated Procedures for Modern and Transparent Evidence Synthesis in Cancer Hazard Identification. J. Natl. Cancer Inst., 112, 30–37.
[^2]: Richard,A.M. et al. (2016) ToxCast Chemical Landscape: Paving the Road to 21st Century Toxicology. Chem. Res. Toxicol., 29, 1225–1251.
[^3]: Smith,M.T. et al. (2016) Key Characteristics of Carcinogens as a Basis for Organizing Data on Mechanisms of Carcinogenesis. Environ. Health Perspect., 124, 713–721.
