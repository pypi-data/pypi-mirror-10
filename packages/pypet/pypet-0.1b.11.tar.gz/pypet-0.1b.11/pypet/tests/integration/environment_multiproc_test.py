__author__ = 'Robert Meyer'

import logging
import random
import os

from pypet import pypetconstants
from pypet.environment import Environment
from pypet.tests.integration.environment_test import EnvironmentTest, ResultSortTest,\
    TestOtherHDF5Settings2
from pypet.tests.testutils.ioutils import run_suite,make_temp_dir, make_trajectory_name, \
     parse_args, get_log_config, unittest
from pypet.tests.testutils.data import create_param_dict, add_params
import pypet.compat as compat
import sys

try:
    import psutil
except ImportError:
    psutil = None


class MultiprocPoolQueueTest(TestOtherHDF5Settings2):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'queue', 'pool'

    def set_mode(self):
        super(MultiprocPoolQueueTest, self).set_mode()
        self.mode = pypetconstants.WRAP_MODE_QUEUE
        self.multiproc = True
        self.ncores = 4
        self.use_pool=True


class MultiprocPoolLockTest(EnvironmentTest):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'lock', 'pool',

    # def test_run(self):
    #     super(MultiprocLockTest, self).test_run()

    def set_mode(self):
        super(MultiprocPoolLockTest, self).set_mode()
        self.mode = pypetconstants.WRAP_MODE_LOCK
        self.multiproc = True
        self.ncores = 4
        self.use_pool=True


class MultiprocPoolSortQueueTest(ResultSortTest):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'queue', 'pool',

    def set_mode(self):
        super(MultiprocPoolSortQueueTest, self).set_mode()
        self.mode = pypetconstants.WRAP_MODE_QUEUE
        self.multiproc = True
        self.ncores = 3
        self.use_pool=True


class MultiprocPoolSortLockTest(ResultSortTest):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'lock', 'pool',

    def set_mode(self):
        super(MultiprocPoolSortLockTest, self).set_mode()
        self.mode = pypetconstants.WRAP_MODE_LOCK
        self.multiproc = True
        self.ncores = 4
        self.use_pool=True


class MultiprocNoPoolQueueTest(EnvironmentTest):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'queue', 'nopool',

    def set_mode(self):
        super(MultiprocNoPoolQueueTest, self).set_mode()
        self.mode = pypetconstants.WRAP_MODE_QUEUE
        self.multiproc = True
        self.ncores = 3
        self.use_pool=False


class MultiprocNoPoolLockTest(EnvironmentTest):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'lock', 'nopool',

    def set_mode(self):
        super(MultiprocNoPoolLockTest, self).set_mode()
        self.mode = pypetconstants.WRAP_MODE_LOCK
        self.multiproc = True
        self.ncores = 2
        self.use_pool=False


class MultiprocNoPoolSortQueueTest(ResultSortTest):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'queue', 'nopool',

    def set_mode(self):
        super(MultiprocNoPoolSortQueueTest, self).set_mode()
        self.mode = pypetconstants.WRAP_MODE_QUEUE
        self.multiproc = True
        self.ncores = 3
        self.use_pool=False


class MultiprocNoPoolSortLockTest(ResultSortTest):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'lock', 'nopool',

    def set_mode(self):
        super(MultiprocNoPoolSortLockTest, self).set_mode()
        self.mode = pypetconstants.WRAP_MODE_LOCK
        self.multiproc = True
        self.ncores = 3
        self.use_pool=False

class MultiprocFrozenPoolQueueTest(TestOtherHDF5Settings2):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'queue', 'pool', 'freeze_input'

    def set_mode(self):
        super(MultiprocFrozenPoolQueueTest, self).set_mode()
        self.mode = pypetconstants.WRAP_MODE_QUEUE
        self.multiproc = True
        self.freeze_pool_input = True
        self.ncores = 4
        self.use_pool=True


class MultiprocFrozenPoolLockTest(EnvironmentTest):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'lock', 'pool', 'freeze_input'

    # def test_run(self):
    #     super(MultiprocLockTest, self).test_run()

    def set_mode(self):
        super(MultiprocFrozenPoolLockTest, self).set_mode()
        self.mode = pypetconstants.WRAP_MODE_LOCK
        self.multiproc = True
        self.freeze_pool_input = True
        self.ncores = 4
        self.use_pool=True


class MultiprocFrozenPoolSortQueueTest(ResultSortTest):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'queue', 'pool', 'freeze_input'

    def set_mode(self):
        super(MultiprocFrozenPoolSortQueueTest, self).set_mode()
        self.mode = pypetconstants.WRAP_MODE_QUEUE
        self.multiproc = True
        self.freeze_pool_input = True
        self.ncores = 3
        self.use_pool=True


class MultiprocFrozenPoolSortLockTest(ResultSortTest):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'lock', 'pool', 'freeze_input'

    def set_mode(self):
        super(MultiprocFrozenPoolSortLockTest, self).set_mode()
        self.mode = pypetconstants.WRAP_MODE_LOCK
        self.freeze_pool_input = True
        self.multiproc = True
        self.ncores = 4
        self.use_pool=True


@unittest.skipIf(psutil is None, 'Only makes sense if psutil is installed')
class CapTest(EnvironmentTest):

    tags = 'integration', 'hdf5', 'environment', 'multiproc', 'lock', 'nopool', 'cap'

    cap_count = 0

    def setUp(self):

        self.multiproc = True
        self.mode = 'LOCK'

        self.trajname = make_trajectory_name(self)

        self.filename = make_temp_dir(os.path.join('experiments',
                                                    'tests',
                                                    'HDF5',
                                                    '%s.hdf5' % self.trajname))
        self.logfolder = make_temp_dir(os.path.join('experiments','tests','Log'))

        random.seed()

        cap_dicts = (dict(cpu_cap=0.000001), # Ensure that these are triggered
                      dict(memory_cap=(0.000001, 150.0)),
                      dict(swap_cap=0.000001,))

        cap_dict = cap_dicts[CapTest.cap_count]
        env = Environment(trajectory=self.trajname,filename=self.filename,
                          file_title=self.trajname, log_folder=self.logfolder,
                          logger_names=('pypet', 'test'), log_levels='ERROR',
                          log_stdout=False,
                          results_per_run=5,
                          derived_parameters_per_run=5,
                          multiproc=True,
                          ncores=4,
                          use_pool=False,
                          **cap_dict)

        logging.getLogger('test').error('Using Cap: %s' % str(cap_dict))
        # Loop through all possible cap configurations
        # and test one at a time
        CapTest.cap_count += 1
        CapTest.cap_count = CapTest.cap_count % len(cap_dicts)

        traj = env.v_trajectory

        ## Create some parameters
        self.param_dict={}
        create_param_dict(self.param_dict)
        ### Add some parameter:
        add_params(traj,self.param_dict)

        #remember the trajectory and the environment
        self.traj = traj
        self.env = env


if __name__ == '__main__':
    opt_args = parse_args()
    run_suite(**opt_args)