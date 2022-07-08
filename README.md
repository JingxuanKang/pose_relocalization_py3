# pose_relocalization_py3
Fork from https://github.com/nqanh/pose_relocalization
Fixes to old version code
### Requirements
- python=3.6.13
- tensorflow-gpu=1.15.0
- Keras 2.0.3
- more details in environment.yaml
- note: Do not use 30series GPU(Some unknown errors)
### Download dataset
- create dataset 

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
