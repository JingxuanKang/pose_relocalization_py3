# pose_relocalization_py3
Fork from https://github.com/nqanh/pose_relocalization
Fixes to old version code
### Requirements
- python=2.7
- tensorflow-gpu=1.15.0
- Keras 2.0.3
- more details in environment.yaml
- note: Do not use 30series GPU(Some unknown errors)
### Dataset
- create dataset in dataset/ as pickle file
- the data in the pickle is a tuple, 
- tuple[0] are the images, the shape is [number_of_images,224,224,3]
- tuple[1] are the posesm the shape is [number_of_images,7] 

### Run train script:
- `cd main_keras`
- `python train.py --gpu GPU_ID ` 
- For example: `python train.py --gpu 0 `     
- --> will train on GPU 0 
- The parameters of the original repository are for the original version. Here write the required paths directly to the file.

### Predict & evaluate
- `cd main_keras`
- `python predict.py`
- Change **in_scene_id**, **in_net_id**, **in_model_file_name** in this file for different scene

### Fix error
Instead of calling the read pickle method in dota_io_cnn.py, the pickle read is used directly in the train. (Unknown error)

_tkinter.TclError: no display name and no $DISPLAY environment variable
import matplotlib
matplotlib.use('Agg')
before import matplotlib.pyplot as plt



If you find this code useful in your research, please consider citing:

	@article{nguyen6dof_lstmpose,
	  author    = {Anh Nguyen and
				   Thanh{-}Toan Do and
				   Darwin G. Caldwell and
				   Nikos G. Tsagarakis},
	  title     = {Real-Time Pose Estimation for Event Cameras with Stacked Spatial {LSTM}
				   Networks},
	  journal   = {IEEE Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)},
	  year      = {2019}
	 }
