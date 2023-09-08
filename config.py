from easydict import EasyDict as edict
import torch

drone = edict()
drone.yaw_rate = 90
drone.default_velocity = 5
drone.moving_unit = 0.5

# main
args = edict(drone=drone)

args.device = torch.device(f"cuda" if torch.cuda.is_available() else "cpu")

args.n_classes = 4

args.gamma = 0.9
args.learning_rate = 1e-3
args.epsilon = 0.3 

args.checkpoint = None ## Load chekpoint

args.batch_size = 200 # batch size
args.mem_size = 1000
args.epochs = 5000  
args.max_time = 60  
args.sync_freq = 500

args.eval_freq = 50

args.voxel_threshold = 0.002
args.voxel_size = 0.04

args.model_name = ""