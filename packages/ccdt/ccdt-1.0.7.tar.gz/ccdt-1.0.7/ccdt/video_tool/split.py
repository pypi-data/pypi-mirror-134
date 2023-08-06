import os
import cv2


class Split(object):
    @classmethod
    def get_videos_path(cls, input_videos_dir, output_dir, file_formats):
        videos_path = []
        file_names = []
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        for root, dirs, files in os.walk(input_videos_dir, topdown=False):
            for filename in files:
                name = filename.split('.')
                if name[1] in file_formats:
                    videos_path.append(os.path.join(root, filename))
                    file_names.append(os.path.join(output_dir, name[0]))
                    if not os.path.exists(os.path.join(output_dir, name[0])):
                        os.mkdir(os.path.join(output_dir, name[0]))
        return videos_path, file_names

    @classmethod
    def save_frame(cls, video_path, interval, output_dir):
        video = 'video'
        video = cv2.VideoCapture(video_path)
        cur_frame = 0
        num = 1
        while True:
            ret, frame = video.read()
            if not ret:
                break
            if cur_frame % int(interval) == 0:
                video_dir, video_name = os.path.split(video_path)
                video_name, extension = os.path.splitext(video_name)
                # image_name = video_name + '_{:0>8d}.jpg'.format(cur_frame)
                image_name = '{:0>8d}.jpg'.format(cur_frame)
                img_dir = os.path.join(output_dir, image_name)
                cv2.imencode('.jpg', frame)[1].tofile(img_dir)
                num += 1
            cur_frame += 1
        print('视频分割完成 {}'.format(video_path))
