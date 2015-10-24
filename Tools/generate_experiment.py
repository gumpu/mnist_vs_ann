import os
import stat

#=============================================================================

class Configuration():

config_template = """
# example configure file for mnist
# training iterator
data = train
iter = mnist
    path_img   = "./../Raw/train-images-idx3-ubyte.gz"
    path_label = "./../Raw/train-labels-idx1-ubyte.gz"
    shuffle = 1
iter = end
# evaluation iterator
eval = test
iter = mnist
    path_img   = "./../Raw/t10k-images-idx3-ubyte.gz"
    path_label = "./../Raw/t10k-labels-idx1-ubyte.gz"
iter = end

netconfig=start
layer[0->1] = fullc:fc1
  nhidden = 100
  init_sigma = 0.01
layer[1->2] = sigmoid:se1
layer[2->3] = fullc:fc1
  nhidden = 10
  init_sigma = 0.01
layer[3->3] = softmax
netconfig=end

# input shape not including batch
input_shape = 1,1,784
batch_size = 100

## global parameters
dev = cpu
save_model = 1
max_round = 15
num_round = 15
train_eval = 1
random_type = gaussian
## learning parameters
eta = 0.1
momentum = 0.9
wd  = 0.0
# evaluation metric
metric = error
# end of config
"""

test_template = """
## Data iterator setting
pred = results/pred{:04d}.txt
iter = mnist
    path_img   = "./../Raw/t10k-images-idx3-ubyte.gz"
    path_label = "./../Raw/t10k-labels-idx1-ubyte.gz"
iter = end
# Global Setting
task = pred
model_in = ./models/{:04d}.model
"""

    def __init__(self):
        pass

    def write_train(self, outpf):
        outpf.write(config_template)

    def write_test(self, outpf, model_number):
        outpf.write(config_template)
        test_config = test_template.format(model_number, model_number)
        outpf.write(test_config)

#=============================================================================
class Experiment():

    def __init__(self, name):
        self.name = name

    def generate(self):
        """Generate the directories and configuration files
        for a single experiment."""

        experiment_directory = self.name
        print(experiment_directory)
        train_config_name = os.path.join(experiment_directory, "train.conf")
        run_script_name   = os.path.join(experiment_directory, "run.sh")

        model_directory   = os.path.join(experiment_directory, "models")
        result_directory  = os.path.join(experiment_directory, "results")
        if not os.path.exists(model_directory):
            os.makedirs(model_directory)
        if not os.path.exists(result_directory):
            os.makedirs(result_directory)

        c = Configuration()
        with open(train_config_name, "w") as outpf:
            c.write_train(outpf)
        for n in range(1, 16):
            test_config_name  = os.path.join(
                    experiment_directory, "test{:04d}.conf".format(n))
            with open(test_config_name, "w") as outpf:
                c.write_test(outpf, n)

        with open(run_script_name, "w") as outpf:
            outpf.write("cxxnet train.conf\n")
            for n in range(1, 16):
                outpf.write("cxxnet test{:04d}.conf\n".format(n))

        st = os.stat(run_script_name)
        os.chmod(run_script_name, st.st_mode | stat.S_IEXEC)

    def create(self):
        pass

#=============================================================================

if __name__ == "__main__":
    experiment = Experiment("ExperimentTest")
    experiment.generate()

