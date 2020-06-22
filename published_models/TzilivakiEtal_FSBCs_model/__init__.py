# Added by Sara Saray to run validation tests on the basket cell models and register the results in the HBP Validation Framework

from __future__ import print_function
import os
from hippounit.utils import ModelLoader

class Tzilivaki_2019_Somogyi_1_morph(ModelLoader):
    # model on HBP Model Catalog

    model_version = "Somogyi_1_morph"

    def __init__(self):
        # path to mod files
        model_path = os.path.dirname(os.path.abspath(__file__))
        print("model_path = ", model_path)
        mod_files_path = model_path + "/Multicompartmental_Biophysical_models/mechanism/"

        #Load cell model
        ModelLoader.__init__(self, mod_files_path = mod_files_path)

        # outputs will be saved in subfolders named like this:
        self.name="Tzilivaki_2019_Somogyi_1_morph"

        # path to hoc file
        # the model must not display any GUI!!
        self.hocpath = model_path + "/Multicompartmental_Biophysical_models/experiment/main_model_Somogyi_1.hoc"


        # If the hoc file doesn't contain a template, this must be None (the default value is None)
        self.template_name = None
        #Template is not loaded directly by HippoUnit, because "current_balanceFS(-68)" has to be called after initializing the template 

        # model.SomaSecList_name should be None, if there is no Section List in the model for the soma, or if the name of the soma section is given by setting model.soma (the default value is None)
        self.SomaSecList_name = None
        # if the soma is not in a section list or to use a specific somatic section, add its name here:
        self.soma = 'FScell[0].soma[0]'

        # For Back-propagating AP Test a section list containing the trunk sections is needed
        # model.TrunkSecList_name = 'trunk'
        self.BasalSecList_name = 'FScell[0].basal_prox'
        self.AxonSecList_name = 'FScell[0].axonal'

        #These will be argument to those tests, where dendritic locatins are selected according to distances.
        # If not set, the end (1 point) of the above given soma section will be used as reference point for distance determination of apical dendrites,
        #The beginning (0 point) of it for basal dendrites and axons

        self.trunk_origin = ['FScell[0].soma[0]', 1] 
        self.basal_origin = ['FScell[0].soma[0]', 1]
        self.axon_origin = ['FScell[0].soma[0]', 1]

        # It is important to set the v_init and the celsius parameters of the simulations here,
        # as if they are only set in the model's files, they will be overwritten with the default values of the ModelLoader class.
        # default values: v_init = -70, celsius = 34 
        self.v_init = -68
        self.dt = 0.1


class Tzilivaki_2019_Somogyi_2_morph(ModelLoader):
    # model on HBP Model Catalog

    model_version = "Somogyi_2_morph"

    def __init__(self):
        # path to mod files
        model_path = os.path.dirname(os.path.abspath(__file__))
        print("model_path = ", model_path)
        mod_files_path = model_path + "/Multicompartmental_Biophysical_models/mechanism/"

        #Load cell model
        ModelLoader.__init__(self, mod_files_path = mod_files_path)

        # outputs will be saved in subfolders named like this:
        self.name="Tzilivaki_2019_Somogyi_2_morph"

        # path to hoc file
        # the model must not display any GUI!!
        self.hocpath = model_path + "/Multicompartmental_Biophysical_models/experiment/main_model_Somogyi_2.hoc"


        # If the hoc file doesn't contain a template, this must be None (the default value is None)
        self.template_name = None
        #Template is not loaded directly by HippoUnit, because "current_balanceFS(-68)" has to be called after initializing the template 

        # model.SomaSecList_name should be None, if there is no Section List in the model for the soma, or if the name of the soma section is given by setting model.soma (the default value is None)
        self.SomaSecList_name = None
        # if the soma is not in a section list or to use a specific somatic section, add its name here:
        self.soma = 'FScell[0].soma[0]'

        # For Back-propagating AP Test a section list containing the trunk sections is needed
        # model.TrunkSecList_name = 'trunk'
        self.BasalSecList_name = 'FScell[0].basal_prox'
        self.AxonSecList_name = 'FScell[0].axonal'

        #These will be argument to those tests, where dendritic locatins are selected according to distances.
        # If not set, the end (1 point) of the above given soma section will be used as reference point for distance determination of apical dendrites,
        #The beginning (0 point) of it for basal dendrites and axons

        self.trunk_origin = ['FScell[0].soma[0]', 1] 
        self.basal_origin = ['FScell[0].soma[0]', 1]
        self.axon_origin = ['FScell[0].soma[0]', 1]

        # It is important to set the v_init and the celsius parameters of the simulations here,
        # as if they are only set in the model's files, they will be overwritten with the default values of the ModelLoader class.
        # default values: v_init = -70, celsius = 34 
        self.v_init = -68
        self.dt = 0.1

