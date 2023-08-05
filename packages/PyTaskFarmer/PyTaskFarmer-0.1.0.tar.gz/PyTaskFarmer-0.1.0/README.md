# PyTaskFarmer

This is a small project of a Python TaskFarmer for running jobs at NERSC's Cori
(though it should be flexible to run on other systems). It is very loosely based
on the concept of [Shane Canon's TaskFarmer](https://github.com/scanon/taskfarmer).

[Full Documentation](https://pytaskfarmer.readthedocs.io/en/latest/)

## Usage

The executable script is:

    usage: pytaskfarmer.py [-h] [--proc [Processes]] [--timeout TIMEOUT]
                            [--workdir WORKDIR] [--verbose VERB]
                            [--runner RUNNER] [--tasklist TASKLISTHANDLER]
                            tasklist

The `tasklist` argument is a simple text file with one task per line. The
interpretation of the task is up to the `TASKLISTHANDLER`. By default, the task
is treated as a command to run. It is not important how complex the command is.

The `--verbose` flag adds a bit more output (though not much) telling you what
the script is doing as it runs (default False).

The `--timeout` option allows you to set a timeout for the script, so that after
 some number of seconds the tasks will be automatically killed (default none).

The `--proc` option tells the script how many parallel workers to create
(default8).

The `--workdir` option tells the script where to store the progress (task
status, log files..) of a single run (default is `tasklist_workdir`).

The `--runner` options indicates which runner to execute the command with. See
the dedicated section on the available runners and how they work.

The `--tasklist` options indicates which tasklist handler to parse the tasklist
with. See the dedicated section on the available runners and how they work.

## What it does (60 second version)

The basic behavior, with the default runner/handler, is as follows. Each access
to a file is protected using a file locking mechanism.

1. The tasklist is read and a `toprocess` file is created in the `workdir` with
   unprocessed tasks.

2. A number of workers (`multiprocessing.Pool`) are constructed to run on
   the tasks.

3. When some work is done, the command is placed into a `finished` or `failed`
   files, depending on the status code.

4. Duration and start times of completed tasks (timeline) are saved into a
   `timeline.json` file. This can then be opened with
   [Perfetto](ui.perfetto.dev).

5. The tasks are processed by the workers until 1) the work is completed; 2) the
   timeout is reached; or 3) a signal is intercepted.