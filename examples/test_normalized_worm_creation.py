# -*- coding: utf-8 -*-
"""
Show how to go from a basic worm to a NormalizedWorm

i.e. NormalizedWorm.from_basicWorm_factory

We then load a pre-calculated NormalizedWorm and verify that 
they are the same:

i.e. nw == nw_calculated

"""
import sys, os
import matplotlib.pyplot as plt

sys.path.append('..')

from movement_validation import user_config, config, utils
from movement_validation import BasicWorm, NormalizedWorm
from movement_validation import VideoInfo, WormFeatures
from movement_validation import FeatureProcessingOptions

def main():
    # Load from file a normalized worm, as calculated by Schafer Lab code
    base_path = os.path.abspath(user_config.EXAMPLE_DATA_PATH)
    schafer_nw_file_path = os.path.join(base_path, 
                                     "example_video_norm_worm.mat")
    nw = NormalizedWorm.from_schafer_file_factory(schafer_nw_file_path)

    # Load from file some non-normalized contour data, from a file we know
    # to have been generated by the same Schafer code that created the above
    # normalized worm.  This file was generated earlier in the code though,
    # and contains more "primitive", non-normalized contour and skeleton data
    schafer_bw_file_path = os.path.join(base_path, 
                                     "example_contour_and_skeleton_info.mat")  
    bw = BasicWorm.from_schafer_file_factory(schafer_bw_file_path)

    bw_from_nw = nw.get_BasicWorm()

    # Calculate a NormalizedWorm from the basic worm information.
    print("Now let's calculate nw from bw_from_nw")    
    nw_calculated = NormalizedWorm.from_BasicWorm_factory(bw_from_nw)

    # Compare our generated normalized worm `nw2` with the pre-loaded 
    # Schafer Lab normalized worm, `nw`.  Validate they are the same.
    nw == nw_calculated
    
    # Compare lengths
    plt.plot(nw.length, c='red')
    plt.plot(nw_calculated.length, c='blue')
    plt.show()
    
    # EXTRAS (nothing to do with NormalizedWorm creation:)
    # The frame rate is somewhere in the video info. Ideally this would 
    # all come from the video parser eventually
    fpo = FeatureProcessingOptions(config.DEFAULT_FPS)

    # Generate the OpenWorm movement validation repo version of the features
    wf = WormFeatures(nw_calculated, fpo)
    
    # Display how long it took to generate each of the features
    wf.timer.summarize()
    

if __name__ == '__main__':
    start_time = utils.timing_function()
    main()
    print("Time elapsed: %.2fs" % 
          (utils.timing_function() - start_time))
    