class Tzilivaki_2019_Somogyi_3_morph(ModelLoader):
    # model on HBP Model Catalog

    model_version = "Somogyi_3_morph"

    def __init__(self):
        # path to mod files
        model_path = os.path.dirname(os.path.abspath(__file__))
        print("model_path = ", model_path)
        mod_files_path = model_path + "/Multicompartmental_Biophysical_models/mechanism/"

        #Load cell model
        ModelLoader.__init__(self, mod_files_path = mod_files_path)

        # outputs will be saved in subfolders named like this:
        self.name="Tzilivaki_2019_Somogyi_3_morph"

        # path to hoc file
        # the model must not display any GUI!!
        self.hocpath = model_path + "/Multicompartmental_Biophysical_models/experiment/main_model_Somogyi_3.hoc"


        # If the hoc file doesn't contain a template, this must be None (the default value is None)
        self.template_name = None
        #Template is not loaded directly by HippoUnit, because "current_balanceFS(-68)" has to be called after initializing the template 

        # model.SomaSecList_name should be None, if there is no Section List in the model for the soma, or if the name of the soma section is given by setting model.soma (the default value is None)
        self.SomaSecList_name = None
        # if the soma is not in a section list or to use a specific somatic section, add its name here:
        self.soma = 'FScell[0].soma[0]'

        # For Back-propagating AP Test a section list containing the trunk sections is needed
        # model.TrunkSecList_name = 'trunk'
        self.BasalSecList_name = 'FScell[0].basal_prox'
        self.AxonSecList_name = 'FScell[0].axonal'

        #These will be argument to those tests, where dendritic locatins are selected according to distances.
        # If not set, the end (1 point) of the above given soma section will be used as reference point for distance determination of apical dendrites,
        #The beginning (0 point) of it for basal dendrites and axons

        self.trunk_origin = ['FScell[0].soma[0]', 1] 
        self.basal_origin = ['FScell[0].soma[0]', 1]
        self.axon_origin = ['FScell[0].soma[0]', 1]

        # It is important to set the v_init and the celsius parameters of the simulations here,
        # as if they are only set in the model's files, they will be overwritten with the default values of the ModelLoader class.
        # default values: v_init = -70, celsius = 34 
        self.v_init = -68
        self.dt = 0.1

