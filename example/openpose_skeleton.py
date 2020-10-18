# --*-- coding:utf-8 --*--
# @author: Xiao Shanghua
# @contact: hallazie@outlook.com
# @file: openpose_skeleton.py
# @time: 2020/10/17 14:09
# @desc:

import sys
import cv2
import os
import config
import matplotlib.pyplot as plt


try:
    root_path = config.OPENPOSE_ROOT_PATH
    try:
        sys.path.append(os.path.join(root_path, 'python\\openpose\\Release'))
        os.environ['PATH'] = os.environ['PATH'] + ';' + root_path + '\\x64\\Release;' + root_path + '\\bin;'
        import pyopenpose as op
    except ImportError as e:
        print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
        raise e

    params = dict()
    params['model_folder'] = config.OPENPOSE_MODEL_PATH
    params['hand'] = config.OPENPOSE_DETECT_HAND
    params['face'] = config.OPENPOSE_DETECT_FACE

    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    # Process Image
    datum = op.Datum()
    image = cv2.imread('G:\\images\\a-characters\\qi-sheng-luo-zbz2-0004.jpg')
    height, width, _ = image.shape
    print(f'raw shape: {height} x {width}')
    min_axis = min(height, width)
    height_ = 768 if height == min_axis else int(height * (768. / min_axis))
    width_ = 768 if width == min_axis else int(width * (768. / min_axis))
    datum.cvInputData = image
    opWrapper.emplaceAndPop([datum])

    keypoints = datum.poseKeypoints[0] if len(datum.poseKeypoints) > 0 else None
    if keypoints is None:
        sys.exit(0)
    print('key size:', len(keypoints))
    x_list = [int(x[0]) for x in keypoints]
    y_list = [int(x[1]) for x in keypoints]
    for x, y in zip(x_list, y_list):
        cv2.rectangle(image, (x-1, y-1), (x+1, y+1), (0, 255, 0), 10)

    # Display Image
    print('Body keypoints: \n' + str(keypoints))
    cv2.imshow('OpenPose 1.6.0 - Tutorial Python API', cv2.resize(image, (width_, height_)))
    # cv2.imshow('OpenPose 1.6.0 - Tutorial Python API', cv2.resize(datum.cvOutputData, (width_, height_)))
    cv2.waitKey(0)
except Exception as e:
    config.LOGGER.exception(e)
    sys.exit(-1)
