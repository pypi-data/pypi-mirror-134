import glob
from PIL import Image


class GifConverter:
    def __init__(self, path_in=None, path_out=None, resize=(320, 240)):
        """
        path_in - 원본 이미지 경로(Ex - images/*.png)
        path_out - 결과 이미지 경로(Ex - output/filename.gif)
        resize - 결과 이미지 크기 변환
        """
        self.path_in = path_in or "./*.png"
        self.path_out = path_out or "./output.gif"
        self.resize = resize

    def convert_gif(self):
        """
        GIF 이미지 변환 기능 수행
        """
        print(self.path_in, self.path_out, self.resize)

        img, *images = [
            Image.open(f).resize(self.resize, Image.ANTIALIAS)
            for f in sorted(glob.glob(self.path_in))
        ]

        try:
            img.save(
                fp=self.path_out,
                format="GIF",
                append_images=images,
                save_all=True,
                duration=500,
                loop=0,
            )
        except IOError:
            print("Cannot convert!", img)


# 이 파일에서만 직접 실행할 경우에만 동작하도록, 다른파일에서 import로 가져가서 사용할 때 동작하지 못하도록하기 위함.
if __name__ == "__main__":
    # 클래스
    c = GifConverter(
        "./project/images/*.png", "./project/image_out/result2.gif", (420, 340)
    )

    # 변환
    c.convert_gif()
