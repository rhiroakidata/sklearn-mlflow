from models.prediction import TreeModel
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--max-depth', nargs='+')
parser.add_argument('--max-leaf-nodes')
parser.add_argument('--model-name')
args = vars(parser.parse_args())

max_depths = args['max_depth']
max_leaf_nodes = args['max_leaf_nodes']
model_name = args['model_name']

#max_depths = [5, 8, 10]
if __name__ == '__main__':
    for n in max_depths:
        params = {"max_depth": int(n), "random_state": 42}
        dtc = TreeModel.create_instance(**params)
        exp_id, run_id = dtc.mlflow_run()
        print(f"MLflow Run completed with run_id {exp_id} and experiment_id {run_id}")
        print("<->" * 40)