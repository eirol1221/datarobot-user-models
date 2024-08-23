# Python 3 GenAI drop-in template environment

This template environment can be used to create GenAI-powered custom models and includes common dependencies for workflows using OpenAI, Langchain, vector DBs, or transformers in PyTorch. 

## Supported Libraries

This environment is built for Python 3 and has support for the following libraries.
For specific version information and the complete list of included packages, see the [requirements](requirements.txt).

- openai
- langchain
- transformers
- sentence-transformers
- torch
- faiss-cpu
- numpy
- pandas
- scikit-learn
- optimum
- onnx
- onnxruntime
- google-cloud-aiplatform
- tiktoken

## Instructions

1. From the terminal, run `tar -czvf py_dropin.tar.gz -C /path/to/public_dropin_environments/python3_genai/ .`
2. Using either the API or from the UI, create a new custom environment with the tarball created
in step 1.

### Creating models for this environment

To use this environment, your custom model archive will typically contain a `custom.py` file containing the necessary hooks, as well as other files needed for your workflow. You can implement the hook functions such as `load_model` and `score_unstructured`, as documented [here](../../custom_model_runner/README.md).

Implement your Python code under the related custom hook functions to build your GenAI workflows. Within your `custom.py` code, import the necessary dependencies found in this environment.

If you need additional dependencies, add those packages in the `requirements.txt` file that you include within your custom model archive. DataRobot will make them available to your custom Python code after you build the environment.

