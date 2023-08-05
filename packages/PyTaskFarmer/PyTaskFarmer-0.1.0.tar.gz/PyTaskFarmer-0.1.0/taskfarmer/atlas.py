import math
import sys
import os.path

from . import task

try:
    import ROOT
except:
    ROOT=None

class TransformTaskList(task.ListTaskList):
    """
    Run an ATLAS transform on input ROOT files.

    See the :code:`__init__` function on details how to configure this tasklist 
    handler. A simple example for running no pileup digitization is below.

    .. code-block:: ini

        [digi]
        TaskList = taskfarmer.atlas.TransformTaskList
        transform = Reco_tf.py
        input = HITS
        output = RDO
        autoConfiguration = everything
        digiSteeringConf = StandardInTimeOnlyTruth
        conditionsTag = default:OFLCOND-MC16-SDR-RUN2-06
        geometryVersion = default:ATLAS-R2-2016-01-00-01
        postInclude = default:PyJobTransforms/UseFrontier.py
        preInclude = HITtoRDO:Campaigns/MC16NoPileUp.py
        preExec = all:from ParticleBuilderOptions.AODFlags import AODFlags; AODFlags.ThinGeantTruth.set_Value_and_Lock(False);' 'HITtoRDO:from Digitization.DigitizationFlags import digitizationFlags; digitizationFlags.OldBeamSpotZSize = 42

    The :code:`TransformTaskList` supports splitting each input file into
    multiple tasks, based on a maximum number of events. However, when
    practical, it is recommeded to use AthenaMP for parallelizing event
    processing. This has a reduced memory footprint. AthenaMP can enabled by
    including the following in your tasklist handler defintion.

    .. code-block:: ini

        athenaopt = all:--nprocs=64

    or by setting the :code:`ATHENA_PROC_NUMBER` environmental variable.

    The transform output is stored in the current working directory. It is then
    copied to the `workdir` using rsync. This two stage process is required due
    to how AthenaMP determines its temporary outputs. The implication is that
    the runner needs to run the command using bash.
    """

    def __init__(self, path, workdir, transform, input, output, maxEventsPerJob=None, **kwargs):
        """
        The `kwargs` are interpreted as arguments to the transform command. For
        example, having an kwarg of
        :code:`kwargs['postInclude']="HITtoRDO:Campaigns/MC16NoPileUp.py"`
        translates into a transform argument of
        :code:`--postInclude='HITtoRDO:Campaigns/MC16NoPileUp.py'`. Note the
        automatic wrapping of the value string inside singlue quotes. These are
        automatically by the added by this tasklist handler.

        Parameters
        ----------
        path : str
            Path to tasklist
        workdir : str
            Path to work directory
        transform : str
            Name of transform (ie: :code:`Sim_tf.py`)
        input : str
            Type of input file (ie: :code:`EVNT`)
        output : str
            Type of output file (ie: :code:`HITS`)
        maxEventsPerJob : str, optional
            Maximum number of events per task
        kwargs
            Arguments passed to athena as :code:`--key='value'`.
        """
        super().__init__(path, workdir)

        if maxEventsPerJob is not None:
            maxEventsPerJob=float(maxEventsPerJob)

        # Input/output configuration
        self.input=input
        self.output=output
        self.outdir=os.path.realpath(f'{workdir}/output')
        self.lock()
        if not os.path.exists(self.outdir):
            os.mkdir(self.outdir)
        self.unlock()

        # Build up command string
        self.cmd = []
        self.cmd.append(transform)
        for opt,val in kwargs.items():
            self.cmd.append(f"--{opt} '{val}'")

        # Build a list of tasks
        filelist=list(self.tasks)
        self.tasks=[]
        fileid=0
        for infile in filelist:
            # Inputs and outputs
            taskid=fileid
            outfile=f'{self.output}.{taskid}.root'
            task={
                f'input{input}File':infile,
                f'output{self.output}File':outfile
            }

            #Split events
            if maxEventsPerJob==None:
                self.tasks.append(self.buildcommand(**task))
            else:
                if ROOT==None:
                    raise Exception('Need PyROOT for input splitting!')

                # Count number of events
                fh=ROOT.TFile.Open(infile)
                nevents=fh.Get('CollectionTree').GetEntries()

                # Split
                for i in range(int(math.ceil(nevents/maxEventsPerJob))):
                    outfile=f'{self.output}.{fileid}.{i}.root'
                    task[f'output{self.output}File']=outfile
                    task['skipEvents']=int(i*maxEventsPerJob)
                    task['maxEvents' ]=int(  maxEventsPerJob)
                    self.tasks.append(self.buildcommand(**task))
            fileid+=1

    def buildcommand(self,**kwargs):
        """ Build task command using hander configuration and per-task settings in `kwargs`. """
        # Build the transform command
        cmd=self.cmd.copy()
        cmd+=list(map(lambda opt: f'--{opt[0]} {opt[1]}', kwargs.items()))

        # Copy the result on success
        cmd.append('&&')
        cmd.append('rsync')
        cmd.append('-avr')
        cmd.append(kwargs[f'output{self.output}File'])
        cmd.append(self.outdir)

        return ' '.join(cmd)

