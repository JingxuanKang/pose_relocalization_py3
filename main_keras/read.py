import os 

cwd = os.getcwd()
#print 'current dir: ', cwd
root_path = os.path.abspath(os.path.join(cwd, os.pardir))  # get parent path
#print 'root path: ', root_path  
print(root_path)
main_output = os.path.join(root_path, 'output')
scene_id = 'shapes_6dof'
net_id = 'vgg_lstm2'
split_id = 'img_pose_all_novel_split'
predition = 'prediction'
log_model = 'log_model'
in_model_file_name = 'full_model_epoch_e1000.hdf5'
a=os.path.join(main_output, scene_id, net_id, split_id, predition) 
print(a)
log_model_path = os.path.join(main_output, scene_id, net_id, split_id, log_model)
model_file = os.path.join(log_model_path, in_model_file_name)

print(log_model_path)
print(model_file)