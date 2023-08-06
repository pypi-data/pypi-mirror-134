# Machine Usage
A simple command-line interface that gives an overview of the available resources on our local cluster.

Machine_usage is build using [Textual](https://github.com/willmcgugan/textual/) as the TUI framework. 
This framework is still a work in progress and currently runs on only **MacOS / Linux**. Windows support is in the pipeline. 

Always happy to hear about any bugs or suggested improvements.

## Quick start

Install and run with
```
pip install machine_usage
machine_usage
```

For all options, see
```
machine_usage --help
```
```
Usage: machine_usage [OPTIONS]

  Command line tool to display the current usage of machines on our local
  cluster.

Options:
  --version       Show the version and exit.
  --machine TEXT  (WORK IN PROGRESS) Display load on specific machine.
  --cluster       Overview of the cluster usage.
  --help          Show this message and exit.
```

## TODO
- [ ] Add GPU usage information
- [ ] Make independent of user profile
- [ ] Make functional outside of local network
