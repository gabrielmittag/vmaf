import os
import pandas as pd

dataset_name = "vid_mos_set_1"
csv_file = "/mnt/vid_set_1/set_1.csv"
basefolder = "/mnt/vid_set_1/"

df = pd.read_csv(csv_file)
df = df[df['db_type']=='train']

yuv_fmt = 'notyuv'
quality_width = 1920
quality_height = 1080


dis_videos = []
ref_videos = []
for index, row in df.iterrows():
    
    video_name = row['video']
    video_url = row['video_url']
    vmaf_url = row['vmaf_url']
    video_source = row['videoSrc']
  
    ref_videos.append(
        {
        'content_id': index, 
        'path': os.path.join(basefolder, row['video'].replace('.mp4', '_ref.mp4')),
        }
    )    
    
    dis_videos.append(
        {
        'content_id': index, 
        'asset_id': index, 
        'groundtruth': row['MOS'], 
        'path': os.path.join(basefolder, row['video']),
        }
    )

