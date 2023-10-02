# Loop refinement of an existing model
from modeller import *
from modeller.automodel import *
#from modeller import soap_loop

log.verbose()
env = environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '/home/snehab/Work/modeller']

# Create a new class based on 'loopmodel' so that we can redefine
# select_loop_atoms (necessary)
class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        # One loop from residue 19 to 28 inclusive
        return selection(self.residue_range('321:A', '332:A'),
                         self.residue_range('321:C', '321:C'))
                         #self.residue_range('389:C', '406:C'),
                         #self.residue_range('96:D', '111:D'))
        # Two loops simultaneously
        #return selection(self.residue_range('19:', '28:'),
        #                 self.residue_range('38:', '42:'))

m = MyLoop(env,
           inimodel='/home/snehab/Desktop/model_out2.pdb',   # initial model of the target
           sequence='5uht',                 # code of the target
           loop_assess_methods=assess.DOPE) # assess loops with DOPE
#          loop_assess_methods=soap_loop.Scorer()) # assess with SOAP-Loop

m.loop.starting_model= 1           # index of the first loop model
m.loop.ending_model  = 10           # index of the last loop model
m.loop.md_level = refine.very_fast  # loop refinement method

m.make()
