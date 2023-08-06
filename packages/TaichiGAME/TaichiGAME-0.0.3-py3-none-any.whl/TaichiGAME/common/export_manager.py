import os
import glob


class ExportManager():
    def __init__(self, root_dir: str = './export-res'):
        try:
            os.makedirs(root_dir + '/frames')
        except FileExistsError:
            for infile in glob.glob(os.path.join(root_dir + '/frames',
                                                 '*.png')):
                os.remove(infile)

        self._frame_cnt: int = -1
        self._root_dir: str = root_dir

    @property
    def frame_name(self) -> str:
        self._frame_cnt += 1
        return self._root_dir + f'/frames/{self._frame_cnt:05d}.png'

    def gen_video(self) -> None:
        print('export .mp4 video...')
        os.chdir(self._root_dir + '/frames')
        os.system('ti video -f24')
        os.system('mv video.mp4 ../')

    def gen_gif(self) -> None:
        print('export .gif ...')
        os.chdir(self._root_dir + '/frames')
        os.system('ti video -f24')
        os.system('ti gif -i video.mp4 -f24')
        os.system('mv video.gif ../')
