import argparse
import yaml



if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()
    
    print("Stage: EVALUATE")

    # Load main config (params.yaml)
    with open(args.config) as fd:
        params = yaml.safe_load(fd)
    

    print(f"INFO:  Running mode:     {params['run_mode']}")
    print(f"INFO:  Use stage config: {args.config}")
    print(f"INFO:  Evaluate params:  {params['evaluate']}")
