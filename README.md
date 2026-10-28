# Cloud VM Monitoring with Python

A lightweight command-line monitoring tool for tracking CPU, memory, and disk usage on a virtual machine. The project is designed for cloud-hosted VMs such as AWS EC2, Google Compute Engine, and Azure Virtual Machines, but it can also run on a local computer.

## Overview

This project uses Python and [`psutil`](https://github.com/giampaolo/psutil) to collect basic system-health metrics at regular intervals. The current implementation prints the latest readings directly to the terminal, making it useful as a simple starting point for cloud VM observability and monitoring experiments.

## Features

- Monitors CPU utilization
- Monitors memory utilization
- Monitors disk utilization for the root filesystem (`/`)
- Refreshes metrics every five seconds
- Uses a minimal Python implementation with one runtime dependency
- Works on local machines and supported cloud virtual machines

## Requirements

- Python 3.8 or newer recommended
- A Linux, macOS, or Windows environment supported by `psutil`
- Access to a terminal or shell

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/m0hitd/Cloud-VM-Monitoring-with-Python.git
   cd Cloud-VM-Monitoring-with-Python
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install the dependency:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Start the monitor with:

```bash
python main.py
```

The program continuously prints output similar to:

```text
CPU: 12.5%, Memory: 47.8%, Disk: 36.2%
```

Press `Ctrl+C` to stop the monitor.

## How It Works

The monitor performs the following steps in a loop:

1. Samples CPU usage over a one-second interval.
2. Reads the current system memory usage.
3. Reads disk usage for the root filesystem.
4. Prints the collected values.
5. Waits five seconds before collecting the next sample.

## Project Structure

```text
.
├── main.py           # Monitoring logic and command-line entry point
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## Configuration

The current monitoring interval is defined in `main.py`:

- CPU sampling interval: 1 second
- Delay between readings: 5 seconds
- Disk path: `/`

These values can be adjusted as the project grows. For Windows environments, the disk path may need to be changed from `/` to an appropriate drive path such as `C:\\`.

## Limitations and Future Improvements

This is an initial implementation intended as a foundation for a more complete VM monitoring solution. Potential improvements include:

- Add configurable sampling and refresh intervals
- Add warning thresholds for high CPU, memory, or disk usage
- Log metrics to a file or monitoring service
- Export metrics in a format such as JSON or Prometheus
- Add structured logging and error handling
- Support monitoring multiple disks
- Add cloud-specific integrations and alerting
- Add automated tests
- Add graceful shutdown handling for long-running deployments

## License

No license has been specified for this repository yet. Add a license file before distributing or reusing the project publicly.
