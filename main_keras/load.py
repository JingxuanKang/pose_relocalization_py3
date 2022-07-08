import os
import pickle
cwd = os.getcwd()
split_id = 'img_pose_all_novel_split'
scene_id='shapes_6dof'
root_path = os.path.abspath(os.path.join(cwd, os.pardir))
dataset_folder = os.path.join(root_path, 'event_data', 'processed' )
data_path = os.path.join(dataset_folder, scene_id, split_id, 'percentage_pkl', '100')
print(data_path)
X,Y=pickle.load(open(os.path.join('/home/jingxuankang/6Dpose/pose_relocalization/event_data/processed/shapes_6dof/img_pose_all_novel_split/percentage_pkl/100', 'train.pkl'), 'rb'))
print(X)