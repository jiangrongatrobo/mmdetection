# The new config inherits a base config to highlight the necessary modification
_base_ = '../fcos/fcos_r50_caffe_fpn_gn-head_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(bbox_head=dict(num_classes=34,))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ("fake poop b"
          ,"laundry basket"
          ,"folding chair"
          ,"dock(rubys+tanosv)"
          ,"cleaning robot"
          ,"scale"
          ,"whole bar stool b"
          ,"dust pan"
          ,"whole bar stool a"
          ,"shoe"
          ,"fan c"
          ,"flat base"
          ,"floor lamp"
          ,"coat rack"
          ,"pet feces"
          ,"sock"
          ,"handheld cleaner"
          ,"power strip"
          ,"rocking chair"
          ,"bar stool a"
          ,"fan"
          ,"fan b"
          ,"fake poop a"
          ,"whole fan b"
          ,"door mark b"
          ,"door mark c"
          ,"door mark a"
          ,"whole fan c"
          ,"wheel"
          ,"bar stool b"
          ,"dock(ruby)"
          ,"whole fan"
          ,"wire"
          ,"clothing item")
data = dict(
    train=dict(
        img_prefix='configs/baiguang34/train/images',
        classes=classes,
        ann_file='configs/baiguang34/train/annotations/instances_default.json'),
    val=dict(
        img_prefix='configs/baiguang34/val/images',
        classes=classes,
        ann_file='configs/baiguang34/val/annotations/instances_default.json'),
    test=dict(
        img_prefix='configs/baiguang34/val/images',
        classes=classes,
        ann_file='configs/baiguang34/val/annotations/instances_default.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'configs/baiguang34/fcos_r50_caffe_fpn_gn-head_1x_coco-821213aa.pth'

total_epochs = 20