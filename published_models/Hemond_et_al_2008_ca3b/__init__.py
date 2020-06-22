# Added by Sara Saray to run validation tests and register the results in the HBP Validation Framework

from __future__ import print_function
import os
from hippounit.utils import ModelLoader

class Hemond_2008_fig9b(ModelLoader):
    # model on HBP Model Catalog

    model_version = "fig9b"

    def __init__(self):
        # path to mod files
        model_path = os.path.dirname(os.path.abspath(__file__))
        print("model_path = ", model_path)
        mod_files_path = model_path + "/"

        #Load cell model
        ModelLoader.__init__(self, mod_files_path = mod_files_path)

        # outputs will be saved in subfolders named like this:
        self.name="Hemond_2008_fig9b"

        # path to hoc file
        # the model must not display any GUI!!
        self.hocpath = model_path + "/main_model_fig9b.hoc"


        # If the hoc file doesn't contain a template, this must be None (the default value is None)
        self.template_name = None

        # model.SomaSecList_name should be None, if there is no Section List in the model for the soma, or if the name of the soma section is given by setting model.soma (the default value is None)
        self.SomaSecList_name = None
        # if the soma is not in a section list or to use a specific somatic section, add its name here:
        self.soma = 'soma[0]'

        # For Back-propagating AP Test a section list containing the trunk sections is needed
        self.TrunkSecList_name = 'trunk'
        self.BasalSecList_name = 'basal'

        #These will be argument to those tests, where dendritic locatins are selected according to distances.
        # If not set, the end (1 point) of the above given soma section will be used as reference point for distance determination of apical dendrites,
        #The beginning (0 point) of it for basal dendrites (and axons)

        self.trunk_origin = ['soma[0]', 1] 
        self.basal_origin = ['soma[0]', 1]

        # It is important to set the v_init and the celsius parameters of the simulations here,
        # as if they are only set in the model's files, they will be overwritten with the default values of the ModelLoader class.
        # default values: v_init = -70, celsius = 34 
        self.v_init = -64
        self.celsius = 35

        # It is possible to run the simulations using variable time step (default for this is False)
        self.cvode_active = True


class Hemond_2008_fig9c(ModelLoader):
    # model on HBP Model Catalog

    model_version = "fig9c"

    def __init__(self):
        # path to mod files
        model_path = os.path.dirname(os.path.abspath(__file__))
        print("model_path = ", model_path)
        mod_files_path = model_path + "/"

        #Load cell model
        ModelLoader.__init__(self, mod_files_path = mod_files_path)

        # outputs will be saved in subfolders named like this:
        self.name="Hemond_2008_fig9c"

        # path to hoc file
        # the model must not display any GUI!!
        self.hocpath = model_path + "/main_model_fig9c.hoc"


        # If the hoc file doesn't contain a template, this must be None (the default value is None)
        self.template_name = None

        # model.SomaSecList_name should be None, if there is no Section List in the model for the soma, or if the name of the soma section is given by setting model.soma (the default value is None)
        self.SomaSecList_name = None
        # if the soma is not in a section list or to use a specific somatic section, add its name here:
        self.soma = 'soma[0]'

        # For Back-propagating AP Test a section list containing the trunk sections is needed
        self.TrunkSecList_name = 'trunk'
        self.BasalSecList_name = 'basal'

        #These will be argument to those tests, where dendritic locatins are selected according to distances.
        # If not set, the end (1 point) of the above given soma section will be used as reference point for distance determination of apical dendrites,
        #The beginning (0 point) of it for basal dendrites (and axons)

        self.trunk_origin = ['soma[0]', 1] 
        self.basal_origin = ['soma[0]', 1]

        # It is important to set the v_init and the celsius parameters of the simulations here,
        # as if they are only set in the model's files, they will be overwritten with the default values of the ModelLoader class.
        # default values: v_init = -70, celsius = 34 
        self.v_init = -64
        self.celsius = 35

        # It is possible to run the simulations using variable time step (default for this is False)
        self.cvode_active = True

