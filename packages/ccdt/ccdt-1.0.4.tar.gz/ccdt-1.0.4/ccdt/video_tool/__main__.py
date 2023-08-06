import argparse
from ccdt.video_tool.split import Split


def get_args():
    parser = argparse.ArgumentParser('视频按帧切片（需要传入两个参数videos_dir，imgs_dir）')
    parser.add_argument('--input_dir',
                        default=r'C:/Users/54071/Desktop/55/data/rename_video_test',
                        # default='./test',
                        help='需要切片的视频路径(支持中文和英文)')
    parser.add_argument('--output_dir',
                        default=r'C:/Users/54071/Desktop/55/data/rename_video_test/output_video',
                        help='图片保存路径')
    parser.add_argument('--file_types',
                        default=['mp4', 'MP4', 'mov', 'avi', 'MOV', '264', 'dav', 'wmv'],
                        help='视频格式')
    parser.add_argument('--image_format', default='jpg', help='图片格式')
    parser.add_argument('--interval', default=50, help='几帧切一次')
    parser.add_argument('--function', type=str, help="输入操作功能参数:split只能输入单个")
    args = parser.parse_args()
    return args


def main(argument):
    if argument.function == 'split':
        videos_path, file_names = Split.get_videos_path(argument.input_dir, argument.output_dir, argument.file_types)
        for i in range(len(file_names)):
            Split.save_frame(videos_path[i], argument.interval, file_names[i])


if __name__ == '__main__':
    args = get_args()
    main(args)
