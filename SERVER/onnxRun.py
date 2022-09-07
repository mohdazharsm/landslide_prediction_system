import numpy as np
import onnx
import onnxruntime

model = "onnx_model.onnx"
session = onnxruntime.InferenceSession(model, None)
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name


def predict(inData):
    print("predict")
    data = np.array(
        [inData],
        dtype=np.float32,
    )
    result = session.run([output_name], {input_name: data})
    print(data)
    # # taking maximum probable value's index
    index_max = np.argmax(result)
    return index_max
