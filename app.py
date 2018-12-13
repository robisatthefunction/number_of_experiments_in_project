import requests, argparse

#get number of experiments in project
def number_of_experiments():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_id", help="paste the project ID as the first argument")
    parser.add_argument("token", help="paste your Optimizely v2 REST API token as the second argument")
    args = parser.parse_args()
    project_id = args.project_id
    token = args.token

    experiment_list = requests.get("https://api.optimizely.com/v2/experiments?project_id=%s" % project_id, headers={'Authorization': 'Bearer %s' % token})

    if experiment_list.status_code == 200:
        number_of_experiments = 0
        for exp in experiment_list.json():
            number_of_experiments += 1
        print(number_of_experiments)

number_of_experiments()
