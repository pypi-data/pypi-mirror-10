""" Submodule with Illumina-related code
"""
import logging
import os

from datetime import datetime
from xml.etree import ElementTree as ET

from taca.utils import misc
from taca.utils.config import CONFIG
from taca.utils.filesystem import chdir

logger = logging.getLogger(__name__)

def demultiplex_HiSeq(run):
    """ Demultiplexing for HiSeq (V3/V4) runs
    """
    raise NotImplementedError('Meec! Demultiplexing for HiSeq (V3/V4) runs not implemented yet :-/')


def demultiplex_MiSeq(run):
    """ Demultiplexing for MiSeq runs
    """
    raise NotImplementedError('Meec! Demultiplexing for MiSeq runs not implemented yet :-/')


class Run(object):
    """ Defines an Illumina run
    """
    def __init__(self, run_dir):
        if not os.path.exists(run_dir) or not \
                os.path.exists(os.path.join(run_dir, 'runParameters.xml')):
            raise RuntimeError('Could not locate run directory {}'.format(run_dir))
        self.run_dir = run_dir
        self.id = os.path.basename(run_dir)
        self._extract_run_info()


    def _extract_run_info(self):
        """ Extracts run info from runParameters.xml and adds it to the class attributes

        TODO: This method could be used to extract A LOT of information about the
        run and maybe... populate statusdb or similar? Just leaving this comment here
        till now...
        """

        run_parameters = ET.parse(os.path.join(self.run_dir, 'runParameters.xml')).getroot().find('Setup')
        # HiSeq and HiSeq X runParameter.xml files will have a Flowcell child with run type info
        run_type = run_parameters.find('Flowcell')
        # But MiSeqs doesn't...
        if run_type is None:
            run_type = run_parameters.find('ApplicationName')

        try:
            if 'HiSeq X' in run_type.text:
                self.run_type = 'HiSeqX'
            elif 'HiSeq Flow Cell' in run_type.text:
                self.run_type = 'HiSeq'
            elif 'MiSeq' in run_type.text:
                self.run_type = 'MiSeq'
        except AttributeError:
            raise RuntimeError('Run type could not be determined for run {}'.format(self.id))


    def is_finished(self):
        """ Returns true if the run is finished, false otherwise
        """
        return os.path.exists(os.path.join(self.run_dir, 'RTAComplete.txt'))


    def demultiplex(self):
        """Perform demultiplexing of the flowcell.

        Takes software (bcl2fastq version to use) and parameters from the configuration
        file.
        """
        logger.info('Building bcl2fastq command')
        config = CONFIG['analysis']
        with chdir(self.run_dir):
            cl = [config.get('bcl2fastq').get(self.run_type)]
            if config['bcl2fastq'].has_key('options'):
                cl_options = config['bcl2fastq']['options']

                # Append all options that appear in the configuration file to the main command.
                # Options that require a value, i.e --use-bases-mask Y8,I8,Y8, will be returned
                # as a dictionary, while options that doesn't require a value, i.e --no-lane-splitting
                # will be returned as a simple string
                for option in cl_options:
                    if isinstance(option, dict):
                        opt, val = option.popitem()
                        cl.extend(['--{}'.format(opt), str(val)])
                    else:
                        cl.append('--{}'.format(option))

            logger.info(("BCL to FASTQ conversion and demultiplexing started for "
                         " run {} on {}".format(os.path.basename(self.id), datetime.now())))

            misc.call_external_command_detached(cl, with_log_files=True)



    @property
    def status(self):
        if self.run_type == 'HiSeqX':
            demux_dir = os.path.join(self.run_dir, 'Demultiplexing')
            if not os.path.exists(demux_dir):
                return 'TO_START'
            elif os.path.exists(os.path.join(demux_dir, 'Stats', 'DemultiplexingStats.xml')):
                return 'COMPLETED'
            else:
                return 'IN_PROGRESS'
        else:
            raise NotImplementedError('Sorry... no status method defined for {} runs'.format(self.run_type))