class AthenaTaskList(task.ListTaskList):
    """
    Run an athena job on input ROOT files.

    See the :code:`__init__` function on details how to configure this tasklist 
    handler. A simple example for running no pileup digitization is below.

    .. code-block: ini

        [valid]
        TaskList = taskfarmer.atlas.AthenaTaskList
        jobOptions = InDetPhysValMonitoring/InDetPhysValMonitoring_topOptions.py
        output = M_output.root
        command = from InDetPhysValMonitoring.InDetPhysValJobProperties import InDetPhysValFlags; InDetPhysValFlags.doValidateTruthToRecoNtuple.set_Value_and_Lock(True)

    The job options need to use the built-in athena support for input files
    (ie: :code:`--filesInput`).

    The :code:`AthenaTaskList` supports splitting each input file into multiple
    tasks, based on a maximum number of events. However, when practical, it is
    recommeded to use AthenaMP for parallelizing event processing. This has a
    reduced memory footprint. AthenaMP can enabled by including the following in
    your tasklist handler defintion.

    .. code-block:: ini

        nprocs = 64

    or by setting the :code:`ATHENA_PROC_NUMBER` environmental variable.

    The output file name is set as the :code:`output` setting. The handler looks
    for it in the current working directory and then copies it to the `workdir`
    using rsync. This two stage process is required due to how AthenaMP
    determines its temporary outputs. The implication is that the runner needs
    to run the command using bash.
    """
    def __init__(self, path, workdir, jobOptions, output, maxEventsPerJob=None, **kwargs):
        """
        The `kwargs` are interpreted as arguments the the athena command. For
        :code:`kwargs['postInclude']="HITtoRDO:Campaigns/MC16NoPileUp.py"`
        translates into an athena argument of
        :code:`--postInclude='HITtoRDO:Campaigns/MC16NoPileUp.py'`. Note the
        automatic wrapping of the value string inside singlue quotes. These are
        automatically added by this tasklist handler.

        Parameters
        ----------
        path : str
            Path to tasklist.
        workdir : str
            Path to work directory.
        jobOptions : str
            Name of jobOptions file to execute.
        output : str
            Expected name of output file.
        maxEventsPerJob : str, optional
            Maximum number of events per task.
        kwargs
            Arguments passed to athena as :code:`--key='value'`.
        """
        super().__init__(path, workdir)

        if maxEventsPerJob is not None:
            maxEventsPerJob=float(maxEventsPerJob)

        # Input/output configuration
        self.outdir=os.path.realpath(f'{workdir}/output')
        self.lock()
        if not os.path.exists(self.outdir):
            os.mkdir(self.outdir)
        self.unlock()

        # Save arguments
        self.args = kwargs
        self.jobOptions = jobOptions
        self.output = output

        # Build a list of tasks
        filelist=list(self.tasks)
        self.tasks=[]
        fileid=0
        for infile in filelist:
            # Inputs and outputs
            taskid=fileid
            task={
                f'filesInput':infile
            }

            #Split events
            if maxEventsPerJob==None:
                taskid=len(self.tasks)
                self.tasks.append(self.buildcommand(taskid, **task))
            else:
                if ROOT==None:
                    raise Exception('Need PyROOT for input splitting!')

                # Count number of events
                fh=ROOT.TFile.Open(infile)
                nevents=fh.Get('CollectionTree').GetEntries()

                # Split
                for i in range(int(math.ceil(nevents/maxEventsPerJob))):
                    task['skipEvents']=int(i*maxEventsPerJob)
                    task['evtMax'    ]=int(  maxEventsPerJob)
                    taskid=len(self.tasks)
                    self.tasks.append(self.buildcommand(taskid,**task))
            fileid+=1

    def buildcommand(self,taskid,**kwargs):
        """ Build task command using hander configuration and per-task settings in :code:`kwargs`

        The :code:`taskid` value is used to determine the unique output filename for the given
        task as :code:`{outdir}/{output}.{taskid}`.
        """
        # Build the athena command
        cmd=['athena.py']
        for opt,val in self.args.items():
            cmd.append(f"--{opt} '{val}'")
        cmd+=list(map(lambda opt: f'--{opt[0]} {opt[1]}', kwargs.items()))
        cmd.append(self.jobOptions)

        # Copy the result on success
        cmd.append('&&')
        cmd.append('rsync')
        cmd.append('-avr')
        cmd.append(self.output)
        cmd.append(f'{self.outdir}/{self.output}.{taskid}')

        return ' '.join(cmd)
