from requests.api import options
from mmanager.mmanager import Model
secret_key = '9cb2825b932f33e40556de3dfd415c0f395503e5'
url = 'URL'
path = 'assets'

model_data = {
    "project": "<project-id>", #project-id
    "transformerType": "Classification",
    "algorithmType": "Xgboost",
    "modelFramework": "other",
    "weight": "",
    "datasetinsertionType": "Manual",
    "training_dataset": "%s/model_assets/train.csv" % path,
    "pred_dataset": "%s/model_assets/pred.csv" % path,
    "actual_dataset": "%s/model_assets/truth.csv" % path,
    "test_dataset": "%s/model_assets/test.csv" % path,
    "model_image_path": "%s/model_assets/model_image.jpg" % path,
    "model_summary_path": "%s/model_assets/summary.json" % path,
    "model_file_path": "%s/model_assets/model.h5" % path,
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
}

ml_options = {
    "credPath": "config.json",
    "datasetUploadPath": "api_upload_test_2",
    "fetchOption": "",
    "modelName": "model-name",
    "dataPath": "",
    "registryOption": ["Model"],
}

Model(secret_key, url).post_model(model_data, ml_options)
