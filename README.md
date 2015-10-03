# Brooks

Brooks is software process dynamics simulator for Brooks' Law.

## Installation

As of now, there is no installer.

## Usage

Clone and modify one of the existing Python modules in the `schedules` directory to describe the simulation you want
to run, the run the simulation with:

    $ cd brooks
    $ python3 -m brooks schedules/schedule_a.py --output=data/schedule_a.tsv -- software_development_rate
    
This runs the simulation with `schedule_a` and captures the `software_development_rate` attribute of the model
state into a tab-separated value (TSV) file, which can then be inspected in a text editor or spreadsheet.

The results from one or more simulation runs with different schedules can be charted with:

    $ python3 software_development_rate data/schedule_a.tsv data/schedule_b.tsv
    
This gives a chart of the `software_development_rate` attribute for the run results from `schedule_a` and
`schedule_b`.
    
