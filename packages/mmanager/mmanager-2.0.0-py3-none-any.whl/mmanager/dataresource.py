import json
import requests
import datetime


def get_model_data(model_data):
    data = {
            "project": model_data['project'],
            "transformerType": model_data['transformerType'],
            "algorithmType": model_data['algorithmType'],
            "target_column": model_data['target_column'],
            "modelFramework": model_data['modelFramework'],
            "datasetinsertionType": model_data['datasetinsertionType'],
            "note": model_data['note'],
            "model_area": model_data['model_area'],
            "model_dependencies": model_data['model_dependencies'],
            "model_usage": model_data['model_usage'],
            "model_adjustment": model_data['model_adjustment'],
            "model_developer": model_data['model_developer'],
            "model_approver": model_data['model_approver'],
            "model_maintenance": model_data['model_maintenance'],
            "documentation_code": model_data['documentation_code'],
            "implementation_plateform": model_data['implementation_plateform'],
            "production": model_data['production'],
            "model_file_path" : model_data['model_file_path'],
            "scoring_file_path" : model_data['scoring_file_path'],
            "binarize_scoring_flag": model_data['binarize_scoring_flag'],
            "modelName": model_data['modelName'],
            "registryOption": json.dumps(model_data['registryOption']),
            "fetchOption": json.dumps(model_data['fetchOption']),
            "dataPath": model_data['dataPath']
    }
    return data

def get_files(model_data):
        if model_data["datasetinsertionType"] == "Manual":
            training_dataset = model_data['training_dataset']
            pred_dataset = model_data['pred_dataset']
            actual_dataset = model_data['actual_dataset']
            test_dataset = model_data['test_dataset']
            model_image_path = model_data['model_image_path']
            model_summary_path = model_data['model_summary_path']
            model_file_path = model_data['model_file_path']

            files = {
                "training_dataset": open(training_dataset, 'rb'),
                "test_dataset": open(test_dataset, 'rb'),
                "pred_dataset": open(pred_dataset, 'rb'),
                "actual_dataset": open(actual_dataset, 'rb'),
                "model_image_path": open(model_image_path, 'rb'),
                "model_summary_path": open(model_summary_path, 'rb'),
                "model_file_path": open(model_file_path, 'rb')
            }
        else:
            files = {
                "training_dataset": "",
                "test_dataset": "",
                "pred_dataset": "",
                "actual_dataset": "",
                "model_image_path": "",
                "model_summary_path": "",
                "model_file_path": ""
            }
        return files

# def ml_options(model_data, ml_options):

#     return ml_options