class Tzilivaki_2019_Somogyi_4_morph(ModelLoader):
    # model on HBP Model Catalog

    model_version = "Somogyi_4_morph"

    def __init__(self):
        # path to mod files
        model_path = os.path.dirname(os.path.abspath(__file__))
        print("model_path = ", model_path)
        mod_files_path = model_path + "/Multicompartmental_Biophysical_models/mechanism/"

        #Load cell model
        ModelLoader.__init__(self, mod_files_path = mod_files_path)

        # outputs will be saved in subfolders named like this:
        self.name="Tzilivaki_2019_Somogyi_4_morph"

        # path to hoc file
        # the model must not display any GUI!!
        self.hocpath = model_path + "/Multicompartmental_Biophysical_models/experiment/main_model_Somogyi_4.hoc"


        # If the hoc file doesn't contain a template, this must be None (the default value is None)
        self.template_name = None
        #Template is not loaded directly by HippoUnit, because "current_balanceFS(-68)" has to be called after initializing the template 

        # model.SomaSecList_name should be None, if there is no Section List in the model for the soma, or if the name of the soma section is given by setting model.soma (the default value is None)
        self.SomaSecList_name = None
        # if the soma is not in a section list or to use a specific somatic section, add its name here:
        self.soma = 'FScell[0].soma[0]'

        # For Back-propagating AP Test a section list containing the trunk sections is needed
        # model.TrunkSecList_name = 'trunk'
        self.BasalSecList_name = 'FScell[0].basal_prox'
        self.AxonSecList_name = 'FScell[0].axonal'

        #These will be argument to those tests, where dendritic locatins are selected according to distances.
        # If not set, the end (1 point) of the above given soma section will be used as reference point for distance determination of apical dendrites,
        #The beginning (0 point) of it for basal dendrites and axons

        self.trunk_origin = ['FScell[0].soma[0]', 1] 
        self.basal_origin = ['FScell[0].soma[0]', 1]
        self.axon_origin = ['FScell[0].soma[0]', 1]

        # It is important to set the v_init and the celsius parameters of the simulations here,
        # as if they are only set in the model's files, they will be overwritten with the default values of the ModelLoader class.
        # default values: v_init = -70, celsius = 34 
        self.v_init = -68
        self.dt = 0.1

class Tzilivaki_2019_Somogyi_5_morph(ModelLoader):
    # model on HBP Model Catalog

    model_version = "Somogyi_5_morph"

    def __init__(self):
        # path to mod files
        model_path = os.path.dirname(os.path.abspath(__file__))
        print("model_path = ", model_path)
        mod_files_path = model_path + "/Multicompartmental_Biophysical_models/mechanism/"

        #Load cell model
        ModelLoader.__init__(self, mod_files_path = mod_files_path)

        # outputs will be saved in subfolders named like this:
        self.name="Tzilivaki_2019_Somogyi_5_morph"

        # path to hoc file
        # the model must not display any GUI!!
        self.hocpath = model_path + "/Multicompartmental_Biophysical_models/experiment/main_model_Somogyi_5.hoc"


        # If the hoc file doesn't contain a template, this must be None (the default value is None)
        self.template_name = None
        #Template is not loaded directly by HippoUnit, because "current_balanceFS(-68)" has to be called after initializing the template 

        # model.SomaSecList_name should be None, if there is no Section List in the model for the soma, or if the name of the soma section is given by setting model.soma (the default value is None)
        self.SomaSecList_name = None
        # if the soma is not in a section list or to use a specific somatic section, add its name here:
        self.soma = 'FScell[0].soma[0]'

        # For Back-propagating AP Test a section list containing the trunk sections is needed
        # model.TrunkSecList_name = 'trunk'
        self.BasalSecList_name = 'FScell[0].basal_prox'
        self.AxonSecList_name = 'FScell[0].axonal'

        #These will be argument to those tests, where dendritic locatins are selected according to distances.
        # If not set, the end (1 point) of the above given soma section will be used as reference point for distance determination of apical dendrites,
        #The beginning (0 point) of it for basal dendrites and axons

        self.trunk_origin = ['FScell[0].soma[0]', 1] 
        self.basal_origin = ['FScell[0].soma[0]', 1]
        self.axon_origin = ['FScell[0].soma[0]', 1]

        # It is important to set the v_init and the celsius parameters of the simulations here,
        # as if they are only set in the model's files, they will be overwritten with the default values of the ModelLoader class.
        # default values: v_init = -70, celsius = 34 
        self.v_init = -68
        self.dt = 0.1