class Hemond_2008_fig9d(ModelLoader):
    # model on HBP Model Catalog

    model_version = "fig9d"

    def __init__(self):
        # path to mod files
        model_path = os.path.dirname(os.path.abspath(__file__))
        print("model_path = ", model_path)
        mod_files_path = model_path + "/"

        #Load cell model
        ModelLoader.__init__(self, mod_files_path = mod_files_path)

        # outputs will be saved in subfolders named like this:
        self.name="Hemond_2008_fig9d"

        # path to hoc file
        # the model must not display any GUI!!
        self.hocpath = model_path + "/main_model_fig9d.hoc"


        # If the hoc file doesn't contain a template, this must be None (the default value is None)
        self.template_name = None

        # model.SomaSecList_name should be None, if there is no Section List in the model for the soma, or if the name of the soma section is given by setting model.soma (the default value is None)
        self.SomaSecList_name = None
        # if the soma is not in a section list or to use a specific somatic section, add its name here:
        self.soma = 'soma[0]'

        # For Back-propagating AP Test a section list containing the trunk sections is needed
        self.TrunkSecList_name = 'trunk'
        self.BasalSecList_name = 'basal'

        #These will be argument to those tests, where dendritic locatins are selected according to distances.
        # If not set, the end (1 point) of the above given soma section will be used as reference point for distance determination of apical dendrites,
        #The beginning (0 point) of it for basal dendrites (and axons)

        self.trunk_origin = ['soma[0]', 1] 
        self.basal_origin = ['soma[0]', 1]

        # It is important to set the v_init and the celsius parameters of the simulations here,
        # as if they are only set in the model's files, they will be overwritten with the default values of the ModelLoader class.
        # default values: v_init = -70, celsius = 34 
        self.v_init = -64
        self.celsius = 35

        # It is possible to run the simulations using variable time step (default for this is False)
        self.cvode_active = True


class Hemond_2008_fig9e(ModelLoader):
    # model on HBP Model Catalog

    model_version = "fig9e"

    def __init__(self):
        # path to mod files
        model_path = os.path.dirname(os.path.abspath(__file__))
        print("model_path = ", model_path)
        mod_files_path = model_path + "/"

        #Load cell model
        ModelLoader.__init__(self, mod_files_path = mod_files_path)

        # outputs will be saved in subfolders named like this:
        self.name="Hemond_2008_fig9e"

        # path to hoc file
        # the model must not display any GUI!!
        self.hocpath = model_path + "/main_model_fig9e.hoc"


        # If the hoc file doesn't contain a template, this must be None (the default value is None)
        self.template_name = None

        # model.SomaSecList_name should be None, if there is no Section List in the model for the soma, or if the name of the soma section is given by setting model.soma (the default value is None)
        self.SomaSecList_name = None
        # if the soma is not in a section list or to use a specific somatic section, add its name here:
        self.soma = 'soma[0]'

        # For Back-propagating AP Test a section list containing the trunk sections is needed
        self.TrunkSecList_name = 'trunk'
        self.BasalSecList_name = 'basal'

        #These will be argument to those tests, where dendritic locatins are selected according to distances.
        # If not set, the end (1 point) of the above given soma section will be used as reference point for distance determination of apical dendrites,
        #The beginning (0 point) of it for basal dendrites (and axons)

        self.trunk_origin = ['soma[0]', 1] 
        self.basal_origin = ['soma[0]', 1]

        # It is important to set the v_init and the celsius parameters of the simulations here,
        # as if they are only set in the model's files, they will be overwritten with the default values of the ModelLoader class.
        # default values: v_init = -70, celsius = 34 
        self.v_init = -64
        self.celsius = 35

        # It is possible to run the simulations using variable time step (default for this is False)
        self.cvode_active = True
