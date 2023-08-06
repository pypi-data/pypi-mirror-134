import argparse
import ccdt.video_tool.split


def get_args():
    parser = argparse.ArgumentParser('视频按帧切片（需要传入两个参数videos_dir，imgs_dir）')
    parser.add_argument('--input_dir',
                        default=r'C:/Users/54071/Desktop/55/data/rename_video_test',
                        help='需要切片的视频路径(支持中文和英文)')
    parser.add_argument('--output_dir',
                        default=r'C:/Users/54071/Desktop/55/data/rename_video_test/output_video',
                        help='图片保存路径')
    parser.add_argument('--file_types',
                        default=['mp4', 'MP4', 'mov', 'avi', 'MOV', '264', 'dav', 'wmv', 'AVI', 'avi',
                                 'webm', 'mkv', 'mkv', 'WMV', 'FLV', 'flv', 'MPG', 'mpg'],
                        help='视频文件格式')
    parser.add_argument('--image_format', default='jpg', help='图片格式')
    parser.add_argument('--interval', default=50, help='几帧切一次')
    parser.add_argument('--function', type=str, help="输入操作功能参数:split只能输入单个")
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    if args.function == 'split':
        videos_path, file_names = ccdt.Split.get_videos_path(args.input_dir, args.output_dir, args.file_types)
        for i in range(len(file_names)):
            ccdt.Split.save_frame(videos_path[i], args.interval, file_names[i])


if __name__ == '__main__':
    main()
