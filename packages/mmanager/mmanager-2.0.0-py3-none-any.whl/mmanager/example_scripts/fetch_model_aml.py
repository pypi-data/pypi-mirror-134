from requests.api import options
from mmanager.mmanager import Model
secret_key = '9cb2825b932f33e40556de3dfd415c0f395503e5'
url = 'http://localhost:8000'
path = 'assets'

model_data = {
    "project": 45,
    "transformerType": "Classification",
    "algorithmType": "Xgboost",
    "modelFramework": "other",
    "weight": "",
    "datasetinsertionType": "AzureML",
    "training_dataset": "",
    "pred_dataset": "",
    "actual_dataset": "",
    "test_dataset": "",
    "model_image_path": "",
    "model_summary_path": "",
    "model_file_path": "",
    "scoring_file_path": "",
    "target_column": "label",
    "note": "",
    "model_area": "apiUpload",
    "model_dependencies": "",
    "model_usage": "",
    "model_adjustment": "",
    "model_developer": "",
    "model_approver": "",
    "model_maintenance": "",
    "documentation_code": "",
    "implementation_plateform": "",
    "error_traceback": "",
    "distribution_error": False,
    "current_date": "",
    "production": "observation",
    "regulations": "",
    "score_data": "",
    "sweetviz": "",
    "error_traceback_distribution": "",
    "binarize_scoring_flag": False,
    "model_input_data": "",
    "modelscore_compute": False,
    "amlCred": "",
}

ml_options = {"credPath": "/home/mizal/Projects/mmanager_test/scripts/config.json",
              "datasetUploadPath": "ss",
              "fetchOption": ["Model"],
              "modelName": "histo",
              "dataPath": "train_histo",
              "registryOption": "",
              }

Model(secret_key, url).post_model(model_data, ml_options)
