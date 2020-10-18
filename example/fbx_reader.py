# --*-- coding:utf-8 --*--
# @author: Xiao Shanghua
# @contact: hallazie@outlook.com
# @file: fbx_reader.py
# @time: 2020/10/18 15:42
# @desc:

import fbx
import FbxCommon


manager = fbx.FbxManager.Create()
scene = fbx.FbxScene.Create(manager, '')
importer = fbx.FbxImporter.Create(manager, '')
_ = importer.Initialize('Jump.fbx', -1)
_ = importer.Import(scene)

mesh = fbx.FbxMesh.Create(scene, 'output')


print(-1)