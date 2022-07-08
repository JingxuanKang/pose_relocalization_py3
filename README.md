# pose_relocalization_py3
Fork from https://github.com/nqanh/pose_relocalization
Fixes to old version code
### Requirements

- tensorflow-gpu
- Keras 2.0.3

### Download dataset
- Download datafrom from: http://rpg.ifi.uzh.ch/davis_data.html 
- Unzip and copy to **/event_data/raw_data** foler 

### Create train/test data
- `cd dataset_script`
- `python CREATE_DATA.py`
- change **list_scene** inside **CREATE_DATA.py** for other scene

### Run train script:
- `cd main_keras`
- `python train.py --gpu GPU_ID --scene SCENCE_ID` 
- For example: `python train.py --gpu 0 --scene shapes_rotation`     --> will train on GPU 0 and shapes_rotation sequence

### Predict & evaluate
- `cd main_keras`
- `python predict.py`
- Change **in_scene_id**, **in_net_id**, **in_model_file_name** in this file for different scene


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
